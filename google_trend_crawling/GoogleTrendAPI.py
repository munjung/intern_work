from pytrends.request import TrendReq
import time
from tqdm import tqdm
import pandas as pd

class GoogleTrendAPI():

    def __init__(self):
        self.pytrend = TrendReq()
        self.result = ''
        self.none_type_dic = ''

    def get_interest_over_time(self, cel):
        time.sleep(1)
        self.pytrend.build_payload(kw_list=[cel.celebCode], timeframe=cel.totalPeriod(), geo=cel.convertAlpha())
        time.sleep(2)
        try:
            time_result = self.pytrend.interest_over_time()[cel.celebCode]
        except:
            time_result = pd.DataFrame({cel.celebCode: [cel.celebName]})
            pass
        return time_result

    def get_related_queries(self, cel):
        self.pytrend.build_payload(kw_list=[cel.celebCode], timeframe=cel.totalPeriod(), geo=cel.convertAlpha())
        time.sleep(1)
        if self.pytrend.related_queries()[cel.celebCode]['rising'] is None:
            self.none_type_dic = pd.DataFrame({'query': [cel.celebName]})
            self.result = self.none_type_dic
        else:
            query_len = len(self.pytrend.related_queries()[cel.celebCode]['rising'])
            if query_len >= 3:
                self.result = self.pytrend.related_queries()[cel.celebCode]['rising'].head(3)

            else:
                self.result = self.pytrend.related_queries()[cel.celebCode]['rising'].head(query_len)

        return self.result

    def add_slash_query(self, related_query):
        query_array = []
        for i in tqdm(range(len(related_query))):
            sub_query = []
            for idx, row in related_query[i].iterrows():
                sub_query.append(row['query'])
            query_array.append('/'.join(sub_query))
        return query_array
