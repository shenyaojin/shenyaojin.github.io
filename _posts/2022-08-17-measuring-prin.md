---
layout: post
title: DTS Measuring Principles
categories: DTS
description: DTS system
keywords: DTS, geophysics
mathjax: true
---

# Introduction
DTS(**D**istributed **T**emperature **S**ensing) focuses on Raman backscatters, compared to DAS, which focused on Rayleigh backscatters. 

# Raman scattering

![/images/blog/DTS/ramanscattering.png]()

- Raman scattering <-> Molecular vibration <-> Temperature
- Note that the T must be in Kelvin.

$$
I_{as}(T) = \frac{K_{as}}{\lambda_{as}^4}\cdot\frac{1}{exp(\frac{h\cdot v_R\cdot c}{k_B\cdot T})-1}
$$

It could be simplified to the following formula: 

$$
R(T) = (\frac{K_{as}}{K_s})(\frac{\lambda_s}{\lambda_{as}})^4exp(-\frac{S_{LE}}{T})
$$

It's obvious that the low temperature is less sensitive than high temperature from the formula.

![/images/blog/DTS/acq.png]()