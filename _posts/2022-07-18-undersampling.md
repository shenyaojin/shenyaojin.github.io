---
layout: post
title: Undersampling and Aliasing
categories: [Signal processing]
description: Signal processing
keywords: Signal processing
mathjax: true
---

# Sampling?
The process of converting a continuous-time signal into a discrete-time signal is called sampling.

- sampling period: the time between two successive sampling instants.

# Nyquist Sampling Principle
It defined the theoretical minimum sampling rate which is related to the maximum of the frequency of the signal.

# Effects of under sampling(Aliasing)
If a signal is sampled less than Nyquist sample rate, then it is called under sampled.

$$
X_s(\omega)=\frac{1}{T}\sum_{n=-\infty}^{+\infty}X(\omega-n\omega_s)
$$

The phenomenon in which a high-frequency component in the frequency spectrum of signal takes identity of a lower frequency component in the spectrum of the sampled signal is called aliasing.

If we sample the data in frequency $$\omega_s$$ then all the components with a frequency more than $$\omega_s/2$$ create aliasing. The low-pass filter (LPF) is commonly known as the anti-aliasing filter.