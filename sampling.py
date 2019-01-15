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
    second = seconds - minite * 60
    return '%d 分 %d 秒' %(minute, second)

a = np.loadtxt('gps_path_229274051_2018-12-24-07-21.txt', delimiter = ',')
b = []
time_base = int(a[0,3])
for i in index_list:
    time_rep = time_representation(int(a[i,3]) - time_base)
    b.append((a[i,0],a[i,1], time_rep))
c = json.dumps(b)    
open('map_data.js','w').write('var map_data = ' + c)
