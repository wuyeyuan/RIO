from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
import xarray as xr

meteo_file1 = "/Users/yuanyuan/Downloads/2022.6-11(5).nc"
meteo_file2 = "/Users/yuanyuan/Downloads/2021.6-11(5).nc"
meteo_file3 = "/Users/yuanyuan/Downloads/2020.6-11(5).nc"
meteo_file4 = "/Users/yuanyuan/Downloads/2019.6-11(5).nc"
meteo_file5 = "/Users/yuanyuan/Downloads/2018.6-11(5).nc"
fh1 = Dataset(meteo_file1, mode='r')
fh2 = Dataset(meteo_file2, mode='r')
fh3 = Dataset(meteo_file3, mode='r')
fh4 = Dataset(meteo_file4, mode='r')
fh5 = Dataset(meteo_file5, mode='r')

fh1 = Dataset(meteo_file1, mode='r')
# fh2 = Dataset(meteo_file2, mode='r')
# print(fh1)

# 获取每个变量的值
lons = fh1.variables['longitude'][:]
lats = fh1.variables['latitude'][:]
sic1 = fh1.variables['siconc'][:]
sic2 = fh2.variables['siconc'][:]
sic3 = fh3.variables['siconc'][:]
sic4 = fh4.variables['siconc'][:]
sic5 = fh5.variables['siconc'][:]

tim = fh1.variables['time'][:]
# print(sic.shape)
# print(sic)

asic1=np.nanmean(np.nanmean(sic1,axis=2),axis=1)
asic2=np.nanmean(np.nanmean(sic2,axis=2),axis=1)
asic3=np.nanmean(np.nanmean(sic3,axis=2),axis=1)
asic4=np.nanmean(np.nanmean(sic4,axis=2),axis=1)
asic5=np.nanmean(np.nanmean(sic5,axis=2),axis=1)
# print(asic2.shape)
# print(asic2)

import matplotlib.dates as mdate
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

y1 = asic1
y2 = asic2
y3 = asic3
y4 = asic4
y5 = asic5

x = [datetime.datetime(2022,6,1) + datetime.timedelta(days=i) for i in range(len(y1))]
ax = plt.gca()
ax.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d'))

plt.xlabel("day",fontsize=14) #画横坐标
plt.ylabel("SIC",fontsize=14) #画纵坐标
plt.axhline(y=0.4,color="r",linestyle=":")
plt.axhline(y=0.15,color="g",linestyle=":")

plt.plot(x,y1,"b",label='2022')
plt.plot(x,y2,"g",label='2021')
plt.plot(x,y3,"c",label='2020')
plt.plot(x,y4,"m",label='2019')
plt.plot(x,y5,"y",label='2018')
plt.gcf().autofmt_xdate()
ax.legend()
ax.set_title('Saoka MEAN SIC 2018-2022')
plt.show()

# print(asic2[asic2<0.15].size)#计算小于0.15的数字个数即天数
# print(asic2[asic2<0.4].size)