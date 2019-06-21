import requests
import pandas as pd

df = pd.read_csv('C:\My folder\DailyObjects\Daily-Marketing-report.v2.csv')

url = "https://stageapi.dailyobjects.com/subProductsFromSkus"

sku_dict = {}

dict = {}
for i in range(0, len(df)):
    if df.iloc[i][2] in sku_dict.keys():
        sku_dict[df.iloc[i][2]] += 1
    else:
        sku_dict[df.iloc[i][2]] = 1

key_list = list(sku_dict.keys())

list = []
str = ""

for i in range(0, len(key_list)):
    if len(list) < 100 and i < len(key_list):
        list.append(key_list[i])
        continue

    for item in list:
        str += "\"" + item + "\","
    str = str[:-1]

    payload = "{\"skus\": [" + str + "]}"

    headers = {'content-type': 'application/json'}
    querystring = {"start": "0", "count": "0"}
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    list = []
    str = ""
    data=response.json()

    for j in range(0, len(data['data'])):
        try:
            # print(data['data'][j]['designCode'])
            if(data['data'][j]['designCode']) != "":
                ct=(data['data'][j]['categories'][0]['slug'])
                bd = (data['data'][j]['brand']['slug'])
                md=(data['data'][j]['model']['slug'])
                dc = (data['data'][j]['designCode'])
                sku=  (data['data'][j]['sku'])
                if ct in dict.keys():
                    temp_brands = dict[ct]
                    if bd in temp_brands.keys():
                        temp_models = dict[ct][bd]
                        if md in temp_models.keys():
                            temp_design_codes = dict[ct][bd][md]
                            dict[ct][bd][md][dc] = sku_dict[sku]
                        else:
                            m = {}
                            m[dc]=sku_dict[sku]
                            dict[ct][bd][md]=m
                    else:
                        m = {}
                        b = {}
                        m[dc]=sku_dict[sku]
                        b[md] = m
                        dict[ct][bd] = b
                else:
                    m={}
                    b={}
                    c = {}
                    m[dc]=sku_dict[sku]
                    b[md]=m
                    c[bd]=b
                    dict[ct] = c
        except KeyError:
            continue

print(dict)