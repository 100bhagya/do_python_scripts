import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('C:\My folder\DailyObjects\Daily-Marketing-report.v2.csv')

cat = input('Enter Category : ')

if cat == "":
    category_list = df['Category']
    cat_count = Counter(category_list)
    df1 = pd.DataFrame.from_dict(cat_count, orient='index')
    df1.plot.pie(subplots=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
else:
    brand_list = []
    for i in range(0,len(df)-1):
        if df.iloc[i][7] == cat:
            brand_list.append(df.iloc[i][8])
    brand_count=Counter(brand_list)
    df1 = pd.DataFrame.from_dict(brand_count, orient='index')
    df1.plot.pie(subplots=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

brand = input('Enter brand : ')

if brand == "":
    brand_list = df['Brand']
    brand_count = Counter(brand_list)
    df2 = pd.DataFrame.from_dict(brand_count, orient='index')
    df2.plot.pie(subplots=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

else:
    model_list = []
    for i in range(0, len(df) - 1):
        if df.iloc[i][8] == brand:
            model_list.append(df.iloc[i][9])
    model_count = Counter(model_list)
    df2 = pd.DataFrame.from_dict(model_count, orient='index')
    df2.plot.pie(subplots=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

model=input('Enter model : ')

if model == "":
    model_list = df['Model']
    model_count = Counter(model_list)
    df3 = pd.DataFrame.from_dict(model_count, orient='index')
    df3.plot.pie(subplots=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
else:
    build_list = []
    for i in range(0, len(df) - 1):
        if df.iloc[i][9] == model:
            build_list.append(df.iloc[i][16])
    build_count = Counter(build_list)
    df3 = pd.DataFrame.from_dict(build_count, orient='index')
    df3.plot.pie(subplots=True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
