---
layout: post
title: Introduction to Match Field
categories: Geophysics
description: None.
keywords: Forward Modeling, numerical methods
mathjax: true
---

# Match field is for what?

It is a new method for microseism localization. 

Compared to plane wave beamforming, match field processing(MFP) neither need to assume the far-enough sources, nor need to assume that the media have constant velocity.

- microseism body waves: great deal of attention.
- microseism surface waves: experienced limited application.(?)

# Methods

## Beamforming

- the standard plane wave frequency wave number beamformer power spectrum is defined as: 

$$ P(\vec s, f) =\frac{\mathbf{a}^H(\vec s, f)\mathbf{R}(f)\mathbf{a}(\vec s, f)}{K}$$

the steering vector is a plane wave.

$$
a_n(\vec s,f)=exp(-2\pi if\vec sr_n)
$$

- If we need to calculate the near-source noise, a solution is to use travel time instead of slowness and sensor location. That is: 

$$
a_{qn}(t) = exp(-2\pi i f t_{qn})
$$

An example of beamforming: 

- the data vector: (3 components)

$$X_{3C}(t) = [X_Z(t), X_N(t), X_E(t)]^T$$

- cross-spectral density matrix(CSDM): 

$$R_{3C}(f)=X_{3C}(f)X_{3C}^H(f)$$

- Polarization covariance matrix: 

$$Y_{3C}(s.f) = e^H(s,f)R_{3C}(f)e(s,f)$$

> e is orthogonal steering matrix.

> 极化协方差矩阵(Y)也称为复埃尔米特矩阵，同极化散射矩阵一样，它也包含了雷达测量得到的全部目标极化信息。极化SAR 图像处理过程一般都是在极化协方差矩阵和极化相干矩阵的基础上进行，它是进行多极化SAR数据分析和处理的基础。

Relationship with power and eigenvalue/vector(decomposed from Y): 

$$P_{3C}=|\vec u_{3C}|^2\lambda_0$$

Here we get the components of the eigenvector and we could rotate it into the desired direction.

With this transform, we process the data again, but replace the original data with the rotated data.

