from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

#建立座標
loc = ms.Point(24.19352298812673, 120.66940049145083)
sv = ms.Point(37.39322970859948, -121.5466194773837)
dl = ms.Point(32.76843333395586, -96.79124028349442)

slist = ms.stations.nearby(loc,limit=4)

print("在指定座標附近的偵測點如下: ")
print(slist)
'''
slist內容:

ID: 觀測站的唯一編號（例如 72494）。
Name: 觀測站名稱（通常是機場或城市名，如 "San Jose / Reid-Hillview"）。
Country: 國家代碼（如 US）。
Region: 地區/州別代碼（如 CA）。
Distance: 最重要的欄位，顯示該觀測站距離你設定的 sv 點有多少公尺。
'''