import requests
from datetime import datetime, timedelta, time
import pandas as pd

# mongoDB
from pymongo import MongoClient
client = MongoClient()
db = client.my_database  # database
col = db.designCode  # collection

df=pd.read_csv('C:\My folder\DailyObjects\Daily-Marketing-report.v2.csv')

url = "https://prodapi.dailyobjects.com/subProductsFromSkus"

# TODAY_DATE=datetime.now()
TODAY_DATE=datetime(2019,5,17)

# YESTERDAY_DATE=(datetime.now() - timedelta(1))
YESTERDAY_DATE=datetime(2019,5,16)
# YESTERDAY_MIDNIGHT=datetime.combine(YESTERDAY_DATE, time.min)
# TODAY_MIDNIGHT=datetime.combine(TODAY_DATE, time.min)
str=""
list=[]
all_data_list=[]


for i in range(0,len(df)-1):
    dt = datetime.strptime(df.iloc[i][5], '%Y-%m-%d %H:%M:%S')
    # if (YESTERDAY_MIDNIGHT <= dt < TODAY_MIDNIGHT):
    if dt>=TODAY_DATE:
        continue
    # and (df['Source'] == 'Mobile' or df['Source'] == 'android' or df['Source'] == 'website' or df[
        # df['Source'].str.contains("iphone") == True])
    if len(list)<100 and YESTERDAY_DATE<=dt<TODAY_DATE:
        list.append(df.iloc[i][2])
        continue
    if len(list) == 0:
        break
    for item in list:
        str+="\"" + item + "\","
    str=str[:-1]
    payload = "{\"skus\": [" + str + "]}"
    # print(payload)
    headers = {'content-type': 'application/json'}
    querystring = {"start": "0", "count": "0"}
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    # print(response.text)
    list = []
    str = ""
    data=response.json()
    # all_data_list=[]

    all_data_list.append(data)
    if dt<YESTERDAY_DATE:
        break

# print(len(all_data_list))
# print(all_data_list)

dict={}

for x in range(0, len(all_data_list)):
    for j in range(0, len(all_data_list[x]['data'])):
        try:
            # print(data['data'][j]['designCode'])
            if(all_data_list[x]['data'][j]['designCode']) != "":
                ct=(all_data_list[x]['data'][j]['categories'][0]['slug'])
                bd = (all_data_list[x]['data'][j]['brand']['slug'])
                md=(all_data_list[x]['data'][j]['model']['slug'])
                dc = (all_data_list[x]['data'][j]['designCode'])
                if ct in dict.keys():
                    temp_brands = dict[ct]
                    if bd in temp_brands.keys():
                        temp_models = dict[ct][bd]
                        if md in temp_models.keys():
                            temp_design_codes = dict[ct][bd][md]
                            if dc in temp_design_codes.keys():
                                dict[ct][bd][md][dc] += 1
                                # m[dc]+=1
                            else:
                                dict[ct][bd][md][dc] = 1
                                # m[dc]=1
                        else:
                            m = {}
                            m[dc]=1
                            dict[ct][bd][md]=m
                    else:
                        m = {}
                        b = {}
                        m[dc]=1
                        b[md] = m
                        dict[ct][bd] = b
                        # c[bd]=b
                else:
                    m={}
                    b={}
                    c = {}
                    m[dc]=1
                    b[md]=m
                    c[bd]=b
                    dict[ct] = c
        except KeyError:
            continue

print(dict)

# print(Counter(DESIGN_CODE_LIST))

# d = dict(Counter(DESIGN_CODE_LIST))
# d['_id']= TODAY_DATE.strftime("%d") + '-' + TODAY_DATE.strftime("%m") + '-' + TODAY_DATE.strftime("%Y")
# print(d)
# result_id=db.col.insert_one(d).inserted_id
# print(result_id)