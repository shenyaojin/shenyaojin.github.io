---
layout: post
title: DAS system(Phase) issues
categories: DAS
description: DAS syste,
keywords: DAS, geophysics
mathjax: true
---


# Noise
Including instrument noise and environmental noise. 

Instrument noise: 
- Fading Noise
- Laser Noise

## Fading noise
Still need some backscatter energy to make data reliable. 

Show the higher amplitude level in short distance. The amplitude change to a lower level because of interference of wave. 

We could use multiple laser frequencies to mitigate the noise level. sacrifice spatial resolution to significantly reduce the noise.

## Laser drifting noise 
If the instrument is unstable, there will be laser drifting noise. Independent to the channel. 

Could be easily removed using many signal processing method. 

# DAS Dynamic Range
we could only measure: $$\|\delta \phi\|<\phi$$; 

$$
\|\delta \varepsilon_{xx}\|<\frac{\lambda}{4nL_G\xi}
$$

Convert to strain rate: 

$$
\|\dot{\varepsilon}\|=\frac{\|\delta\varepsilon_{xx\|}}{dt}=\dots
$$

## Exceeding the dynamic range

It is different from geophone(maybe it will be similar in intensity-based system, but different in phase-based system)

![](/images/blog/DAS/EX3_4.png)

## Sample rate in DAS interrogators

Maximum pulse rate != output sampling rate. Down-sample is OK if we do not lose information.

# DAS Spatial Resolution

- Gauge length and pulse.
- Mainly by gauge length because gauge length setting is usually larger. 

GL should be much larger than pulse width or there will be some non-linear components in measurement.