import json
from collections import OrderedDict

file_data = OrderedDict()

for i in range(1,4):
    for j in range(1,10):
        file_data["messages"] = [{"role":"system","content":"정확한 정보를 제공하는 도우미"},{"role":"user","content":f"{i}학년 {j}반의 학생수는 몇명인가"},{"role":"assistant","content":f"{i}학년 {j}반의 학생수는 명 입니다."}]
        with open('datasets.jsonl', 'a', encoding="utf-8") as make_file:
            json.dump(file_data, make_file, ensure_ascii=False)
            make_file.write('\n')


         