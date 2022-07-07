---
layout: post
title: Basic Problem in computational geophysics
categories: Geophysics
description: None.
keywords: Forward Modeling, numerical methods
mathjax: true
---

# Basic Problems - 1

## Forward Modeling & Backward Modeling

**Forward Modeling**： Source, Model parameters; mathematical model, observed data

**Backford Modeling**：Observed data, mathematical model, source, model parameters

- inversion is based on forward modeling. is it a simplest way to implement forward modeling???

## Green Function

$$Lu=0/-f(x,t)$$

L is 2-order diffferential oprator.

In **gravity/magnetic** method: $$L=\Delta=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}$$

**Electromagnetic**: $$L=\Delta+k^2$, $k=\omega^2\mu\epsilon/c^2+i4\pi\omega\mu r/c^2$$

**Seismic**: $$L=\Delta-\frac{1}{v^2}\frac{\partial^2}{\partial t^2}$$

### The physical meaning of Green function

1. source function & basic solution

2. if BC & Initial Condition exists, Green funtion is related to those conditions.

3. use Green function to solve any field simulated by a point source.

$$
u(x)=\iiint_\Omega G(x,x_0)f(x_0)d\Omega+\iint_{\partial \Omega}G(x,x_0)\frac{\partial u(x_0)}{\partial n}ds-\\\iint_{\partial\Omega}u(x_0)\frac{\partial G(x,x_0)}{\partial n}ds
$$

### How to use Green function to solve a specific problem?

(1) find a proper integration(a specific form) to represent as the solution of the problem.

(2) get the solution of G and $\frac{\partial G}{\partial n}$

(3) put G and $\frac{\partial G}{\partial n}$ into the integration. Then we'll get the solution.

## Numerical Differentiation

## Taylor expansion

it's simple: 

$$
f(x+h)=f(x)+f'(x)h+\frac{f''(x)}{2}h^2+...
$$

### Differential

**Forward Differential**: $$f'(x)\approx\frac{f(x+h)-f(x)}{h}+o(h)$$ 

**Backward Differential**: $$f'(x)\approx\frac{f(x)-f(x-h)}{h}+o(h)$$

**Central Differential**: $$f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}+o(h^2)$$

**Explicit**: $$u_{j+1}=u_j-f(u_j,t_j)\Delta t$$

**Implicit** & Crank-Nocolson form

## Numerical Integration

$$
I=\int_a^bf(x)dx\\
I\approx\sum_{i=0}^n\Delta xf(x_i)
$$

Midpoint formula:

$$
I\approx\int_{i=0}^{n-1}\Delta xf(\frac{x_i+x_{x+1}}2)
$$

Simpson Formula

$$
I\approx \sum_{i=0}^{n-1}\frac{\Delta x}{6}[f(x_i)+4f(\frac{x_i+x_{x+1}}2)+f(x_{i+1})]
$$

## Inversion of Matrix && Singular value

small sigular value will cause problems, we need to handle it !

$$
1/\lambda\to\frac{\lambda}{\lambda^2+\alpha}
$$

## Norm

1-Norm

**2-norm**(it's important)
