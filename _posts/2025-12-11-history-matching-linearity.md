---
layout: post
title: "History Matching with DSS: Is Diffusion Linearly Additive?"
description: "Whether pressure diffusion solutions can be superposed in MOOSE: a proof for the one-way coupled case, and why it breaks for the fully coupled hydro-mechanical model."
toc:
  beginning: true
date: 2025-12-11
categories:
  - theory
tags:
  - MOOSE
  - geomechanics
  - inversion
---

# The linearity of diffusion

I learned how diffusion works in MOOSE and how the variables are coupled in the
MOOSE framework. I then know whether they are linearly addable or not.

## The classical diffusion (one-way coupled)

The governing equation for the pressure diffusion is:

$$
\frac{\partial p}{\partial t} = \frac{k}{\mu\phi c_t}\nabla p
$$

where $D = \frac{k}{\mu\phi c_t}$ is the hydraulic diffusivity.

After we solve the pressure equation, we need to solve a simplified version of
the linear momentum conservation equation by treating the pressure gradient as
a body force. The governing equation would be:

$$
\nabla \cdot \sigma + F =0
$$

Also, using Hooke's law with effective stress, we have the total stress tensor:

$$
\sigma=C:\varepsilon -\alpha p \mathbf I
$$

where,

- $\mathbf{u}$ is the displacement vector (strain
  $\boldsymbol{\epsilon} = \frac{1}{2}(\nabla \mathbf{u} + (\nabla \mathbf{u})^T)$).
- $\mathbf{C}$ is the stiffness tensor (containing Young's modulus $E$ and
  Poisson's ratio $\nu$).
- $\alpha$ is the Biot-Willis coefficient (coupling strength).
- $\mathbf{F}$ represents body forces (like gravity).

Then we have:

$$
\nabla \cdot (\mathbf{C} : \nabla \mathbf{u}) = \alpha \nabla p - \mathbf{F}
$$

We can see the strain is in explicit form in the momentum conservation
equation.

## Fully coupled hydro-mechanical model

Eq A:

$$
\nabla \cdot \left( \mathbf{C} : \boldsymbol{\epsilon} - \alpha p \mathbf{I} \right) + \mathbf{F} = 0
$$

Same as one-way coupled. Still contains 2 variables.

Eq B:

$$
\frac{1}{M} \frac{\partial p}{\partial t} + \alpha \frac{\partial \epsilon_{vol}}{\partial t} + \nabla \cdot \left( - \frac{k}{\mu} \nabla p \right) = Q
$$

- $\epsilon_{vol} = \text{trace}(\boldsymbol{\epsilon}) = \epsilon_{xx} + \epsilon_{yy} + \epsilon_{zz}$
  is the volumetric strain.
- $M$ is the Biot modulus.
- The coupling term $\alpha \frac{\partial \epsilon_{vol}}{\partial t}$ is the
  squeezing effect. If the rock compresses rapidly, it squeezes fluid out,
  temporarily increasing pore pressure.

Currently the hydro-mechanical model (HMM) is what I'm using in MOOSE.

## Linear additivity of the two types of equation

### Classical diffusion

Yes, I believe it is linearly addable. Here's the proof:

Since the strain is not time dependent (it is explicitly calculated from the
pressure field), we only need to prove the linear additivity of classical
pressure diffusion.

So we mark the pressure diffusion as:

$$
\frac{\partial p}{\partial t} -\frac{k}{\mu\phi c_t}\nabla p =0
$$

We have three sets of solutions of the diffusion equation:

- $p_1(x,t_1)$ is the solution at $t_1$ (waveform at $t_1$)
- $p_2(x,t_2)$ is the solution at $t_2$ (waveform at $t_2$)
- $p_3(x) = p_1(x,t_1)+p_2(x,t_2)$

Since $p_1$, $p_2$ are solutions, we have:

$$
\frac{k}{\mu\phi c_t}\nabla p_1(x,t_1) =0
$$

and,

$$
\frac{k}{\mu\phi c_t}\nabla p_2(x,t_2) =0
$$

Simply adding them, we have:

$$
\frac{k}{\mu\phi c_t}\nabla (p_1(x, t_1)+ p_2(x,t_2)) =0
$$

That means $p_3(x)$ is also a solution of the PDE.

### HMM/THM

However, this does not hold for the fully coupled hydro-mechanical model.

# The pressure curve — do I need to normalize?

My current answer is **NO**. The pressure will be coupled with the strain field
(even one-way), so a normalized pressure will still make the strain
inaccurate.

# Next step

- I'll use a numerical method to verify the conclusion above.
- Also, I need to adjust the kernel settings in MOOSE. Currently, these are
  the kernels (HMM) I'm using:

![HMM kernels currently used in MOOSE](/public/images/history-matching-how/hmm-kernels.png)

Here,

1. `dp/dt` will be kept in classical diffusion.
2. Darcy flow: keep.
3. Others: remove. They couple pressure and strain.

I need to add kernels in Python:

1. `StressDivergenceTensors`: $\nabla \cdot \sigma =0$
2. In the material block, after defining the material in fracture & SRV, we
   need to define how to calculate strain from the pressure field. Still
   working on this; it seems I need `ComputeIsotropicElasticityTensor`,
   `ComputeSmallStrain`, and `ComputeLinearElasticPoroelasticStress`.
