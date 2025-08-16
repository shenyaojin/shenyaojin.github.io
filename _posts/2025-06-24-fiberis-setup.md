---
layout: post
title: "fiberis.moose setup"
date: 2025-06-24
categories:
  - theory
---

This note introduces the state of art, of my fibeRIS simulator -> MOOSE extension.

# How to install MOOSE environment?

Shenyao Jin, RCP@CSM, shenyaojin@mines.edu

## Use cases

The MOOSE environment is used to run the `fibeRIS` simulator, which is a finite element code for simulating multiphysics problems.

## MOOSE environment

I would like to do the work on Lakota. Still, I installed MOOSE env on both Mac and Lakota. It is suggested to install MOOSE on your work directory, such as `~/projects/` or `~/moose/`, so that you can easily manage the MOOSE environment and its dependencies.

### Installation (refer to INL's webpage)

For my Mac, it is already compiled and is in `~/.moose/` (I deleted it recently, instead, a newer version is installed in `~/projects/`).

The installation will be in the **Bakken Mariner folder** so that I can easily do the simulation using the specific module.

So I will first install the MOOSE environment on Lakota. I updated my conda (if conda returns error while compiling, you should try **mini forge** suggested by INL, delete all anaconda files, including .conda, .condarc, etc.) first.

```bash
conda update --all --yes

```

Add INL's public channel to gain access to INL's conda package library:

```bash
conda config --add channels <https://conda.software.inl.gov/public>

```

> [!Caution] DO NOT USE SUDO
If you find yourself using sudo commands while engaging Conda commands... something is not right. The most common reason for needing sudo is due to an improper Conda installation. Conda should be installed to your home directory, without any use of sudo
> 

This command is working on my Linux (depends on time, pls refer to this [website](https://mooseframework.inl.gov/getting_started/installation/conda.html); still suggest to align with the MOOSE version):

```bash
conda create -n moose moose-dev=2024.12.02=mpich

```

I suggest to use this on Mac:

```bash
conda create --name moose moose-libmesh moose-tools

```

Then

```bash
conda init bash
conda init zsh

```

I don't know why we need to initialize bash in macOS(for the default shell is zsh), so I add zsh line.

Then enter this then you can start compile code:

```bash
conda activate moose

```

Compile from the source code:

```bash
mkdir -p ~/projects
cd ~/projects
git clone <https://github.com/idaholab/moose.git>
cd moose
git checkout master

```

Build MOOSE:

```bash
cd ~/projects/moose/test
make -j 6

```

Run test:

```bash
cd ~/projects/moose/test
./run_tests -j 6

```

> Clean the cache if encountered error
The anaconda itself will cause error
> 

## Compile MOOSE: porous media module

To use `fiberis.moose`, you must compile the MOOSE `porous_flow` module. Run `Makefile` in the `~/projects/moose/modules/porous_flow` directory:

```bash
cd /path/to/moose/root/modules/porous_flow
make -j 6

```

If successful, you will see a binary file named `porous_flow-opt` in the same directory. 

![Porous Flow Module]({{ 'public/images/0815_moose_fig.png' | relative_url }})
Fig 1. Porous Flow Module

## Configure python path

For MacOS and Linux, you need to set the `PYTHONPATH` environment variable to include the MOOSE Python bindings. You can do this by adding the following line to your `.bashrc` or `.zshrc` file:

```bash
export PYTHONPATH=$PYTHONPATH:~/projects/moose/python
```
