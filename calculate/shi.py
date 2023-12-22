import numpy as np
import json

with open('./can_shu.json','r',encoding='utf-8') as f:
    date=json.load(f,strict=False)
    print(type(date))
    print(date)