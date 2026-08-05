---
layout: post
title: "MOOSE PorousFlow: Governing Equations"
description: "Working notes on the governing equations of MOOSE's PorousFlow module: mass conservation, Darcy flow, diffusion-dispersion, and solid mechanics coupling."
toc:
  beginning: true
date: 2025-08-20
categories:
  - theory
tags:
  - MOOSE
  - poromechanics
---

# INL MOOSE, porous flow module

I adapt the equations and remove the heat flow term, for we don't need to
history match this one. (Why? 1. we don't have DTS data; 2. final goal: get the
geometry of the frac, perm, and k of the frac. Mechanics is taking control.)

## Governing equations

### Fluid flow (continuity equation)

$$
0=\frac{\partial M^\kappa}{\partial t} + M^\kappa \nabla \cdot \mathbf{v}_s + \nabla \cdot \mathbf{F}^\kappa
$$

- `dt` term: rate of change of fluid.
- `vs` term: movement of skeleton. If $\nabla\cdot\mathbf v_s$ is positive, the
  skeleton is expanding. It will **suck** water from other places.
- `fk` term: flow term — the fluid flow in *vs* the fluid flow out.

| Variable | Description | Unit |
| --- | --- | --- |
| $\mathbf M$ | Mass density | $\mathrm{kg/m^3}$ |
| $\mathbf v_s$ | Velocity of skeleton | $\mathrm{m/s}$ |
| $\mathbf F$ | Flux | $\mathrm{kg\cdot s^{-1}\cdot m^{-2}}$ |

### Mass density

The mass of species $\kappa$ per volume of rock is written as a sum over all
phases present in the system:

$$
M^\kappa = \phi \sum_\beta S_\beta\rho_\beta\chi_\beta^\kappa + (1-\phi) C^\kappa
$$

where:

$$
\sum_\beta S_\beta = 1, \qquad \sum_\kappa \chi_\beta^\kappa = 1 \;\; \forall \beta
$$

### Flux

Flux is the sum of the advective flux and the diffusive-and-dispersive flux:

$$
\mathbf F^\kappa = \sum_\beta \chi_\beta^\kappa \mathbf F_\beta^{\mathrm{advective}} +\mathbf F ^\kappa _{\mathrm{diffusion+dispersion}}
$$

The **advective** flux is controlled by **Darcy's law**:

$$
\mathbf F_{\beta}^{\mathrm{advective}} = \rho_\beta \mathbf v_\beta = -\rho_\beta\frac{kk_{r,\beta}}{\mu_\beta}(\nabla P_\beta -\rho_\beta \mathbf g)
$$

In this equation,

| Variable | Description | Unit |
| --- | --- | --- |
| $\mathbf v_\beta$ | Darcy velocity in phase $\beta$ | $\mathrm{m/s}$ |
| $k$ | absolute permeability (tensor) | $\mathrm{m^2}$ |
| $k_{r,\beta}$ | relative permeability | N/A |

$k_{r,\beta}$ is always a function of the saturation(s), but with
**Klinkenberg** effects it may also be a function of the gas pressure. Relative
permeability can also be hysteretic, so that it depends on the history of
saturation.

> In reality, relative permeability is actually a tensor (for example it's
> usually different in lateral and vertical directions) but is most often
> treated as a scalar, since it's hard to get parameters for the tensorial
> case. In the PorousFlow module it is treated as a scalar.

For **diffusion** and hydrodynamic **dispersion**, we have:

$$
\mathbf F_{\mathrm{diffusion+dispersion}}^\kappa =-\sum_\beta\rho_\beta \mathcal D_\beta^\kappa\nabla\chi_\beta^\kappa
$$

The hydrodynamic dispersion factor is defined as

$$
\mathcal D_\beta^\kappa = D_{\beta, T}^\kappa \mathcal I + \frac{D_{\beta, L}^\kappa - D_{\beta, T}^\kappa}{\mathbf v_\beta^2}\mathbf v_\beta \mathbf v_\beta
$$

where,

$$
D_{\beta, L}^\kappa = \phi\tau_0\tau_\beta d_\beta^\kappa + \alpha_{\beta,L} |\mathbf v|_\beta, \qquad
D_{\beta, T}^\kappa = \phi\tau_0\tau_\beta d_\beta^\kappa + \alpha_{\beta,T} |\mathbf v|_\beta
$$

In these equations,

| Variable | Description | Unit |
| --- | --- | --- |
| $d_\beta^\kappa$ | molecular diffusion coefficient for component $\kappa$ in phase $\beta$ | $\mathrm{m^2/s}$ |
| $\chi_\beta^\kappa$ | mass fraction of component $\kappa$ in phase $\beta$ | N/A |
| $\tau_0\tau_\beta$ | phase tortuosity | N/A |
| $\phi$ | porosity of the solid | N/A |
| $\alpha_{\beta, L}$ | longitudinal dispersivity of phase $\beta$ | $\mathrm{m}$ |
| $\alpha_{\beta, T}$ | transverse dispersivity of phase $\beta$ | $\mathrm{m}$ |

It is common to set the dispersion to zero by setting
$\alpha_{\beta, T}=\alpha_{\beta, L}=0$.

> In PorousFlow, tortuosity is defined as the ratio of the shortest path to the
> effective path.

### Solid mechanics

This term contributes to $M^\kappa \nabla \cdot \mathbf{v}_s$. Based on the
conservation of momentum:

$$
\rho_{mat} \frac{\partial v_s^j}{\partial t} = \nabla_i \sigma_{ij}^{tot} + \rho_{mat}b_j =\nabla_i\sigma_{ij}^{eff}-\alpha_B\nabla_j P_f+\rho_{mat}b_j
$$

And the constitutive law:

$$
\sigma_{ij}^{eff} = \sigma_{ij}^{tot}+\alpha_B\delta_{ij}P_f=E_{ijkl}(\epsilon_{kl}^{elastic}-\delta_{kl}\alpha_TT)
$$

The elastic tensor $E_{ijkl}$ has an inverse $C_{ijkl}$ called the
**compliance tensor**.

Equilibrium equation:

$$
\nabla \cdot (\sigma_{ij}^{eff} - \alpha_B\delta_{ij}P_f)=0
$$

# What's next

MOOSE's design philosophy does not explicitly use **PDEs**, but assembles the
physical processes from kernels. How these processes map to a complete MOOSE
kernel configuration is covered in my
[history matching notes](/theory/history-matching-linearity/).
