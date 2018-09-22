import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances


class Similarities:

    def __init__(self, df_user_item):
        self.df_initial_user_similarities = self._set_total_usr_usr_simis(df_user_item)
        self.df_user_similarities = {}

    def _set_total_usr_usr_simis(self, df_user_item):
        """Compute initial user-user-similarities (for all metrics) across all users in the provided ratings-data.

        These can later be substituted with in-cluster similarities where needed.
        """
        total_similarities = {}
        for metric in ['correlation', 'cosine', 'dice', 'jaccard']:
            total_similarities[metric] = self._create_user_user_sim(df_user_item, metric=metric)
        return total_similarities

    def create_usr_usr_sim(self, df_user_item, user_id):
        self.df_user_similarities[user_id] = self._set_total_usr_usr_simis(df_user_item)

    def _create_user_user_sim(self, df_user_item, users=None, metric='cosine'):
        """Users can be provided to compute similarities only across the specified users."""
        if users is not None:
            df_user_item_updated = df_user_item.loc[users, :]
            user_similarity = pd.DataFrame(1 - pairwise_distances(df_user_item_updated, metric=metric),
                                           index=df_user_item_updated.index,
                                           columns=df_user_item_updated.index)
            return user_similarity
        else:
            user_similarity = pd.DataFrame(1 - pairwise_distances(df_user_item, metric=metric),
                                           index=df_user_item.index,
                                           columns=df_user_item.index)
            return user_similarity

    # not tested yet /!\
    def update_user_user_sim(self, df_user_item, users, metric):
        """Update user_similarities[metric] to the user-simis only accounting for subset of users."""
        self.df_initial_user_similarities[metric] = self._create_user_user_sim(df_user_item, users, metric=metric)

    def get_user_similarity(self, current_user, metric="cosine"):
        return self.df_user_similarities[current_user][metric]

    def get_similar_users(self, current_user, metric="cosine", simi_threshhold=0):
        df_sim_mat = self.get_user_similarity(current_user, metric)
        similar_users = list(df_sim_mat[df_sim_mat.loc[current_user] > simi_threshhold].index)
        similar_users.remove(current_user)
        return similar_users
