import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# 读取nc文件
nc_file = nc.Dataset('/Users/yuanyuan/Downloads/cmems_2022_7_D.nc')

# 获取变量数据
var_data = nc_file.variables['siconc'][:]

# 获取经度、纬度和时间维度数据
lon = nc_file.variables['longitude'][:]
lat = nc_file.variables['latitude'][:]
time = nc_file.variables['time'][:]

# 定义投影方式
proj = ccrs.NorthPolarStereo()

# 定义子图和画布
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection=proj))

# 绘制海冰数据
im = ax.pcolormesh(lon, lat, var_data[-1,:,:], transform=ccrs.PlateCarree(), cmap='coolwarm')

# 添加海岸线和网格线
ax.coastlines(resolution='50m')
gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
gl.xlabel_style = {'size': 12, 'color': 'gray'}
gl.ylabel_style = {'size': 12, 'color': 'gray'}

# 添加标题和颜色条
ax.set_title('Sea Ice Concentration')
cbar = plt.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Concentration', fontsize=12)

# 显示图像
plt.show()
