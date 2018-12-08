from GoogleTrendAPI import *
from Celeb import *
import time
import pandas as pd
from tqdm import tqdm
from datetime import datetime
import datetime

if __name__ == '__main__':

    #database = DataBase()
    # df = pd.DataFrame()
    #database.get_celeb_excel_file()
    df = pd.read_excel('/Users/mycelebs/Desktop/total_query.xlsx')
    celeb_name = df['cd_name']
    celeb_search_list = df['search_term']
    today = time.strftime('%Y-%m-%d')
    start = today.replace("2018", "2016")
    country_code = ['tw','vn','jp','th','fr','kr','ch']
    country_name=['대만','베트남','일본','태국','프랑스','한국','중국']
    goo = GoogleTrendAPI()
    total_country_query = []

    def related_queries(i, country_idx):
        celeb = Celeb(celeb_search_list[i], start, today, country_code[country_idx], celeb_name[i])
        result = goo.get_related_queries(celeb)
        return result

    def interest_time_value(i, country_idx):
        celeb = Celeb(celeb_search_list[i],start,today,country_code[country_idx],celeb_name[i])
        result = goo.get_interest_over_time(celeb)
        return result

    for country_idx in range(len(country_code)):
        related_queries_list = []
        for celeb_idx in tqdm(range(len(celeb_search_list))):
            related_query = related_queries(celeb_idx, country_idx)
            related_queries_list.append(related_query)
        total_country_query.append(related_queries_list)
        print(total_country_query[country_idx])

    # def slash_query(related_query):
    #     query_array = []
    #     for i in tqdm(range(len(related_query))):
    #         sub_query = []
    #         for idx, row in related_query[i].iterrows():
    #             sub_query.append(row['query'])
    #
    #         query_array.append('/'.join(sub_query))
    #
    #     return query_array

    dataframes = []
    dataframes.append(df)
    for i in range(len(total_country_query)):
        result = goo.add_slash_query(total_country_query[i])
        sub_df = pd.DataFrame({'associate_word_' + country_code[i]: result})
        dataframes.append(sub_df)

    # 국가별 연관검색어 결과
    #pd.concat(dataframes, axis=1).to_excel('excel/celeb_info3.xlsx', index=False)
    pd.concat(dataframes, axis=1).to_excel('excel/total_query_1.xlsx', index=False)

    ################################아래부턴 시간별 관심도
    test_result=[]
    test_country=[]
    test_celeb_name=[]
    last_df = pd.DataFrame()
    country_today = time.strftime('%Y-%m')
    total_country=[]

    for country_idx in tqdm(range(len(country_code)-1)):
        country_queries=[]
        for celeb_idx in tqdm(range(len(celeb_search_list))):
            country_query = interest_time_value(celeb_idx, country_idx)
            time.sleep(2)
            country_queries.append(pd.DataFrame(country_query))
        total_country.append(country_queries)


    for i in range(len(total_country)):
        results=[]
        for j in range(len(celeb_search_list)):
            try:
                # total_country[i][j]의 타입은 데이터프레임, 년도와 월을 기준으로 관심도결과를 평균냄(mean)
                res = total_country[i][j].groupby(total_country[i][j][celeb_search_list[j]].keys().strftime('%-Y-%m')).mean()
            except:
                # 만약에 관심도 결과가 없는경우 셀럽 이름으로 된 데이터 프레임을 만들어줌
                res = pd.DataFrame({celeb_search_list[j]: [celeb_name[j]]})
                pass
            for k in range(len(res)):
                test_country.append(country_name[i])
                test_celeb_name.append(celeb_name[j])
            results.append(res)
        test_result.append(results)


    for i in tqdm(range(len(test_result))):
       for j in range(len(test_result[i])):
            k = test_result[i][j].reset_index()
            if len(k['index'].head()) == 1:
                k['index'] = country_today
            k.columns = ['cgs_search_date', 'cgs_search_count']
            last_df = pd.concat([last_df,k], axis=0)

    last_df['cd_idx'] = test_celeb_name
    last_df['cgs_country'] = test_country
    last_df['cgs_search_date'] = last_df['cgs_search_date'].apply(lambda x : set_date(x))
    last_df['cgs_search_count'] = last_df['cgs_search_count'].apply(lambda x: set_count(x))
    #last_df.to_excel('excel/last_time_value3.xlsx', index=False)
    last_df.to_excel('excel/total_query_2.xlsx', index=False)


    def set_date(x):
        try:
            yy = datetime.datetime.strptime(str(x), '%Y-%M')
            return yy.strftime('%Y-%M-01 00:00:00')
        except Exception as e:
            return

    def set_count(x):
        if type(x) != float:
            x = 0
        return x
