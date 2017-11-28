# So here is some just amazing code. It is for making plots of various things from the 6dF survey
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


import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 2, figsize=(7,7))
axes[0, 0].scatter(z, mag_b, c=a_v, s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[0, 0].set_title("z vs mag_b")
axes[0, 0].set_xlabel("z")
axes[0, 0].set_ylabel("mag_b")
axes[1, 0].scatter(z, mag_r, c=a_v, s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[1, 0].set_title("z vs mag_r")
axes[1, 0].set_xlabel("z")
axes[1, 0].set_ylabel("mag_r")
axes[1, 1].scatter(mag_r, mag_b, c=a_v, s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[1, 1].set_title("mag_r vs mag_b")
axes[1, 1].set_xlabel("mag_r")
axes[1, 1].set_ylabel("mag_b")
axes[0, 1].scatter(z, mag_b - mag_r, c=a_v, s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[0, 1].set_title("z vs mag_b - mag_r")
axes[0, 1].set_xlabel("z")
axes[0, 1].set_ylabel("mag_b - mag_r")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(7,7))
mask = (z < 0.2) & (mag_b > 10)
axes[0, 0].scatter(z[mask], mag_b[mask], c=a_v[mask], s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[0, 0].set_title("z vs mag_b")
axes[0, 0].set_xlabel("z")
axes[0, 0].set_ylabel("mag_b")
axes[1, 0].scatter(z[mask], mag_r[mask], c=a_v[mask], s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[1, 0].set_title("z vs mag_r")
axes[1, 0].set_xlabel("z")
axes[1, 0].set_ylabel("mag_r")
axes[1, 1].scatter(mag_r[mask], mag_b[mask], c=a_v[mask], s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[1, 1].set_title("mag_r vs mag_b")
axes[1, 1].set_xlabel("mag_r")
axes[1, 1].set_ylabel("mag_b")
axes[0, 1].scatter(z[mask], mag_b[mask] - mag_r[mask], c=a_v[mask], s=3, edgecolor='none', cmap='jet', alpha=0.5)
axes[0, 1].set_title("z vs mag_b - mag_r")
axes[0, 1].set_xlabel("z")
axes[0, 1].set_ylabel("mag_b - mag_r")
plt.tight_layout()
plt.show()

ras = np.linspace(ra.min(), ra.max(), 20)
decs = np.linspace(dec.min(), dec.max(), 20)

