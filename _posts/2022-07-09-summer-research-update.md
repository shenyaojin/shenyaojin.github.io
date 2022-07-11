---
layout: post
title: Research on DAS-Recorded data of Lake Hatti(update on 9th Jul)
categories: DAS Geophysics
description: None.
keywords: Summer research
mathjax: true
---

# Connect to RCP server

I have connected to Zhejiang University's cluster server before, so it's relatively easy to configure everything in Mines.
![](/images/blog/summer_research/RDP.png)

# Process the data

I decide to use MATLAB first. In common sense, MATLAB will perform a bit better than python while reading the data. However, I faced some problems while reading the data. 

## MATLAB's version

```MATLAB
Error using h5infoc
Unable to open the file because of HDF5 Library error. Reason:

    H5Fget_obj_count    not a file id

Error in h5info (line 125)
    hinfo = h5infoc(filename,location, useUtf8);

Error in read_data (line 13)
info = h5info(file_name);
```

If the version is older than MATLAB 2022a it will return another error: 
```
Error using h5infoc
The filename specified was either not found on the MATLAB path or it contains unsupported characters.

Error in h5info (line 108)
    hinfo = h5infoc(filename,location, useUtf8);

Error in read_data (line 18)
info = h5info(filename);
```

That's so weird. So I'll try to use python now.

## Python's version
I will use h5py to read the data.

### Use anaconda to install the package
```bash
conda activate base
conda install h5py
```

### Read the data
Data: 
> DFOS_Class_deformation_UTC-YMD20210527-HMS192431.605_seq_00000000000

### Output the resampling data
I resampled this data. Then there are about 22000 points each channel.

The output file size is around 120 Mb(in txt form).


### Output the strain data
use "diff" to get the strain data. Here is a small question: I'm not quite sure that I need to do the differential before resampling (interval is 1 point, that means $$\Delta = a_{t+1} - a_{t}$$ ) or after resampling(Interval is about 50 points, $$\Delta = a_{t+50} - a_{t}$$).

Anyway, I chose the latter method to do the differential because I believe it'll be more reasonable.

### Appendix: code here.
It is also saved in the working folder. 

```python
import h5py as h5
import numpy as np
import os
# This script is created by SY Jin on 9th Jul, 2022
# Tested on Linux(ubuntu 22.04 LTS).
# To read a DAS-record data file in python. (2G around)

# define the file name
file_name = "DFOS_Class_deformation_UTC-YMD20210527-HMS192431.605_seq_00000000000.hdf5"
new_name = file_name.strip(".hdf5")

# clear the flag of file.
os.system("h5clear -s %s" % file_name)

# Read the file into variation f
dataset = h5.File(file_name, 'r')
# reveal the dimension of the data.
dimension_data = list(dataset.keys())

deformation = dataset['deformation']
# print(dataset["/deformation/data"][0])
# <- this will output one channel(416 data)
# data:
# channel   1 2 3 ... 416
# time:
#       1
#       2
#       ...
#       1095520
# output to a txt file.
# file_name

output_re_sampling_txt_filename = new_name + "_resampling.txt"
output_strain_txt_filename = new_name + "_strain.txt"
# output the re-sampling file
data = dataset["/deformation/data"]
shape_data = np.shape(data) # time, channel
f_resampling = open(output_re_sampling_txt_filename, 'w')
f_strain = open(output_strain_txt_filename, 'w')
interval = 50

for i in range(int(shape_data[0]/interval)-1):
    temp_resampling = (data[interval*i])  # interval == 50
    temp_strain = (np.abs(data[i+interval] - data[i]))
    # write into file
    for j in range(shape_data[1]): # number of channel
        f_resampling.write(str(temp_resampling[j]))
        f_resampling.write(" ")
        f_strain.write(str(temp_strain[j]))
        f_strain.write(" ")
    f_resampling.write("\n")
    f_strain.write("\n")

f_resampling.close()
f_strain.close()


```