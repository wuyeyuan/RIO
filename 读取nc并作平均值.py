import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# 读取nc文件
file_path = '/Users/yuanyuan/Downloads/4.nc'
nc_file = nc.Dataset(file_path)

# 获取海冰密集度、经纬度和时间维度数据
ice_conc = nc_file.variables['siconc'][:]
lat = nc_file.variables['latitude'][:]
lon = nc_file.variables['longitude'][:]
time = nc_file.variables['time'][:]
ice_thick = nc_file.variables['sithick'][:]
themper = nc_file.variables['thetao'][:]
# 计算海冰密集度平均值
ice_conc_mean = np.mean(ice_conc, axis=(1, 2))
ice_thick_mean = np.mean(ice_thick, axis=(1, 2))
themper_mean = np.mean(themper, axis=(2, 3))
themper_mean = np.squeeze(themper_mean, axis=1)

##合并输出为csv
# 使用column_stack将四个MaskedArray合并为一个二维数组
merged_array = np.column_stack((ice_conc_mean, ice_thick_mean, themper_mean))

# 将二维数组转换为Pandas DataFrame
df = pd.DataFrame(merged_array, columns=['iceconc', 'icethick', 'themper'])

# 指定保存路径，保存为CSV文件
path = '/Users/yuanyuan/Desktop/合并csv/csv/sic.csv'
df.to_csv(path, index=False)

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