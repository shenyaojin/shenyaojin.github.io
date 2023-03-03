---
layout: post
title: \\[How to] Read NetCDF 4 Data with python
categories: [Programming Skills]
description: Describe the functions to read, generate and modify the NetCDF 4 data
keywords: Python, NetCDF4
---

# Prep

## Install Conda

On Archlinux, you could use AUR or use pamac(for Manjaro) to install conda. It offers you auto update and easy uninstall.

## Intall lib: netCDF4

netCDF4 is the lib specialized in nc file. gdal is also recommend to read netCDF files.

```shell
conda install -c conda-forge netcdf4
```

# Load a NetCDF Dataset

If there's a model in data folder: 

```python
import netCDF4 as nc
fn = 'data/mymodel.nc'
ds = nc.Dataset(fn)
```

Then ds is the var that stores the data. We could use `print` to get all the vars in ds's namespace. For example: 

```python
print(data_set)
```

Output: (it's a seismic velocity initial model)

```
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF4 data model, file format HDF5):
    Conventions: CF-1.3
    dimensions(sizes): nbound(2), Northing(3), Easting(162), Depth(25)
    variables(dimensions): int32 nbound(nbound), float64 Northing(Northing), float64 Northing_bnds(Northing, nbound), float64 Northing_Origin(), float64 Easting(Easting), float64 Easting_bnds(Easting, nbound), float64 Easting_Origin(), float64 Depth(Depth), float64 Depth_bnds(Depth, nbound), float64 Depth_Origin(), float64 Slowness(Depth, Easting, Northing)
    groups:
```

With `ds.__dict__` we could retrive metadata from nc dataset: 

```
{'Conventions': 'CF-1.3'} (What's this?)
```

# View data

## view dimensions: 

Use a loop to get the size of all available dimensions: 

```python
for dim in ds.dimensions.values():
    print(dim)
   
>>> output: 
    <class 'netCDF4._netCDF4.Dimension'>: name = 'nbound', size = 2
    <class 'netCDF4._netCDF4.Dimension'>: name = 'Northing', size = 3
    <class 'netCDF4._netCDF4.Dimension'>: name = 'Easting', size = 162
    <class 'netCDF4._netCDF4.Dimension'>: name = 'Depth', size = 25
```

## View metadata:

It's similar to dimensions, usint variables.values: 

```python
for var in ds.variables.values():
    print(var)
 
>>> output: 
<class 'netCDF4._netCDF4.Variable'>
int32 nbound(nbound)
    long_name: Boundary index variable
unlimited dimensions: 
current shape = (2,)
filling on, default _FillValue of -2147483647 used
<class 'netCDF4._netCDF4.Variable'>
float64 Northing(Northing)
    units: m
    long_name: Northing coordinate
    bounds: Northing_bnds
unlimited dimensions: 
current shape = (3,)
filling on, default _FillValue of 9.969209968386869e+36 used
<class 'netCDF4._netCDF4.Variable'>
float64 Northing_bnds(Northing, nbound)
    units: m
```

## View Values: 

How to make slices is the most important part of nc file reading. The format is like following: 

```Python
ds['Easting'][:]
```

That means I want to access all the data in "Easting" part. It will output: 

```
masked_array(data=[ 0.2,  0.4,  0.6,  0.8,  1. ,  1.2,  1.4,  1.6,  1.8,
                    2. ,  2.2,  2.4,  2.6,  2.8,  3. ,  3.2,  3.4,  3.6,
                    3.8,  4. ,  4.2,  4.4,  4.6,  4.8,  5. ,  5.2,  5.4,
                    5.6,  5.8,  6. ,  6.2,  6.4,  6.6,  6.8,  7. ,  7.2,
                    7.4,  7.6,  7.8,  8. ,  8.2,  8.4,  8.6,  8.8,  9. ,
                    9.2,  9.4,  9.6,  9.8, 10. , 10.2, 10.4, 10.6, 10.8,
                   11. , 11.2, 11.4, 11.6, 11.8, 12. , 12.2, 12.4, 12.6,
                   12.8, 13. , 13.2, 13.4, 13.6, 13.8, 14. , 14.2, 14.4,
                   14.6, 14.8, 15. , 15.2, 15.4, 15.6, 15.8, 16. , 16.2,
                   16.4, 16.6, 16.8, 17. , 17.2, 17.4, 17.6, 17.8, 18. ,
                   18.2, 18.4, 18.6, 18.8, 19. , 19.2, 19.4, 19.6, 19.8,
                   20. , 20.2, 20.4, 20.6, 20.8, 21. , 21.2, 21.4, 21.6,
                   21.8, 22. , 22.2, 22.4, 22.6, 22.8, 23. , 23.2, 23.4,
                   23.6, 23.8, 24. , 24.2, 24.4, 24.6, 24.8, 25. , 25.2,
                   25.4, 25.6, 25.8, 26. , 26.2, 26.4, 26.6, 26.8, 27. ,
                   27.2, 27.4, 27.6, 27.8, 28. , 28.2, 28.4, 28.6, 28.8,
                   29. , 29.2, 29.4, 29.6, 29.8, 30. , 30.2, 30.4, 30.6,
                   30.8, 31. , 31.2, 31.4, 31.6, 31.8, 32. , 32.2, 32.4],
             mask=False,
       fill_value=1e+20)
```

And here's an example to convert 4 -> 9 th data to ndarray: 

```python
np.array(ds['Easting'][5:10])
```

Output: (Pycharm, text mode)

```
0,1.2
1,1.4
2,1.6
3,1.8
4,2.0
```

# Conclusion

(Thanks Konrad Hafen) NetCDF files are commonly used for geographic time-series data. Initially, they can be a bit intimidating to work with because of the large amounts of data contained, and the different format from the csv and raster files that are most commonly used. NetCDF is a great way to document geographic data because of the built in documentation and metadata. This makes it easy for end users to understand exactly what the data represent with little ambiguity. NetCDF data are accessed as numpy arrays, which present many possibilities for analysis and incorporation to existing tools and workflows.



**Ref**: 

https://towardsdatascience.com/read-netcdf-data-with-python-901f7ff61648
