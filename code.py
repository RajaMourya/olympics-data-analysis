# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
data=pd.read_csv(path)

data=data.rename(columns={ "Total" : "Total_Medals"})
data['Better_Event'] = np.where(data['Total_Summer']>data["Total_Winter"],"Summer","Winter")
data['Better_Event'] = np.where( data['Total_Summer']==data["Total_Winter"] , "both" , data['Better_Event'])
print(data['Better_Event'].value_counts())
x=data
better_event = data['Better_Event'].value_counts().idxmax()
data=data[:-1]
ind_list=set(data["Total_Medals"].nlargest(10).index.tolist()+data["Total_Winter"].nlargest(10).index.tolist()+data["Total_Summer"].nlargest(10).index.tolist())
top_countries = data.iloc[list(ind_list)][['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
def top_ten(df,col):
    country_list = df.iloc[df[col].nlargest(10).index.tolist()]
    return country_list["Country_Name"]
top_10_summer, top_10_winter, top_10 = top_ten(data,'Total_Summer'), top_ten(data,'Total_Winter'), top_ten(data,'Total_Medals')

summer_df, winter_df, top_df = data[data["Country_Name"].isin(top_10_summer)], data[data["Country_Name"].isin(top_10_winter)], data[data["Country_Name"].isin(top_10)]
common=['United States', 'Sweden', 'Germany', 'Soviet Union']
import matplotlib.pyplot as plt

plt.bar(summer_df["Country_Name"], summer_df["Total_Summer"])
plt.bar(winter_df["Country_Name"], winter_df["Total_Winter"])
plt.bar(top_df["Country_Name"], top_df["Total_Medals"])
plt.xticks(rotation=90)
plt.legend(labels=['Total_Summer','Total_winter',"Total_Medals"])

summer_df["Golden_Ratio"]= summer_df['Gold_Summer']/summer_df["Total_Summer"]
winter_df["Golden_Ratio"]= winter_df['Gold_Winter']/winter_df["Total_Winter"]
top_df["Golden_Ratio"]= top_df['Gold_Total']/top_df["Total_Medals"]

top_country_gold , top_max_ratio =  data.iloc[top_df["Golden_Ratio"].idxmax()]["Country_Name"], top_df["Golden_Ratio"].max()
winter_country_gold , winter_max_ratio =data.iloc[winter_df["Golden_Ratio"].idxmax()]["Country_Name"] , winter_df["Golden_Ratio"].max()
summer_country_gold , summer_max_ratio =data.iloc[summer_df["Golden_Ratio"].idxmax()]["Country_Name"], summer_df["Golden_Ratio"].max()


data_1=data
data_1["Total_Points"] = data_1["Gold_Total"]*3 + data_1["Silver_Total"]*2 + data_1["Bronze_Total"]
most_points , best_country = data_1["Total_Points"].max() , data_1.iloc[data_1["Total_Points"].idxmax()]["Country_Name"]

best = data[data["Country_Name"]==best_country][['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel("United States") ; plt.ylabel('Medals Tally')
data=x



