import pymysql
import pandas as pd
import requests
import urllib
from bs4 import BeautifulSoup
import time
import json
import re
from difflib import SequenceMatcher
from PIL import Image


def kobis_movie_list_by_month(month):
    db_connection = #데이터베이스 정보
    movie_DB = pd.read_sql('SELECT md_kobis_movie_code FROM movie_DB', db_connection)

    pre_movie_code_list = [x.replace('m_','') for x in list(movie_DB.md_kobis_movie_code)]
    url = 'http://kobis.or.kr/kobis/business/mast/mvie/findOpenScheduleList.do?sDate='+ str(month) + '&sNationCd=03&viewEa=500'
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml')
    table_soup = soup.find(class_='scheduleList').find('tbody')
    kobis_movie_list = [table_soup.findAll('tr')[i].findAll('td')[0].text.strip() for i in range(len(table_soup.findAll('tr')))]
    open_date_list = [table_soup.findAll('tr')[i].findAll('td')[3].text.strip() for i in range(len(table_soup.findAll('tr')))]

    new_kobis_movie_list = []
    for kobis_movie_code in kobis_movie_list:
        if str(kobis_movie_code) not in pre_movie_code_list:
            new_kobis_movie_list.append(kobis_movie_code)
        else:
            pass
    return list(set(new_kobis_movie_list))


def delete_value_in_list(keywords, lst):
    del_keyword_list = keywords.split(',')
    for kword in del_keyword_list:
        if kword in lst:
            lst.remove(kword)

    return lst

def get_similar_name(name):
    dellist = '스타,셀럽,배우,가수,개그맨,여배우,연예인,웹툰,만화,카툰,보다,볼 거,영화,무비,애니,애니메이션,작품,보다,볼 거,방송,티비,티브이,텔레비,드라마,예능,TV,보다,볼 거,아트,작품,예술,그림,와인,비어,맥주,의류,옷,패션,입다,입을,입을만한,숙박,호텔,모텔,모탤,펜션,팬션,게하,개하,게스트하우스,숙소,여관,여인숙,개스트하우스,놀다,가다,맛집,맛 집,음식,먹다,먹지,먹을거,식당,밥집,레스토랑,요리,먹다,먹지,먹을거,립스틱,틴트,메이크업,파운데이션,아이쉐도우,아이섀도우,립라이너,비비크림,립밤,아이라이너,파우더,화장품,명소,가볼 만한 장소,가볼 만한 여행지,가볼 만한데,놀 만한 여행지,놀만한 여행지,놀 만한 장소,놀만한 장소,갈 만한 여행지,갈만한 여행지,갈 만한 장소,갈만한 장소,가기좋은데,가기 좋은데,갈 만한데,갈만한데,놀기 좋은데,놀 만한데,놀만한데,놀다,가다,여행지,여행,편의시설,마트,슈퍼,편의점,선물,기프트,헤어,헤어스타일,머리스타일,머리,간편식품,즉석식품,인스턴트식품,먹다,먹지,먹을거,음악,노래,뮤직,듣다,들을거,들을만한,들을,가방,사다,살까,지갑,패션소품,모자,벨트,넥타이,손수건,스카프,머플러,키홀더,장갑,양말,케이스,우산,다이어리,악세사리,아이웨어,선글라스,안경,시계,워치,사다,살까,장신구,주얼리,목걸이,반지,피어싱,펜던트,쥬얼리,사다,살까,커피전문점,커피숍,스타벅스,스벅,투썸플레이스,투썸,탐앤탐스,탐탐,이디야커피,이디야,폴바셋,엔제리너스,엔젤리너스,커피빈,프랜차이즈음식점,호식이두마리치킨,호식이,호식이 두마리,호식이 두마리 치킨,교촌치킨,교촌 치킨,부어치킨,부어 치킨,네네치킨,네네 치킨,멕시카나,멕시칸,파리바게뜨,빠리바게뜨,빠바,보네스뻬,도미노피자,도미노 피자,도미노,피자스쿨,피자 스쿨,BBQ,비비큐,BHC,비에치씨,굽네치킨,굽네,굽네 치킨,돈치킨,돈 치킨,파리크로아상,파리 크로아상,파리 크라상,파리크라상,뚜레쥬르,뚜레주르,따삐오,맥도날드,맥날,롯데리아,롯데 리아,버거킹,버거 킹,KFC,미스터피자,미피,피자헛,피자 헛,파파존스피자,파파존스,피자마루,피자 마루,피자에땅,피자에 땅,피자 에땅,치킨매니아,치킨 매니아,빠리바게트,파리바게트,호식이치킨,즐기다,즐길만한거,즐길거,즐길데,즐길 데,놀다,놀만한거,놀거,놀만한데,놀만한 데,쉬다,쉴만한거,쉴거,쉴만한데,쉴만한 데,할만한거,할거,할만한데,할만한 데,액티비티,투어,체험,데이트,입장권,도서,에세이책,육아책,종교책,역사책,자기계발책,소설책,만화책,유아책,여행책,대중문화책,과학책,요리책,컴퓨터책,아이티책,책,신발,슈즈,구두,스니커즈,등산화,레인부츠,부츠,스니커즈,슬립온,플랫,런닝화,운동화'

    sim_add_1 = re.sub('[^가-힣 ]', '', name).replace('  ',' ')
    if len(sim_add_1) == 1:
        sim_add_1 = ''
    sim_add_2 = re.sub('[^가-힣]', '', name)
    if len(sim_add_2) == 1:
        sim_add_2 = ''
    sim_add_3 = re.sub('[^가-힣 \w]', '', name).replace('  ', ' ')
    if len(sim_add_3) == 1:
        sim_add_3 = ''
    sim_list = list(set([sim_add_1, sim_add_2, sim_add_3]))
    sim_list = delete_value_in_list(dellist,sim_list)
    if '' in sim_list:
        sim_list.remove('')
    if ' ' in sim_list:
        sim_list.remove(' ')
    if '  ' in sim_list:
        sim_list.remove('  ')
    return ','.join(sim_list)



class MovieMetaCrawl():
    def __init__(self, api_key, kobis_movie_code, people_df):
        self.api_key = api_key
        self.kobis_movie_code = kobis_movie_code
        self.json_data_one_depth_key_list = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'showTm', 'prdtYear',
                                             'openDt', 'prdtStatNm', 'typeNm']
        self.api_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'.format(api_key,kobis_movie_code)
        self.one_depth_key_list = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'showTm', 'prdtYear', 'openDt',
                                   'prdtStatNm', 'typeNm']
        self.people_info_url = 'http://kobis.or.kr/kobis/business/mast/mvie/searchMovieDtl.do'
        self.people_df = people_df

    def get_json_data_api(self):
        r = requests.get(self.api_url).text
        self.json_data_api = json.loads(r)
        return self.json_data_api

    def get_etc_data(self):
        kobis_movie_code = self.kobis_movie_code
        url = 'http://kobis.or.kr/kobis/business/mast/mvie/searchMovieDtl.do?code={}'.format(kobis_movie_code)
        r = requests.get(url).text
        info_soup = BeautifulSoup(r, 'lxml')
        try:
            self.synopsis = info_soup.find('p', {'class': 'contentBreak'}).text.replace('\r', '').replace('\t',
                                                                                                          '').replace(
                '\n', '')
        except:
            self.synopsis = ''

        main_poster = info_soup.find('article', {'class': 'basicInfo'})
        try:
            self.main_poster_url = 'http://kobis.or.kr' + main_poster.find('img').get('src').replace('thumb/thn_', '')
        except:
            self.main_poster_url = ''

        self.etc_data_dict = {
            'md_synopsys': self.synopsis,
            'md_mainposter_url': self.main_poster_url
        }

        return self.etc_data_dict

    def get_json_data_actor(self):
        kobis_movie_code = self.kobis_movie_code
        url = 'http://kobis.or.kr/kobis/business/mast/mvie/searchMovActorLists.do'
        f_data = {'movieCd': str(kobis_movie_code)}
        h_data = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate',
                  'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2,ja;q=0.2',
                  'Connection': 'keep-alive',
                  'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded',
                  'Cookie': 'ACEFCID=UID-57FDCABD8390CCEDD399C152; JSESSIONID=qycTYDJT3F33RhBsxrqckGBSG2GMTh9J16vn20G6hJr5GytVGtDQ!-134877309!1349909687',
                  'Host': 'kobis.or.kr', 'Origin': 'http://kobis.or.kr',
                  'Referer': 'http://kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        r = requests.post(url, data=f_data, headers=h_data).text
        actor_soup = BeautifulSoup(r, 'lxml')
        actor_htxt = actor_soup.find('p').text
        self.json_data_actor = json.loads(actor_htxt)
        return self.json_data_actor

    def get_json_data_staff(self):
        kobis_movie_code = self.kobis_movie_code
        url = 'http://kobis.or.kr/kobis/business/mast/mvie/searchMovStaffLists.do'
        f_data = {'movieCd': str(kobis_movie_code)}
        h_data = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate',
                  'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2,ja;q=0.2',
                  'Connection': 'keep-alive',
                  'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded',
                  'Cookie': 'ACEFCID=UID-57FDCABD8390CCEDD399C152; JSESSIONID=qycTYDJT3F33RhBsxrqckGBSG2GMTh9J16vn20G6hJr5GytVGtDQ!-134877309!1349909687',
                  'Host': 'kobis.or.kr', 'Origin': 'http://kobis.or.kr',
                  'Referer': 'http://kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        r = requests.post(url, data=f_data, headers=h_data).text
        staff_soup = BeautifulSoup(r, 'lxml')
        staff_htxt = staff_soup.find('p').text
        self.json_data_staff = json.loads(staff_htxt)
        return self.json_data_staff

    def get_movie_info(self):
        json_data_api = self.get_json_data_api()
        json_etc_data = self.get_etc_data()
        self.one_depth_dict = {x: json_data_api['movieInfoResult']['movieInfo'][x] for x in self.one_depth_key_list}
        self.basic_info_df = pd.DataFrame({0: self.one_depth_dict}).T  # 임의의 인덱스번호임. 0 으로 디폴트 적용
        try:
            self.open_date = pd.to_datetime(self.one_depth_dict['openDt']).strftime('%Y-%m-%d')
        except:
            self.open_date = self.one_depth_dict['openDt']

        nation_list = json_data_api['movieInfoResult']['movieInfo']['nations']
        self.making_country = ','.join([dic['nationNm'] for dic in nation_list])

        # director
        directors_list = json_data_api['movieInfoResult']['movieInfo']['directors']
        self.directors_kor_nm = ','.join([dic['peopleNm'] for dic in directors_list])
        self.directors_en_nm = ','.join([dic['peopleNmEn'] for dic in directors_list])

        # actors
        actors_list = json_data_api['movieInfoResult']['movieInfo']['actors']
        self.actors_kor_nm = ','.join([dic['peopleNm'] for dic in actors_list])
        self.actors_en_nm = ','.join([dic['peopleNmEn'] for dic in actors_list])
        self.actors_cast = ','.join([dic['cast'] for dic in actors_list])
        self.actors_cast_en = ','.join([dic['castEn'] for dic in actors_list])

        # genre
        genres_list = json_data_api['movieInfoResult']['movieInfo']['genres']
        self.sub_genres = ','.join([dic['genreNm'] for dic in genres_list]).replace('멜로/로맨스', '로맨스/멜로')

        # grade
        if len(json_data_api['movieInfoResult']['movieInfo']['audits']) != 0:
            self.grade_info = json_data_api['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'].replace('이상',
                                                                                                                 '')
        else:
            self.grade_info = ''

        # company
        companies_dict = {x['companyPartNm']: x['companyNm'] for x in
                          json_data_api['movieInfoResult']['movieInfo']['companys']}
        try:
            self.publ_com = companies_dict['배급사']
        except:
            self.publ_com = ''

        try:
            self.impo_com = companies_dict['수입사']
        except:
            self.impo_com = ''

        try:
            self.prod_com = companies_dict['제작사']
        except:
            self.prod_com = ''

        self.info_data_dict = {

            "md_kobis_movie_code": self.one_depth_dict['movieCd'],
            "md_name": self.one_depth_dict['movieNm'],
            "md_name_en": self.one_depth_dict['movieNmEn'],
            "md_running_time": self.one_depth_dict['showTm'],
            "md_date": self.open_date,
            "md_type": self.one_depth_dict['typeNm'],
            "md_genre": self.sub_genres,
            "md_sub_genre": self.sub_genres,
            "md_publisher": self.publ_com,
            "md_importer": self.impo_com,
            "md_produce_company": self.prod_com,
            "md_making_country": self.making_country,
            "md_grade": self.grade_info,
            "md_synopsys": json_etc_data['md_synopsys'],
            "md_mainposter_url": json_etc_data['md_mainposter_url']
        }
        return self.info_data_dict

    def get_movie_info_people(self):
        self.json_data_actor = self.get_json_data_actor()
        self.json_data_staff = self.get_json_data_staff()

        df_actors = pd.DataFrame(self.json_data_actor)
        df_actors = df_actors.applymap(lambda x: str(x))
        df_actors = df_actors.applymap(lambda x: x.replace('None', ''))
        try:
            self.main_actors_name = ','.join(
                list(df_actors[df_actors['actorGb'] == '1'].reset_index(drop=True)['peopleNm']))
            self.main_actors_name_en = ','.join(
                list(df_actors[df_actors['actorGb'] == '1'].reset_index(drop=True)['peopleNmEn']))
            self.main_actors_code = ','.join(
                list(df_actors[df_actors['actorGb'] == '1'].reset_index(drop=True)['peopleCd']))
            self.main_actors_cast = ','.join(
                list(df_actors[df_actors['actorGb'] == '1'].reset_index(drop=True)['cast']))
            self.sub_actors_name = ','.join(
                list(df_actors[df_actors['actorGb'] == '2'].reset_index(drop=True)['peopleNm']))
            self.sub_actors_name_en = ','.join(
                list(df_actors[df_actors['actorGb'] == '2'].reset_index(drop=True)['peopleNmEn']))
            self.sub_actors_code = ','.join(
                list(df_actors[df_actors['actorGb'] == '2'].reset_index(drop=True)['peopleCd']))
            self.sub_actors_cast = ','.join(list(df_actors[df_actors['actorGb'] == '2'].reset_index(drop=True)['cast']))
        except:
            self.main_actors_name = ''
            self.main_actors_name_en = ''
            self.main_actors_code = ''
            self.main_actors_cast = ''
            self.sub_actors_name = ''
            self.sub_actors_name_en = ''
            self.sub_actors_code = ''
            self.sub_actors_cast = ''

        df_staffs = pd.DataFrame(self.json_data_staff)
        df_staffs = df_staffs.applymap(lambda x: str(x))
        df_staffs = df_staffs.applymap(lambda x: x.replace('None', ''))
        try:
            self.directors_name = ','.join(
                list(df_staffs[df_staffs['roleNm'] == '감독'].reset_index(drop=True)['peopleNm']))
            self.directors_name_en = ','.join(
                list(df_staffs[df_staffs['roleNm'] == '감독'].reset_index(drop=True)['peopleNmEn']))
            self.directors_code = ','.join(
                list(df_staffs[df_staffs['roleNm'] == '감독'].reset_index(drop=True)['peopleCd']))
        except:
            self.directors_name = ''
            self.directors_name_en = ''
            self.directors_code = ''

        self.people_data_dict = {

            'md_main_actors': self.main_actors_name,
            'md_mainactor_en': self.main_actors_name_en,
            'md_kobis_mainactor_code': self.main_actors_code,
            'md_main_character': self.main_actors_cast,
            'md_sub_actors': self.sub_actors_name,
            'md_subactor_en': self.sub_actors_name_en,
            'md_kobis_subactor_code': self.sub_actors_code,
            'md_sub_character': self.sub_actors_cast,
            'md_director': self.directors_name,
            'md_director_en': self.directors_name_en,
            'md_kobis_director_code': self.directors_code

        }

        return self.people_data_dict

    def get_celeb_idx_matching(self):
        """
        :param kobis_people_code: kobis 인물 코드가 콤마단위로 들어가있는 데이터를 입력
        :return: cd_idx 와 매칭하여 결과 출력
        """
        # director
        people_data = self.get_movie_info_people()
        celeb_data = self.people_df
        directors_celeb_idx_list = []
        if people_data['md_kobis_director_code'] != '':
            for code in people_data['md_kobis_director_code'].split(','):
                try:
                    celeb_idx = str(celeb_data[celeb_data['kobis_people_id'] == int(code)]['celeb_idx'].values[0])
                except:
                    celeb_idx = '-'
                directors_celeb_idx_list.append(celeb_idx)
        self.directors_celeb_idx = ','.join(directors_celeb_idx_list)

        # main_actor
        main_actors_celeb_idx_list = []
        if people_data['md_kobis_mainactor_code'] != '':
            for code in people_data['md_kobis_mainactor_code'].split(','):
                try:
                    celeb_idx = str(celeb_data[celeb_data['kobis_people_id'] == int(code)]['celeb_idx'].values[0])
                except:
                    celeb_idx = '-'
                main_actors_celeb_idx_list.append(celeb_idx)
        self.main_actors_celeb_idx = ','.join(main_actors_celeb_idx_list)

        # sub_actor
        sub_actors_celeb_idx_list = []
        if people_data['md_kobis_subactor_code'] != '':
            for code in people_data['md_kobis_subactor_code'].split(','):
                try:
                    celeb_idx = str(celeb_data[celeb_data['kobis_people_id'] == int(code)]['celeb_idx'].values[0])
                except:
                    celeb_idx = '-'
                sub_actors_celeb_idx_list.append(celeb_idx)

        self.sub_actors_celeb_idx = ','.join(sub_actors_celeb_idx_list)

        self.celeb_idx_matching_dict = {

            'md_director_celeb_idx': self.directors_celeb_idx,
            'md_mainactor_celeb_idx': self.main_actors_celeb_idx,
            'md_subactor_celeb_idx': self.sub_actors_celeb_idx

        }

        return self.celeb_idx_matching_dict

    def get_naver_movie_code(self):
        movie_title = self.get_movie_info()['md_name']
        director_name = self.get_movie_info_people()['md_director']

        query = re.sub('([^a-zA-Z0-9가-힣 -])', ' ', movie_title).replace('확장판', '').replace('무삭제판', '').replace('무삭제',
                                                                                                               '').replace(
            '무삭특별판', '')
        url = 'http://movie.naver.com/movie/search/result.nhn?section=movie&query={}&section=all&ie=utf8'.format(query)
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'lxml')
        search_keyword = movie_title.replace(' ', '') + director_name.replace(' ', '')

        naver_movie_nomi_list_df = pd.DataFrame()
        if str(soup.find('ul', {'class': 'search_list_1'})) != 'None':
            for i in range(len(soup.find('ul', {'class': 'search_list_1'}).findAll('li'))):
                try:
                    naver_title = soup.find('ul', {'class': 'search_list_1'}).findAll('li')[i].find('dl').find(
                        'dt').find('a').text.strip()
                    naver_title = re.sub('(\(.*?\))', '', naver_title).replace(' ', '')
                except:
                    naver_title = 'no_info'

                try:
                    naver_url = \
                        soup.find('ul', {'class': 'search_list_1'}).findAll('li')[i].find('dl').find('dt').find('a')[
                            'href']
                except:
                    naver_url = 'no_info'

                try:
                    if '감독' in str(soup.find('ul', {'class': 'search_list_1'}).findAll('li')[i].find('dl').findAll('dd',
                                                                                                                   {
                                                                                                                       'class': 'etc'})[
                                       1]):
                        naver_staff_info_text = \
                            soup.find('ul', {'class': 'search_list_1'}).findAll('li')[i].find('dl').findAll('dd', {
                                'class': 'etc'})[1].text.strip()
                        naver_director = re.sub('(\|출연 :[\w \가-힣, \d \,]+)', '', naver_staff_info_text).replace('감독',
                                                                                                                '').replace(
                            ':', '')
                    else:
                        naver_director = 'no_info'
                except:
                    naver_director = 'no_info'

                try:
                    naver_star = soup.find('ul', {'class': 'search_list_1'}).findAll('li')[i].find(class_='num').text
                except:
                    naver_star = 'no_info'

                try:
                    naver_image = soup.find('ul', {'class': 'search_list_1'}).findAll('li')[i].find('p', {'class':'result_thumb'}).find('a').find('img')['src']
                except:
                    naver_image = 'no_info'

                compare_keyword = naver_title.replace(' ', '') + naver_director.replace(' ', '')
                match_percent = SequenceMatcher(isjunk=None, a=search_keyword, b=compare_keyword, autojunk=True).ratio()

                dic = {'n_title': naver_title, 'n_director': naver_director,
                       'naver_url': 'http://movie.naver.com' + naver_url,
                       'compare_keyword': naver_title.replace(' ', '') + naver_director.replace(' ', ''),
                       'matcher': match_percent, 'star': naver_star, 'image' : naver_image}
                dic_df = pd.DataFrame({i: dic}).T
                naver_movie_nomi_list_df = naver_movie_nomi_list_df.append(dic_df)

        try:
            naver_movie_nomi_list_df = naver_movie_nomi_list_df.sort_values('matcher', ascending=0).reset_index(
                drop=True)

            self.recomm_naver_movie_title = naver_movie_nomi_list_df.iloc[0]['n_title']
            self.recomm_naver_movie_matcher = naver_movie_nomi_list_df.iloc[0]['matcher']
            self.recomm_naver_movie_url = naver_movie_nomi_list_df.iloc[0]['naver_url']
            self.recomm_naver_movie_rating = naver_movie_nomi_list_df.iloc[0]['star']
            self.recomm_naver_movie_image = naver_movie_nomi_list_df.iloc[0]['image']
            self.recomm_naver_movie_director = naver_movie_nomi_list_df.iloc[0]['n_director']

        except:
            self.recomm_naver_movie_title = ''
            self.recomm_naver_movie_matcher = ''
            self.recomm_naver_movie_url = ''
            self.recomm_naver_movie_rating = ''
            self.recomm_naver_movie_image = ''

        self.recomm_naver_movie_dict = {

            'md_naver_title': self.recomm_naver_movie_title,
            'md_naver_rating': self.recomm_naver_movie_rating,
            'md_naver_rating_url': self.recomm_naver_movie_url,
            'md_naver_rating_url_matching': self.recomm_naver_movie_matcher,
            'md_naver_image_url': self.recomm_naver_movie_image,
            'md_naver_director' : self.recomm_naver_movie_director

        }

        return self.recomm_naver_movie_dict


def mod_images(kobis_code_list):
    for i, idx in enumerate(kobis_code_list):
        try:
            print(str(idx))
            #img_file = f'./images/{str(idx)}.jpg' ### 경로 수정 필요
            img_file = '/Users/mycelebs/PycharmProjects/movieeeee/images/{}.jpg'.format(str(idx))  ### 경로 수정 필요
            admin_save_file = '/Users/mycelebs/PycharmProjects/movieeeee/images/admin/{}.jpg'.format(str(idx))
            color_analy_save_file = '/Users/mycelebs/PycharmProjects/movieeeee/images/color_analy/{}.jpg'.format(str(idx)) ### 경로 수정 필요
            img = Image.open(open(img_file, 'r+b'))
            img_admin = img.resize((int(640 * img.width / img.height), 640))
            img_w, img_h = img_admin.size
            background = Image.new('RGB', (640, 640), (255, 255, 255, 255))
            bg_w, bg_h = background.size
            offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))
            background.paste(img_admin, offset) 
            background.save(admin_save_file) 
            img_color = img.resize((int(640 * img.width / img.height), 640))
            img_color.save(color_analy_save_file) 
        except:
            print('error: no_image', idx, kobis_code_list[i])

###############
# a = list(total_df['md_kobis_movie_code'])
# a[1]
# img_file = '/Users/mycelebs/PycharmProjects/movieeeee/images/{}.jpg'.format(str(a[1]))
# admin_save_file = '/Users/mycelebs/PycharmProjects/movieeeee/images/admin/{}.jpg'.format(str(a[1]))
# color_analy_save_file = '/Users/mycelebs/PycharmProjects/movieeeee/images/color_analy/{}.jpg'.format(str(a[1])) ### 경로 수정 필요
# img = Image.open(open(img_file, 'r+b'))
# img_admin = img.resize((int(640 * img.width / img.height), 640))
# img_w, img_h = img_admin.size #447*640
# background = Image.new('RGB', (640, 640), (255, 255, 255, 255))
# bg_w, bg_h = background.size #640*640
# offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2)) #96,0

# background.paste(img_admin, offset) 

# background.save(admin_save_file)
# img_color = img.resize((int(640 * img.width / img.height), 640))
# img_color.save(color_analy_save_file)
# img_color.size
# ################

new_movie_list_this_month = kobis_movie_list_by_month('201811')

insert_list = ','.join(list(set(new_movie_list_this_month)))
conn = pymysql.connect(host='db.ds.mycelebs.com', database='kuk',
                       user='celebDev', passwd='epdlxjtkdldjstm!', charset='utf8')
curs = conn.cursor()
query = "INSERT INTO kuk.new_movie (kobis_movie_code_list, regist_date) VALUES ('{}', CURRENT_DATE())".format(insert_list)
curs.execute(query)
conn.commit()


people_df = pd.read_sql('SELECT * FROM movie_people_connection', con=conn)
new_movie_df = pd.read_sql('SELECT * FROM new_movie', con=conn)

movie_list = new_movie_df['kobis_movie_code_list'].values[-1].split(',')
# movie_list = kobis_movie_list_by_month('201801')  # 해당 월의 영화 리스트 가져오기 : def_zip_movie_data_crawl.py 파일 내에 있음
# movie_list = list(box_office.md_kobis_movie_code)
total_df = pd.DataFrame()
total_txt_df = pd.DataFrame()
total_cnt_df = pd.DataFrame()
#####
for i, kobis_movie_code in enumerate(movie_list):
    try:
        # kobis_movie_code = movie_list[0]
        info_work_start_time = time.time()
        movie_crawl = MovieMetaCrawl('c1476617d9c596b877e48bfd0af595db', kobis_movie_code, people_df)
        # movie_crawl.get_json_data_api()
        # movie_crawl.get_json_data_actor()
        # movie_crawl.get_json_data_staff()

        basic_data = movie_crawl.get_movie_info()
        people_data = movie_crawl.get_movie_info_people()
        celeb_data = movie_crawl.get_celeb_idx_matching()
        naver_data = movie_crawl.get_naver_movie_code()

        total_dict = {**basic_data, **people_data, **celeb_data, **naver_data}

        similar_name = get_similar_name(total_dict['md_name'])
        total_dict['cd_similar_name'] = similar_name
        # after pytho 3.5 ==> multiple dict merge

        df = pd.DataFrame({i: total_dict}).T
        total_df = total_df.append(df)
        time.sleep(0.2)

        save_file = "/Users/mycelebs/PycharmProjects/movieeeee/images/{}.jpg".format(basic_data['md_kobis_movie_code'])
        try:
            if 'no_img' not in basic_data['md_mainposter_url']:
                urllib.request.urlretrieve(basic_data['md_mainposter_url'], save_file)
            else:
                urllib.request.urlretrieve(naver_data['md_naver_image_url'].replace('?type=f67', '').replace('https','http'), save_file)
        except:
            print('error: ', i, 'kobis_img :',basic_data['md_mainposter_url'], '  / naver_img :', naver_data['md_naver_image_url'])

        print(kobis_movie_code, '데이터 수급')
    except:
        print(i, kobis_movie_code, 'error')

    # print(
    #     f' {kobis_movie_code} 작업 완료, 기본정보 작업시간 : {str(round(duration_time_for_basic_info,2))}초, ___ 댓글,리뷰 작업시간 : {str(round(duration_time_for_txt,2))}초')

today = time.strftime('%Y%m%d')
total_df = total_df[
    ['md_kobis_movie_code', 'md_name', 'cd_similar_name' ,'md_name_en', 'md_date', 'md_running_time', 'md_making_country', 'md_type',
     'md_grade', 'md_genre', 'md_sub_genre', 'md_publisher', 'md_importer', 'md_produce_company', 'md_synopsys',
     'md_director', 'md_director_en', 'md_kobis_director_code', 'md_main_actors', 'md_mainactor_en',
     'md_kobis_mainactor_code', 'md_main_character', 'md_sub_actors', 'md_subactor_en', 'md_kobis_subactor_code',
     'md_sub_character', 'md_mainposter_url', 'md_director_celeb_idx', 'md_mainactor_celeb_idx',
     'md_subactor_celeb_idx', 'md_naver_rating_url', 'md_naver_rating_url_matching', 'md_naver_rating',
     'md_naver_title', 'md_naver_image_url', 'md_naver_director']]

total_df.to_excel('/Users/mycelebs/PycharmProjects/movieeeee/docs/new_movie_{}.xlsx'.format(today), index = False)  ### 경로 수정 필요
#total_df = pd.read_excel('/Users/mycelebs/PycharmProjects/movieeeee/docs/new_movie_20181004.xlsx')
mod_images(list(total_df['md_kobis_movie_code']))
