import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取nc文件
file_path = '/Users/yuanyuan/Desktop/1993-2000BS巴罗海峡SIC/资料/cmems_巴罗海峡93-20sicDAY.nc'
nc_file = nc.Dataset(file_path)

# 获取海冰密集度、经纬度和时间维度数据
ice_conc = nc_file.variables['siconc'][:]
lat = nc_file.variables['latitude'][:]
lon = nc_file.variables['longitude'][:]
time = nc_file.variables['time'][:]

# 计算海冰密集度平均值
ice_conc_mean = np.mean(ice_conc, axis=(1, 2))

# 将时间维度转换为可读时间格式
time_units = nc_file.variables['time'].units
time_calendar = nc_file.variables['time'].calendar
dates = nc.num2date(time, units=time_units, calendar=time_calendar)
# 将dates转换为datetime类型的数组
datetimes = mdates.date2num(dates)




# 画出海冰密集度平均值随时间变化的图像
fig, ax = plt.subplots()
ax.plot(datetimes, ice_conc_mean)
ax.set_xlabel('Time')
ax.set_ylabel('Mean Ice Concentration')
ax.set_title('Mean Ice Concentration vs. Time')

# 设置x轴为时间格式
date_format = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

plt.axhline(y=0.4,color="r",linestyle=":")
plt.axhline(y=0.15,color="g",linestyle=":")

plt.show()


# 关闭nc文件
#nc_file.close()