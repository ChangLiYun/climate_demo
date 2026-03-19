from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

POINT = ms.Point(24.160887904904108, 120.65667192896451)
START = date(2023, 1, 1)
END = date(2025, 12, 31)

stations = ms.stations.nearby(POINT, limit=4)   # 給予 stations 座標 並尋找附近的偵測點 抓回前四台 進行資料的擷取


ts = ms.daily(stations, START, END)    # 從這些機器取出指定時段內的 資料
df = ms.interpolate(ts, POINT).fetch()
df_reset = df.reset_index()
print(df_reset) # power bi 會去除 index 欄位( 關鍵欄位 日期)