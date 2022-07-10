---
layout: post
title: Research on DAS-Recorded data of Lake Hatti(update on 9th Jul)
categories: DAS, Geophysics
description: None.
keywords: Summer research
---

# Connect to RCP server

I have connected to Zhejiang University's cluster server before, so it's relatively easy to configure everything in Mines.
![](/images/blog/summer_research/RDP.png)

# Process the data

I decide to use MATLAB first. In common sense, MATLAB will perform better in I/O.

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

I faced some problems while reading the data. 

Before MATLAB 2022a it will return another error: 
```
Error using h5infoc
The filename specified was either not found on the MATLAB path or it contains unsupported characters.

Error in h5info (line 108)
    hinfo = h5infoc(filename,location, useUtf8);

Error in read_data (line 18)
info = h5info(filename);
```

So I'll try to use python now.

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