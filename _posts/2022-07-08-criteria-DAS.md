---
layout: post
title: Four key criteria
categories: DAS
description: Some principles to measure the performance of DAS
keywords: DAS, geophysics
mathjax: true
---

# Four key criteria
- Measurement resolution
- Spatial resolution
- Measurement range
- Measurement time(AKA temporal resolution)

> They have *close* relationship. 

# Measurement Resolution

It means how small the physical quantity changes that the sensor can measure.

resolution $$\approx$$ sensitivity $$\ne$$ accuracy

# Measurement Range
It is usually determined by the length of fiber.

# Spatial resolution
![](/images/blog/DAS/SP_RE.png)

spatial resolution is $$\delta z$$ in this figure.

![](/images/blog/DAS/SP_RE2.png)
the hot-spot's relative size to the resolution.

- Solid line is actual measurement 
- Broken line is detected by the sensor.

# Measurement time 
DTS and DSS couldn't return accurate result with a single pulse.

The time taken by the system to acquire the readings for all points in the sensing fiber to required measured resolution.


# Short fiber vs Long fibre
A short fiber will enable the interrogator to inject more pulse. Thus it has higher measurement resolution if the measurement time is same. 

5km fiber & 1s measurement time =  10km fiber & 2s measurement time in measurement resolution theoretically.

## Interference in the fiber
> a longer fiber will gain more information than a shorter fiber while there exists lots of pluses.

# Spatial resolution and sampling resolution
- sampling resolution: determined by the acquisition system. 
- Actually in the first figure, the horizontal interval of "x" mark could be regarded as sampling resolution.

backscatter: 後向散射