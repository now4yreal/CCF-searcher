
import json
import os
temp_content = ''
with open("./CCF-searcher/dblp_crawler_output_2022.json", "r") as f:
    temp_content = f.read()

point = 0
semi_point = 0
result =[]
pre_loc = 0
sum = 0
all_get_fullname = []
for i in range(len(temp_content)):
    if i == 0:
        pre_loc = i
    elif i == len(temp_content) - 2:
        result += eval(temp_content[pre_loc : i + 2])
        sum += 1
        print(sum)
        break
    elif temp_content[i] == '[' and temp_content[i + 1] == '[' and temp_content[i - 1] == ']':
        pre_loc = i
    elif temp_content[i] == ']' and temp_content[i + 1] == ']' and temp_content[i + 2] == '[':
            try:
                temp_result = eval(temp_content[pre_loc : i + 2])
                fullname = temp_result[0][6]
                if fullname not in all_get_fullname:
                    all_get_fullname.append(fullname)
                    result += temp_result
                pre_loc = i + 2
                sum += 1
                print(sum)
            except Exception as e:
                print(e)
                exit()
                with open("./CCF-searcher/result/dblp_crawler_output_{}.json".format(i), "w") as f:
                    f.write(temp_content[pre_loc - 10: i + 10])    
                pre_loc = i + 2
                exit()
                

def get_unique_ccf_fullname(path="CCF_rank_2019.json")->list:
    '''
    Get all CCF links
    '''

    with open(path, 'r') as f:
        lists = json.loads(f.read())

    return lists

search_list = get_unique_ccf_fullname()

'''
loss = []
for i in search_list:
    if i['full-name'] not in all_get_fullname:
        loss.append(i['url'])
print(loss)
'''

with open("./CCF-searcher/dblp_crawler_output_2022_final.json", "w") as f:
    f.write(json.dumps(result))