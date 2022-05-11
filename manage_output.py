import json
temp_content = ''
with open("/home/nudt/xlk/CCF-searcher/dblp_crawler_output_3.json", "r") as f:
    temp_content = f.read()

point = 0
semi_point = 0
result =[]
pre_loc = 0
sum = 0
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
                result += eval(temp_content[pre_loc : i + 2])
                pre_loc = i + 2
                sum += 1
                print(sum)
            except Exception as e:
                print(e)
                with open("/home/nudt/xlk/CCF-searcher/result/dblp_crawler_output_{}.json".format(i), "w") as f:
                    f.write(temp_content[pre_loc - 10: i + 10])    
                pre_loc = i + 2
                exit()
                


with open("/home/nudt/xlk/CCF-searcher/dblp_crawler_output_final2.json", "w") as f:
    f.write(json.dumps(result))