---
layout: post
title: Research on DAS-Recorded data of Lake Hatti(update on 10th Jul)
categories: [DAS, Geophysics]
description: None.
keywords: Summer research
---

# Plot the data

I use matplotlib to plot the data.

![](/images/blog/summer_research/Plot_data_20220710.png)

The first image is the resampled the data. And the second image is strain data, using differential with the interval 50 points of the original data.

Note that the first image's data is normalized. Here's a version that is not normalized.

![](/images/blog/summer_research/Plot_data_20220710_1.png)

## Appendix: codes here

It is also saved in the working folder. 

```python
import matplotlib.pyplot as plt
import numpy as np

# this script is created by SY Jin, 9th Jul, 2022
# to get the plot of 10s DAS data.

file_name = "DFOS_Class_deformation_UTC-YMD20210527-HMS192431.605_seq_00000000000.hdf5"
new_name = file_name.strip(".hdf5")
output_re_sampling_txt_filename = new_name + "_resampling.txt"
output_strain_txt_filename = new_name + "_strain.txt"

data = np.loadtxt(output_re_sampling_txt_filename)
data_strain = np.loadtxt(output_strain_txt_filename)

# normalization
# data = (data - np.min(data))/(np.max(data)-np.min(data))
# data_strain = (data_strain - np.min(data_strain))/(np.max(data_strain) - np.min(data_strain))

plt.subplot(2, 1, 1)
plt.contourf(data)
plt.xlabel("channel")
plt.ylabel("point")
plt.colorbar()
plt.title("Result of the amplitude")

plt.subplot(2, 1, 2)
plt.contourf(data_strain)
plt.xlabel("channel")
plt.ylabel("point")
plt.colorbar()
plt.title("result of strain")
plt.show()
```