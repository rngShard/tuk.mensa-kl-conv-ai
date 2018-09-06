import pandas as pd


class IdMatcher:

    def __init__(self, path_current, path_meals):
        self.path_current = path_current
        self.path_meals = path_meals
        self.df_current = pd.read_csv(path_current, encoding='utf-8', engine="python")
        self.df_meals = pd.read_csv(path_meals, encoding='utf-8')

    def match_ids(self):
        next_id = self.df_meals.m_id.max() + 1
        m_ids = []
        rows = []
        for i in self.df_current.iterrows():
            title = i[1].title_norm
            if sum(self.df_meals.title_norm.isin([title])) > 0:
                m_ids.append(self.df_meals[self.df_meals["title_norm"] == title].m_id)
            else:
                m_ids.append(next_id)
                current_list = list(self.df_current[self.df_current.title_norm.isin([title])].iloc[0])
                new_row = [next_id] + current_list
                rows.append(new_row)
                print(rows)
                next_id += 1
                last_index = self.df_meals.iloc[-1].name
        for k, v in enumerate(rows):
            if v[0] not in self.df_meals.m_id.values:
                self.df_meals.loc[last_index + 1 + k] = rows[k]
        m_ids = [int(i) for i in m_ids]
        self.df_current.insert(0, "m_id", m_ids)

    def export_meal_to_csv(self, absolute_path=None):
        path = self.path_meals
        if absolute_path is None:
            current_file = os.path.abspath(os.path.dirname(__file__))
            os_file_path = os.path.join(current_file, path)
            self.df_meals.to_csv(os_file_path, encoding='utf-8', index=False)
        else:
            self.df_meals.to_csv(path, encoding='utf-8', index=False)

    def export_current_to_csv(self, absolute_path=None):
        path = self.path_current
        if absolute_path is None:
            current_file = os.path.abspath(os.path.dirname(__file__))
            os_file_path = os.path.join(current_file, path)
            self.df_current.to_csv(os_file_path, encoding='utf-8', index=False)
        else:
            self.df_current.to_csv(path, encoding='utf-8', index=False)
