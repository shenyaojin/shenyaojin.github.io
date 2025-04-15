---
share: "True"
layout: post
title: Pressure Diffusion in Fractured Media
date: 2025-04-13
categories:
  - theory
tags:
  - geomechanics
  - DAS
---
Here is the workflow how we can derive the strain / pressure ratio from LF-DAS and gauge data.   
# Poisson's ratio estimation  
  
## Summary  
LFDAS data -> strain   
Pressure gauge data -> pressure  
  
Then we can calculate the Poisson's ratio use these datasets.   
## Theory  
### LF-DAS data  -> Strain   
From Lindsey, 2020 we have:   
$$  
\varepsilon_{xx}=\frac{\lambda}{4\pi nL_G\zeta}\Delta\Phi  
$$  
OR time deriviative:  
$$  
\dot\varepsilon_{xx}=\frac{\lambda}{4\pi n L_G\zeta}\frac{\Delta\Phi}{\Delta t}  
$$  
Where the incident wavelength $\lambda$= 1550 nm, refractive index n = 1.4682, and gauge length $L_G$= 4.08 m, the scalar coefficient $\zeta$ = 0.79 accounts for stress-induced birefringence, which governs the optical phase shift in response to axial strain as measured by the LF-DAS.  
  
This equation can convert **degree change (raw data)** ($\Delta \Phi$) to **strain rate**. Then I calculate the value:   
1. Our raw data $\Delta \Phi$, frequency $f=1$ Hz, raw unit `rad/10430.4`  
2. The coefficient  
$$  
c=\frac{\lambda}{4\pi nL_G\zeta}=\frac{1550 nm}{4\times 3.14\times4.08m\times0.79}=\frac{1.55\times10^{-6}\ m}{40.483 m}=3.82\times10^{-8}  
$$  
## Pressure -> Strain  
Use **Hooke's Law** we can convert pressure to strain  
$$  
\varepsilon=\frac PE  
$$  
Where $P$ is the pressure measured, $E$ is the Young's Modulus for the material.   
  
Then we are able to measure the Poisson's ratio(apparent).  
## Use Cases  
In code [2025-04-14-Poisson-Ratio-Code](./2025-04-14-Poisson-Ratio-Code.md).  
  
## References  
Lindsey, Nathaniel J., Horst Rademacher, and Jonathan B. Ajo‐Franklin. 2020. “On the Broadband Instrument Response of Fiber‐Optic DAS Arrays.” _Journal of Geophysical Research. Solid Earth_ 125 (2): e2019JB018145.  
