import pandas as pd
from tqdm import tqdm

df = pd.DataFrame()
df = pd.read_excel('/Users/mycelebs/Desktop/matzip_rank.xlsx')

df2 = pd.DataFrame()
df2 = pd.read_excel('/Users/mycelebs/Desktop/matzip_cdidx_name.xlsx')

df2.columns

total_columns = len(df['vf_names'])
df['vf_names'][0].split(',')[:3]

total_filter=[]
for i in tqdm(range(total_columns)):
	res = df['vf_names'][i].split(',')[:3]
	total_filter.append(res)

cd_idx = pd.DataFrame(df['cd_idx'])
len(total_filter)
ss = pd.DataFrame({'ranking':total_filter})
res = pd.concat([cd_idx,ss], axis=1)
res.to_excel('rank_update.xlsx', index=False)

result = pd.merge(df2,res,on='cd_idx')
result.to_excel('total_ranking.xlsx', index=False)
