from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import xarray as xr

meteo_file1 = "D:\\NWP2\\22sic.nc"
meteo_file2 = "D:\\NWP2\\22sit.nc"
fh1 = Dataset(meteo_file1, mode='r')
fh2 = Dataset(meteo_file2, mode='r')

# 获取每个变量的值
lons = fh1.variables['longitude'][:]
lats = fh1.variables['latitude'][:]
sic = fh1.variables['siconc'][:]
sit = fh2.variables['sithick'][:]
tim = fh1.variables['time'][:]
# print(sic.shape)
# print(sic)


import numpy as np
array1 = sit
print(array1)

# 针对PC7船舶
array2 = np.where(array1<2,array1,-4)
array3 = np.where(array2<1.6,array2,-5)
array4 = np.where(array3<1.2,array3,-6)
array5 = np.where(array4<0.95,array4,-7)
array6 = np.where(array5<0.5,array5,-8)
array7 = np.where(array6<=0,array6,-9)
array8 = np.where(array7!=0,array7,-10)

array9 = np.where(array8!=-4,array8,-3)
array10 = np.where(array9!=-5,array9,-2)
array11 = np.where(array10!=-6,array10,-1)
array12 = np.where(array11!=-7,array11,0)
array13 = np.where(array12!=-8,array12,1)
array14 = np.where(array13!=-9,array13,2)
array15 = np.where(array14!=-10,array14,3)

sic3 = 10*sic
rio1 = np.multiply(array15,sic3)
a = np.ones((365,9,121))#与sic、sit的形状一致
sc = 10*(a-sic)
rio2 = np.multiply(3,sc)
rio = rio1+rio2

ario1=np.nanmean(rio,axis=2)
ario2=np.nanmean(ario1,axis=1)
# print(ario2.shape)
# print(ario2)

# from datetime import datetime
# import matplotlib.pyplot as plt
import matplotlib.dates as mdate
# import pandas as pd


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
# create data
y = ario2
x = [datetime.datetime(2022,1,1) + datetime.timedelta(days=i) for i in range(len(y))]
ax = plt.gca()
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
# plt.xlim(1,366)
# plt.ylim(0,1)
plt.xlabel("day",fontsize=14) #画横坐标
plt.ylabel("RIO",fontsize=14) #画纵坐标
plt.axhline(y=0,color="r",linestyle=":")
plt.axhline(y=-10,color="g",linestyle=":")

plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()


# print(ario2[ario2>=0].size)#计算小于0.15的数字个数
# print(ario2[ario2>-10].size)




