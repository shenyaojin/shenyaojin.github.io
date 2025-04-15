---
share: "True"
layout: post
title: Poisson's ratio test python code
date: 2025-04-13
categories:
  - code
tags:
  - modeling
---
This code is designed for Poisson's ratio estimation using LF-DAS and gauge data.   
  
# Code Test – Poisson's ratio  
## Address  
`/rcp/rcp42/home/shenyaojin/Documents/bakken_mariner/scripts/well_leakage_history_matching/strain_pressure_coupling/101_ratio_estimation.py`  
  
It is a refractor of `midland` script:   
`E:\Projects\Mariner\student_folders\shenyao\dss_lfdas_data_analysis_0123\pythonProject\0731_poissonratio_estimation_v2.ipynb`  
  
## Purpose  
Get the Poisson ratio, convert DAS/pressure data to strain  
  
## Context  
Theory: [2025-04-14-Poisson-Ratio-Theory]({{ '/theory/Poisson-Ratio-Theory/' | relative_url }}) 

## Workflow  
1. Load DAS and gauge data.  
	- **DASdata** -> stage 1  
	- gauge -> gauge 1  
	- gauge md  
  
2. Pre-processing  
	- DAS data. -> crop time (Just want to remain the first pressure propagation wavefront)  
	- Gauge data  -> Interpolate to DAS data's time axis.  
```python  
#%% Do preprocessing  
start_time = datetime.datetime(xxxx, xx, xx, xx, xx, xx)  
end_time = datetime.datetime(xxxx, xx, xx, xx, xx, xx)  
print("Start Time: ", DASdata.start_time)  
DASdata.select_time(start_time, end_time)  
DASdata.select_depth(xx, xx)  
gauge_data.select_time(start_time, end_time)  
```  
2. After read-in the data:   
	- DAS data -> Use conversion to change it from $\Delta \Phi$ to $\dot \varepsilon$   
	- Gauge, calculate gradient
  
```python  
#%% Post-processing  
# 1. DAS data  
conversion_factor = 1.55e-6 / (4 * 3.14 * 4.09 * 0.79)  
unit_factor = 10430.4  
  
DASdata_strain = DASdata.copy()  
DASdata_strain.data = DASdata.data * conversion_factor / unit_factor  
  
# 2. Gauge data, convert to temporal pressure gradient  
gauge_data_temporal_grad = gauge_data.copy()  
gauge_data_temporal_grad = np.gradient(gauge_data.data, gauge_data.taxis)  
  
# 3. Single channel DAS data  
DASchan_strain = DASchan * conversion_factor / unit_factor  
```  

## Results  

- Co plot them. Result can be found on server: `/rcp/rcp42/home/shenyaojin/Documents/bakken_mariner/figs/04142025`  
- The ratio `strain rate / pressure temoporal grad`$\approx 5.6\times10^{-9} psi^{-1}$   
- Then in `Pa`, we have:   
$$  
ratio\ in\ Pa = 5.6\times10^{-9}\frac1{psi}\times \frac{1\ psi}{6894.76\ Pa}\approx 8.06\times 10^{-13}\ Pa^{-1}  
$$  
## Interpretation  

The only thing is Poisson's ratio is smaller than expected. A likely explanation is that the cement sheath is still mechanically coupled to the surrounding formation. In this case, when radial pressure increases and the cement attempts to expand laterally, the adjacent rock formation resists that deformation. This lateral confinement reduces the axial strain induced by the Poisson effect, leading to an underestimated strain-to-pressure ratio and, consequently, an unrealistically low inferred Poisson’s ratio.  
  
## Next Steps  

I'm figuring out why cross correlation does not work for this case.   
  
