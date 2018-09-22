import numpy as np


def predict_rating(current_user, df_user_similarity, df_user_item, df_meals, similar_users, m_id=None,
                   metric='cosine', explain=False):
    # if no list of similar_user provided, compute it first
    # if len(similar_users) == 0:
    #    similar_users = self.similarities.get_similar_users(current_user, metric)

    if explain:
        print("Similar users: {}".format(similar_users))
        if m_id is None:
            print("Predicting ratings for user {} with `{}`".format(current_user, metric))
        else:
            print("Predicting rating for user {} & meal {} ({}) with `{}`".format(current_user, m_id,
                                                                                  df_meals[
                                                                                      df_meals[
                                                                                          'm_id'] == m_id].loc[:,
                                                                                  'uTitle'].to_string(), metric))
            print("... with sim. user ratings of {} for meal {}".format(
                [df_user_item.loc[u, m_id] for u in similar_users], m_id))

    # if no meal_id provided, predict ratings for all known meals (probably only for debugging) ...
    if m_id is None:
        return _bulk_predict(current_user, df_user_item, similar_users, metric)
    else:
        # ... otherwise predict for user X rating of meal Y
        return _predict(current_user, df_user_similarity, df_user_item, similar_users, m_id, metric)


def _predict(current_user, df_user_similarity, df_user_item, similar_users, m_id, metric):
    real_rating = df_user_item.loc[current_user].loc[m_id]
    if real_rating != 0:
        return real_rating
    else:
        sum_ratings, sum_sim = 0, 0
        for sim_user in similar_users:
            similarity = df_user_similarity.loc[current_user].loc[
                sim_user]
            rating = df_user_item.loc[sim_user].loc[m_id]
            if rating == 0:
                continue
            sum_ratings += rating * similarity
            sum_sim += similarity
        if sum_sim == 0:
            return 0
        else:
            prediction = sum_ratings / sum_sim
            return prediction


def _bulk_predict(current_user, df_user_item, similar_users, metric):
    """Note that now m_id not explicitely given, but rather compute all ratings of 0-rating (Debugging only?) ."""
    preserved_current_rating = df_user_item.loc[current_user].replace(0, np.nan)

    aggregated_similar_user_ratings = df_user_item.loc[similar_users].replace(0, np.nan)
    # print(aggregated_similar_user_ratings.head())
    aggregated_similar_user_ratings['user'] = [current_user for _ in
                                               range(len(aggregated_similar_user_ratings.index))]
    # print(aggregated_similar_user_ratings.head())
    aggregated_similar_user_ratings = aggregated_similar_user_ratings.groupby('user').mean().fillna(0)
    # print(aggregated_similar_user_ratings)

    for idx, preserved_rating in preserved_current_rating.iteritems():
        if preserved_rating > 0:
            aggregated_similar_user_ratings.loc[:, idx] = preserved_rating
    return aggregated_similar_user_ratings


def predict_cluster(current_user, df_user_item, cluster_neighbors, m_id=None):
    # real_ratings = df_user_item.loc[current_user]
    if m_id is None:
        return _bulk_predict_average(current_user, df_user_item, cluster_neighbors)
    else:
        return _predict_average(current_user, df_user_item, cluster_neighbors, m_id)


def _predict_average(current_user, df_user_item, cluster_neighbors, m_id):
    real_rating = df_user_item.loc[current_user].loc[m_id]
    if real_rating != 0:
        return real_rating
    ratings = df_user_item[df_user_item.index.isin(cluster_neighbors)].loc[
              :, m_id]
    average_prediction = ratings.where(ratings > 0).mean()
    if np.isnan(average_prediction):
        return 0
    else:
        return average_prediction


def _bulk_predict_average(current_user, df_user_item, cluster_neighbors):
    preserved_current_rating = df_user_item.loc[current_user]
    ratings = df_user_item[df_user_item.index.isin(cluster_neighbors)]
    average_prediction = ratings.where(ratings > 0).mean()
    for idx, preserved_rating in preserved_current_rating.iteritems():
        if preserved_rating > 0:
            average_prediction[idx] = preserved_rating
    return average_prediction
