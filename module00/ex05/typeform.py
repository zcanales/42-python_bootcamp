import numpy as np
import pandas as pd
import sys
import mathtuple1 = tuple((3, 30, 2019, 9, 25))
print("%02d/%02d/%04d %02d:%02d" %(tuple1[3], tuple1[4], tuple1[2], tuple1[0], tuple1[1]))

tuple2 = tuple((0, 4, 132.422222, 100000, 12345.67))
print("day_%002d, ex_%02d : %.2f, %.2e, %.2e" %(tuple2[0], tuple2[1], tuple2[2], tuple2[3], tuple2[4] ))

t = (0, 4, 132.42222, 10000, 12345.67)
day = t[0] if t[0] >= 10 else "0" + str(t[0])
ex = t[1] if t[1] >= 10 else "0" + str(t[1])

message = f"day_{t[0]:02d}, ex_{t[1]:02d} : {t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}"
print(message)

