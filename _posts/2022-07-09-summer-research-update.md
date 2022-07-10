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
