---
layout: post
title: "Cement Shrinkage and Microannulus Formation in Horizontal Wells"
description: "Why cement shrinkage matters for zonal isolation: mechanisms, typical sheath dimensions in Bakken 5.5-inch casing, and how shrinkage-induced microannuli show up in LF-DAS data."
toc:
  beginning: true
date: 2025-05-07
categories:
  - geophysics
tags:
  - cement
  - LFDAS
  - well-integrity
---

I introduce the cement shrinkage effect in O&G well development.

# Cement Shrinkage

## Definition of cement shrinkage

Changes of pore water content due to drying or wetting processes cause
**significant volume changes** of concrete in load-free specimens. They are
called shrinkage (typically causing strains between 0.0002 and 0.0005, and in
low strength concretes even 0.0012) or swelling (< 0.00005 in normal
concretes, < 0.00020 in high strength concretes).

This was first reported by Le Chatelier (that guy also found the
[principle of Le Chatelier](https://en.wikipedia.org/wiki/Le_Chatelier%27s_principle)).

## When will it happen?

It will actually happen all the time. The shrinkage of cement paste during
hardening is caused by **chemical reactions** of the clinker minerals with
water during the first hours. At a later stage it is caused by changes in the
**water content** of the hardened paste.

## The relationship with my project

In the context of wellbore cementing, **cement shrinkage** can critically
impact the hydraulic isolation performance of the annular space between casing
and formation. As observed in our field study, low-frequency distributed
acoustic sensing (LF-DAS) captured heel-ward migrating strain signals and
pressure communication along the monitor well — signals consistent with the
presence of pressure pathways behind casing. These pathways are likely formed
due to **shrinkage-induced debonding** at the cement–formation interface,
which creates a low-diffusivity conduit for fluid migration.

Early-age chemical shrinkage during the hydration of clinker minerals can
cause micro-annuli formation, especially if curing conditions are suboptimal
or if the cement experiences differential drying. Over time, **drying
shrinkage** or **autogenous shrinkage** further degrades the bond integrity.
Such debonded zones can remain undetected by traditional cement bond logs but
manifest as strain anomalies in LF-DAS data due to radial stress and the
resulting axial strain via Poisson's effect.

In this study, we model these effects by introducing a spatially varying
hydraulic diffusivity field along the monitoring well. Regions with low cement
quality exhibit increased compressibility and lower diffusivity, consistent
with pressure trapping and asymmetric wavefront propagation observed in the
DAS and pressure gauge datasets. Therefore, understanding and quantifying
cement shrinkage provides a physical foundation for interpreting LF-DAS strain
signals and identifying compromised zonal isolation before stimulation.

## Cement sheath width after shrinkage in Bakken horizontal wells

### Typical cement sheath thickness in a 5.5″ casing annulus

In Bakken horizontal wells completed with 5.5-inch casing, the cement sheath
(annular cement "ring" between casing and formation) is on the order of a few
tenths of an inch thick. When the wellbore is drilled close to gauge (e.g. a
~6.5–6.75″ hole for 5.5″ casing), a concentric casing yields roughly
**0.4–0.6 inches** (about 10–15 mm) of radial cement thickness. This is
consistent with industry guidelines that require a minimum annular clearance
around casing (e.g. U.S. onshore regulations mandate ≥0.422″ of clearance on
each side of the casing collars). In practice, cement sheath thickness in
shale plays like the Bakken often falls in the ~8 mm to 15 mm range depending
on hole size and centralization. For example, laboratory simulations of shale
well cementing have used sheath thicknesses of ~8 mm (0.3″) in scaled-down
tests (though such ultra-thin sheaths are not ideal in the field), whereas
full-scale tests with 5″–5.5″ casing typically assume ~12–13 mm (≈0.5″)
cement sheaths. If the open hole is larger or washed out, the cement layer can
be thicker, but very large annular gaps risk channeling if not properly
cemented. On the other hand, too narrow an annulus (<0.3–0.4″) is undesirable
as it complicates mud removal and cement placement. **In summary, a ~0.5″
thick cement ring is a typical target around 5.5″ casing in the Bakken**,
providing a solid hydraulic seal and mechanical support when properly placed.

### Effect of cement shrinkage on sheath width (microannulus formation)

Oilwell cement undergoes slight bulk shrinkage as it sets — on the order of
**1–2% volume reduction** for typical Portland-based systems. This small
shrinkage does **not dramatically thin the cement sheath** in a uniform way
(the overall sheath thickness remains roughly in the same range). However,
shrinkage can lead to the cement **debonding at one of the interfaces**
(casing or formation), forming a **micro-annulus**, i.e. a very narrow gap.
Essentially, as the cement volume contracts, it may pull away from the steel
or rock, leaving a micro-scale separation without significantly changing the
bulk radial thickness of the cement ring. In practice, micro-annuli are
**extremely thin (typically less than 1 mm in width)**. Field cement bond log
analyses define micro-annulus gaps on the order of **a few thousandths of an
inch up to a few hundredths (tens to hundreds of microns)**. For instance,
real cement evaluation logs have documented interface gaps ranging from only a
few micrometers to a few millimeters in extreme cases, though gaps toward the
high end of that range are rare. A microannulus of ~0.1 mm (0.004″) is
considered a mild case, while 0.5 mm would be a severe loss of bond.

After shrinkage, the **effective sealing width** of the cement sheath is
slightly reduced by the presence of any microannulus, but the **physical
cement layer thickness remains ~0.4–0.6″** in our example. In other words, you
still have about a half-inch cement sheath encircling the casing, but a tiny
sliver of that may be a gap if shrinkage-induced debonding occurs. This
micro-gap can compromise zonal isolation by allowing fluid migration if
continuous. Notably, horizontal wells in the Bakken are subjected to pressure
and temperature cycles (e.g. during fracturing and production) that can
further stress the cement. Rapid cooling of the casing (such as when pumping
cold fluids) can induce additional **"chilling" shrinkage** of the cement or
casing contraction, potentially opening a microannulus if the cement is not
sufficiently resilient. The **primary concern** is not that the cement
sheath's thickness drastically decreases, but that a **circumferential
microannular channel** can form. This is why even a **very small gap (on the
order of 0.1–0.5 mm)** at the interface is taken seriously — it can extend
along the annulus and become a leakage path despite the cement sheath still
being largely in place.

# Fluid estimation

I will estimate how much fluid will leak during stimulation of the producer.
We are mainly using Darcy's law:

$$
q = \frac k\mu \frac A L \Delta p
$$

where $k$ is permeability, $\mu$ is viscosity, $A$ is the area of the leakage
zone, $L$ is the spacing between two clusters, and $\Delta p$ is the pressure
difference between two stages.

# References

1. de Haas, G. D., Kreijger, P. C., Niël, E. M. M. G., Slagter, J. C., Stein,
   H. N., Theissing, E. M., & van Wallendael, M. (1975). The shrinkage of
   hardening cement paste and mortar. *Cement and Concrete Research*, 5(4),
   295–319.
2. [Creep and shrinkage of concrete (Wikipedia)](https://en.wikipedia.org/wiki/Creep_and_shrinkage_of_concrete)
3. U.S. Federal Cementing Clearance Regulation,
   [43 CFR § 3172.7 — Casing and cementing](https://www.law.cornell.edu/cfr/text/43/3172.7):
   requires minimum annular clearance of 0.422″ on all sides of casing collars.
4. Lin Y.H. et al., *Natural Gas Industry B*, 2020,
   [doi:10.1016/j.ngib.2020.09.007](https://doi.org/10.1016/j.ngib.2020.09.007):
   experimental casing-cement-formation assembly with casing OD = 60.3 mm,
   borehole = 76 mm, cement sheath thickness = 8 mm.
5. *Oil & Gas Journal* — "Proper centralizers can improve horizontal well
   cementing" ([ogj.com](https://www.ogj.com/)): cement shrinkage ~1–2%,
   minimized via additives; good centralization = >80% standoff.
6. [CBL Interpretation Manual, April 2013](https://fr.scribd.com/document/135946220/April16-2013-CBL-Interpretation):
   micro-separation typically <1 mm, detected through CBL delta response.
7. *Frontiers in Energy Research* — ["Impact of microannulus on efficiency..."](https://www.frontiersin.org/articles/10.3389/fenrg.2022.938077):
   microannulus observed via cement log, microns to a few mm wide.
8. S. M. Ali et al., *SPE 91399* ([seal-tite.com](https://seal-tite.com/)):
   pressure-activated sealant injection into micro-annular leaks.
9. [Visco-Plastic Flow in Squeeze Cementing, University of Strathclyde](https://strathprints.strath.ac.uk/74825/):
   squeeze slurries designed to invade narrow microannular pathways.
10. [SPE-206052-MS](https://onepetro.org/SPEATCE/proceedings-abstract/21ATCE/3-21ATCE/D031S026R002/462120):
    cement clearance $CC = (\text{Borehole} - \text{Casing})/2$, referred to as
    cement sheath thickness in SPE design guides.
