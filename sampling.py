# sampling necessary info and write it to html
# the sampling parameter is fine tuned
import numpy as np
import json
index_list = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560,
 580, 600, 620, 640, 660, 680, 700, 720,725,730,735,741,745,750,755, 760,770, 780, 800, 810,820,825,830,835, 841,850, 861, 880, 900, 920, 940, 960, 980]

a = np.loadtxt('gps_path_229274051_2018-12-24-07-21.txt', delimiter = ',')
b = []
for i in index_list:
    b.append([a[i,0],a[i,1], i])
c = json.dumps(b)    
open('tmp.txt','w').write(c)