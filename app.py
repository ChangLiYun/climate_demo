from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

# Specify location and time range

"""
    ms.Point( lat , long )  緯度 , 經度
"""
#座標
POINT2 = ms.Point(50.1155, 8.6842, 113)  # Try with your location
POINT = ms.Point(26.050336646717362, 119.33699261643062)
#時間
START = date(2025, 1, 1)
END = date(2025, 12, 31)

# 先找可用的 偵測點
stations = ms.stations.nearby(POINT, limit=4)   # 給予 stations 座標 並尋找附近的偵測點 抓回前四台 進行資料的擷取
'''
limit =4 回傳距離你座標最近的前 4 個氣象站
'''
# 時間跟資料填入
ts = ms.daily(stations, START, END)    # 從這些機器取出指定時段內的 資料
print("-------------- Time Serie ------------")
print( ts )
print("-------------- Time Serie ------------")
df = ms.interpolate(ts, POINT).fetch()
# df --> sql server database 存放 ---> power bi
# df --> power bi 做分析 ( df to_csv  --> import power bi)

# 1. 匯出成 CSV
df.to_csv('./weather tc.csv', index=False)
print("----- 已匯出至 dallas_weather.csv -----")


#print(df)
# Plot line chart including average, minimum and maximum temperature
# df.plot(y=[ms.Parameter.TEMP, ms.Parameter.TMIN, ms.Parameter.TMAX])
# plt.show()