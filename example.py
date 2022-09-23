import json
import pandas as pd

paper_lists = json.loads(open('./CCF-searcher/dblp_crawler_output_final.json', 'r').read())
df = pd.DataFrame(paper_lists, columns=["year", "title", "doi", "authors", "ccf_rank", "abbreviation", "ccf_name", "full_name", "publisher"])\
    .sort_values(['ccf_rank', 'year'], ascending=[True, False])


# ------------- Paper Quality -------------
#df2 = df[(df['year'] >= 2000) | (df["year"] == -1)]
#df2 = df2[(df2['ccf_rank'].str.contains('CCF-A|CCF-B', case=False))]
# ------------- Field         -------------
#df2 = df[(df['abbreviation'].str.contains('Usenix Security|^CCS|S&P|NDSS', case=False))]
df2 = df[(df['ccf_rank'].str.contains('CCF-A|CCF-B', case=False))]
df2 = df2[(df2['title'].str.contains("static", case=False))]
df2 = df2[(df2['title'].str.contains("analy", case=False))]
df2 = df2[(df2['title'].str.contains("detect", case=False))]

#df2 = df2[(~df2['title'].str.contains('fuzzy', case=False))]
# ------------- Direction     -------------
# ------------- Conference / Journal   -------------
#df2 = df2[(df2['ccf_name'].str.contains('Usenix Security Symposium', case=False))]



df2 = df2.sort_values(['ccf_rank', 'year', 'abbreviation'], ascending=[True, False, False])
df3 = df2[["ccf_rank", "ccf_name", "year", "title", "authors"]].copy() # Show
df3.authors = df3['authors'].str[:32]
print(df3)
print('Count: ', len(df3))

target_df = df2.drop(index=[])
["year", "title", "doi", "authors", "ccf_rank", "abbreviation", "ccf_name", "full_name", "publisher"]
output  = '| CCF-rank | Activity Theme | Year | Title |\n'
output += '|---|---|---|---|\n'
'''
output_temp = []
for i in range(len(target_df)):
    output_temp.append('| %s | %s | %s | %s | [%s](%s) |\n' % (
        target_df.iloc[i]['ccf_rank'], 
        target_df.iloc[i]['abbreviation'], 
        target_df.iloc[i]['ccf_name'], 
        target_df.iloc[i]['year'], 
        target_df.iloc[i]['title'],
        target_df.iloc[i]['doi']
    ))
result = []
for i in output_temp:
    if i not in result:
        result.append(i)
        output += i
open('./CCF-searcher/result/sandbox_and_detect.md', 'w').write(output)
'''

for i in range(len(target_df)):
    output += '| %s | %s | %s | %s | [%s](%s) |\n' % (
        target_df.iloc[i]['ccf_rank'], 
        target_df.iloc[i]['abbreviation'], 
        target_df.iloc[i]['ccf_name'], 
        target_df.iloc[i]['year'], 
        target_df.iloc[i]['title'],
        target_df.iloc[i]['doi']
    )

open('./CCF-searcher/result/static_analy_detect_AB.md', 'w').write(output)