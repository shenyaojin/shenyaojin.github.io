---
layout: post
title: Inversion theory
categories: geophysics
description: Describe some basic method to run the inversion
keywords: inversion, least-square
mathjax: true
---

# Inversion methods

## Least-square linear inversion (最小二乘反演)

$$
d=Gm\\
d^{obs}=d+n
$$

So

$$
m=(G^*G)^{-1}G^*d^{obs}
$$

> Another rule is: Least norm criterion.

## Damping least squares criterion

function: 

$$
S(m) = \|d-Am\|_2+\alpha\|m\|_2
$$

then: 

$$
m=(A^TA+\alpha I)^{-1}A^Td
$$

## Tikhonov Regularization Method
for a bounded linear operator K: X->Y, and y $\in$ Y, need to get the solution of $x^\alpha\in X$, letting it have minimum **Tikhonov** funtion in $x\in X$

$$
J_\alpha(x)=\|Kx-y\|_Y^2+\alpha\|\phi(x)\|_X^2
$$

we often define $\alpha$ as regularization parameter.

## Maximum likelihood & maximum posterior

## Landweber Method
$$
D=Gm\\
m^0=0
m^{k+1}=m^k+\alpha^kG^*(d-Gm^k)
$$

