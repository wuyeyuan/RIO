from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

meteo_file1 = "/Users/yuanyuan/Downloads/cmems_2020.7-10(S2全).nc"
# meteo_file2 = "D:\\NWP2\\Lancaster22sic.nc"
fh1 = Dataset(meteo_file1, mode='r')
# fh2 = Dataset(meteo_file2, mode='r')
# print(fh1)

# 获取每个变量的值
lons = fh1.variables['longitude'][:]
lats = fh1.variables['latitude'][:]
sic = fh1.variables['siconc'][:]
# sit = fh2.variables['sithick'][:]
tim = fh1.variables['time'][:]
# print(sic.shape)
# print(sic)

asic1=np.nanmean(sic,axis=2)
asic2=np.nanmean(asic1,axis=1)
# print(asic2.shape)
# print(asic2)

import matplotlib.dates as mdate
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

y = asic2
x = [datetime.datetime(2020,7,1) + datetime.timedelta(days=i) for i in range(len(y))]
ax = plt.gca()
ax.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d'))

plt.xlabel("day",fontsize=14) #画横坐标
plt.ylabel("SIC",fontsize=14) #画纵坐标
plt.axhline(y=0.4,color="r",linestyle=":")
plt.axhline(y=0.15,color="g",linestyle=":")

plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()


print(asic2[asic2<0.15].size)#计算小于0.15的数字个数即天数
print(asic2[asic2<0.4].size)