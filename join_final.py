import json
with open("./dblp_crawler_output_2022_final.json", "r") as fi1:
    with open("./dblp_crawler_output_final.json", "r") as fi2:
        with open("./dblp_crawler_output_final_res.json", "w") as fout:
            content2 = fi2.read()
            content1 = fi1.read()
            fout.write(json.dumps(eval(content1)+eval(content2)))
