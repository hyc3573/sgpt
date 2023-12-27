import os
import json
from collections import OrderedDict

file_data = OrderedDict()

prompt = ""
answer = ""
index = 1

f = open("datasets.txt", 'r', encoding='utf-8')

while True:
    line = f.readline()

    if not line: break

    splitline = line.split("/")

    if splitline != '\n' and index % 2 != 0:
        prompt = splitline[0].replace("\n","") 
        index += 1

    elif splitline != '\n' and index % 2 == 0:
        answer = splitline[0].replace("\n","") 
        file_data["messages"] = [{"role":"system","content":"정확한 정보를 제공하는 도우미"},{"role":"user","content":f"{prompt}"},{"role":"assistant","content":f"{answer}"}]
        with open('datasets.jsonl', 'a', encoding="utf-8") as make_file:
                json.dump(file_data, make_file, ensure_ascii=False)
                make_file.write('\n')
        index += 1

    print(splitline)
    print("oo")





    
f.close()


        # file_data["messages"] = [{"role":"system","content":"정확한 정보를 제공하는 도우미"},{"role":"user","content":f"{prompt}"},{"role":"assistant","content":f"{answer}"}]
        # with open('datasets.jsonl', 'a', encoding="utf-8") as make_file:
        #     json.dump(file_data, make_file, ensure_ascii=False)
        #     make_file.write('\n')

