# So here is some just amazing code. It is for making plots of various things from the 6dF survey
# and calculating overdensity at particular coords
# If you have time in the exercise, try to get this fixed up, efficient, tested and documented
import numpy as np

f = open(r"C:\Users\shint1\PyCharmProjects\WorkshopExample\data\6df.csv", 'r')
c = 0
ra, dec, z, quality, a_v, mag_b, mag_r = [], [], [], [], [], [], []
for line in f:
    if c == 0:
        pass
    else:
        s = line.split(",")
        if int(s[3]) not in [2,3,4] or float(s[2]) < 0 or float(s[6]) < 5 or float(s[7]) < 5:
            continue
        ra.append(float(s[0]))
        dec.append(float(s[1]))
        z.append(float(s[2]))
        quality.append(int(s[3]))
        a_v.append(float(s[5]))
        mag_b.append(float(s[6]))
        mag_r.append(float(s[7]))
    c += 1
ra = np.array(ra)
dec = np.array(dec)
z = np.array(z)
quality = np.array(quality)
a_v = np.array(a_v)
mag_b = np.array(mag_b)
mag_r = np.array(mag_r)
print("Have %d entries" % len(ra))

radius = 1
ra_sn = [50, 75, 175, 200, 205, 300]
dec_sn = [-40, -60, -10, -30, -5, -70]
nums = []
for i in range(len(ra_sn)):
    r, d = ra_sn[i], dec_sn[i]
    dist = np.sqrt((ra - r)**2 + (dec - d)**2)
    num = np.sum(dist < radius)
    nums.append(num)
rands = np.vstack((ra, dec)).T
np.random.shuffle(rands)
rands = rands[:500, :]
print(rands.shape)
vals = []
for r, d in rands:
    dist = np.sqrt((ra - r)**2 + (dec - d)**2)
    vals.append(np.sum(dist < radius))
mean = np.mean(vals)
overdensity = (np.array(nums) / mean) - 1
print("Overdensities:")
print("%12s %12s %12s" % ("RA", "DEC", "delta"))
for i in range(len(ra_sn)):
    print("%12.4f %12.4f %12.4f" % (ra_sn[i], dec_sn[i], overdensity[i]))

