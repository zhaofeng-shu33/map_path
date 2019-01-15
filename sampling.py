# -
# sampling necessary info and write it to html
# the sampling parameter is fine tuned
import numpy as np
import json
import math
index_list = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560,
 580, 600, 620, 640, 660, 680, 700, 720,725,730,735,741,745,750,755, 760,770, 780, 800, 810,820,825,830,835, 841,850, 861, 880, 900, 920, 940, 960, 980]
def time_representation(time_int):
    '''
        convert time_int (minisecond) to representation of x 分 y 秒
    '''
    seconds = time_int/1000
    minute = math.floor(seconds/60)
    second = seconds - minute * 60
    return '%d 分 %d 秒' %(minute, second)

from math import radians, cos, sin, asin, sqrt
 
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000

a = np.loadtxt('gps_path_229274051_2018-12-24-07-21.txt', delimiter = ',')
b = []
time_base = int(a[0,3])
for index, i in enumerate(index_list):
    time_rep = time_representation(int(a[i,3]) - time_base)
    dist = haversine(a[0,0],a[0,1], a[i,0], a[i,1])
    b.append((a[i,0],a[i,1], index, time_rep, '%.1f km'%(dist/1000)))
c = json.dumps(b)    
open('map_data.js','w').write('var map_data = ' + c)
