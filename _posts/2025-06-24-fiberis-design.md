---
layout: post
title: "MOOSE Utils: state of the art of fiberis.moose"
date: 2025-06-24
categories:
  - theory
---

This note introduces the state of art, of my fibeRIS simulator -> MOOSE extension.

# MOOSE utils in fibeRIS: state of art

Shenyao Jin, RCP@CSM, shenyaojin@mines.edu

## Use cases

It is written in python, the coding details are shown in another note.

## MOOSE environment

I would like to do the work on Lakota. Still, I installed MOOSE env on both Mac and Lakota.

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

> [!Note] Clean the cache if encountered error
The anaconda itself will cause error
> 

I have successfully installed MOOSE on both my Mac, and Lakota.

- Mac: `/Users/shenyaojin/projects`
- Lakota (I think it should work for other Linux machine): `/rcp/rcp42/home/shenyaojin/Documents/bakken_mariner/moose_env/moose/`

### Modules: porous flow

MOOSE has lots of pre-defined modules. In my project we will just use THM model's, which is called [porous flow](https://mooseframework.inl.gov/modules/porous_flow/).

I will attach some example code in 

The **governing equation**, it says is:

$$

0=\frac{\partial M^\kappa}{\partial t} + M^\kappa \nabla\cdot \textbf{v}s + \nabla\cdot \textbf{F}^\kappa+\Lambda M^\kappa-\phi I{chem}-q^\kappa

$$

- $M$: Mass of fluid per bulk volume
- $v_s:$ Velocity of the porous solid skeleton
- $F$: Flux
- $\Lambda$: Radioactive decay rate
- $\phi I_{chem}$: Represents chemical precipitation or dissolution.
- $q$: Source

For the **mass density**, it can be presented by:

$$

M^\kappa = \phi \sum_\beta S_\beta \rho_\beta\chi_\beta^\kappa+(1-\phi)C^\kappa

$$

The solid's porosity is $\phi$. $S_\beta$ is the saturation of phase $\beta$ (solid, liquid, gas, NAPL). $\rho_\beta$ is the density of phase $\beta$. $\chi^\kappa_\beta$ is the mass fraction of component $\kappa$ present in phase $\beta.$ The final term represents fluid absorption into the porous-rock skeleton: $C_\kappa$ is the mass of absorbed species per volume of solid rock-grain material.

The saturation and mass fractions must have a sum of **1**.

For the **Flux**, is a sum of advective flux and diffusive and dispersive flux:

$$
F^\kappa = \sum_\beta \chi_\beta^\kappa \mathrm{F}\beta^{\mathrm{advective}}+\mathbf F_{\mathrm{diffusion+dispersion}}^\kappa
$$

For the **advection**, it is governed by **Darcy's law**.

$$
\mathbf{F}_\beta^{\mathrm{advective}} = \rho\beta \mathbf v_\beta=-\rho_\beta\frac{kk_{r,\beta}}{\mu_\beta}(\nabla P_\beta-\rho_\beta\mathbf g)
$$

### Kernels in porous media diffusion

![image.png](attachment:80b45e63-9b1d-4e6a-af07-85f73f38272c:image.png)

## MOOSE extension: modules

For now: 

The fibeRIS MOOSE extension provides a comprehensive suite of tools for interacting with the MOOSE framework, enabling programmatic control over simulation workflows. For a detailed overview, refer to the [fibeRIS MOOSE Extension README](https://github.com/shenyaojin/fibeRIS/blob/main/src/fiberis/moose/README.md).

- **Configuration (`config.py`)**: Defines Python classes (`HydraulicFractureConfig`, `SRVConfig`) to specify parameters for hydraulic fractures and stimulated reservoir volumes.
- **Input File Generation (`input_generator.py`)**: Generates MOOSE input files (`.i`) from Python dictionary configurations. Includes `MooseBlock` base class.
- **Model Building (`model_builder.py`)**: A higher-level API to construct MOOSE input files using the configuration objects, simplifying the definition of physical features and mesh operations.
- **Input File Editing (`input_editor.py`)**: Allows reading, modifying, and writing existing MOOSE input files using `pyhit` and `moosetree`.
- **Simulation Execution (`runner.py`)**: Programmatically runs MOOSE simulations, captures output, and manages the execution process, including MPI support.
- **Post-processing (`postprocessor.py`)**: Reads MOOSE output files (primarily Exodus `.e` files) using `meshio` and extracts data for analysis, including nodal/cell variables and time-dependent data. **Note:** it is not used anymore for I have integrated all visualization code to `fiberis.analyzer` .

## Topic: mesh refinement (v1)

<aside>
💡

1. No implement of the original mesh grid refinement. Only keep the HF/SRV refinement.
2. AMA will be implemented.
3. This is the old state of art doing mesh setup. Now please refer to v2.
</aside>

My strategy combines initial targeted discretization with dynamic mesh adaptation:

1. **Targeted Initial Refinement:** Key features like hydraulic fractures and Stimulated Reservoir Volumes (SRVs) receive user-specified initial refinement. This ensures these a priori known active regions are adequately discretized from the start, using parameters in our `HydraulicFractureConfig` and `SRVConfig` objects, which interface with MOOSE's `RefineBlockGenerator`.
2. **Reasonable Base Matrix Discretization:** The main reservoir matrix starts with a user-defined, reasonably coarse mesh. We avoid complex global manual refinement for the matrix initially to simplify input and reduce overhead.
3. **Automatic Mesh Adaptivity (AMA):** The core of our long-term strategy is implementing MOOSE's robust AMA. This technique dynamically refines or coarsens the mesh based on evolving solution features (e.g., error indicators, gradients of pressure, displacement, stress). This focuses computational effort where needed, such as propagating fracture tips or areas with sharp fluid flow changes.

**Alignment with State-of-the-Art Practices:**

This hybrid approach aligns with best practices in computational mechanics and multiphysics:

- **Efficiency and Accuracy:** AMA offers optimal accuracy for a given computational cost by refining active areas while keeping quiescent regions coarser.
- **Dynamic Phenomena:** For problems with moving boundaries or localized phenomena typical of hydraulic fracturing, AMA is essential for accurate and efficient physics capture.
- **MOOSE Capabilities:** We will leverage MOOSE's comprehensive AMA tools (error indicators, marking strategies, mesh modification algorithms) and expose them to users controllably through our Python API.

By combining targeted initial refinement for critical zones with a powerful AMA strategy, we aim to provide a user-friendly tool that delivers accurate and computationally efficient results for complex hydraulic fracturing simulations.

AMA Link: 

[ex05_amr.md|MOOSE](https://mooseframework.inl.gov/releases/moose/v1.0.0/examples/ex05_amr.html)

## Topic: mesh refinement (v2)

<aside>
💡

Change in v2: I realized MOOSE will not accept the mesh without refining. We must do refinement on the mesh. 

</aside>

The mesh setup will be able to handle multiple hydraulic fractures. Our model builder constructs a sophisticated 2D mesh directly within the MOOSE framework, specifically tailored for simulating multiple horizontal hydraulic fractures. The process begins by creating a series of horizontal layers using MOOSE's `GeneratedMeshGenerator`. For each layer that will contain a fracture, two sub-layers are generated with a `bias_y` parameter, creating a finer mesh resolution around the fracture's centerline. These sub-layers are then seamlessly joined using the `StitchedMeshGenerator`. This process is repeated and chained together to form a single, continuous base mesh with inherent local refinement along all specified fracture paths.

Following the base mesh construction, distinct material regions are defined not by geometric cutting, but by assigning block IDs. The `SubdomainBoundingBoxGenerator` identifies regions for hydraulic fractures and stimulated reservoir volumes (SRV) by marking all mesh elements that fall within user-defined bounding boxes. To further enhance accuracy, the `RefineBlockGenerator` can be selectively applied to these named blocks, increasing element density where it's needed most. Finally, blocks and boundaries are assigned descriptive names using `RenameBlockGenerator` and `SideSetBoundingBoxGenerator`, respectively, ensuring a well-organized and readable input file for the MOOSE solver.

## Topic: state of art: the MOOSE .i file generator

### 1. Core Philosophy and Architecture

The design philosophy is centered on **separation of concerns** and **programmatic construction**. Instead of treating the `.i` file as a monolithic text block, the toolkit deconstructs it into logical Python objects. The core architecture revolves around a clear, multi-stage workflow:

1. **Configuration (`config.py`):** Define high-level simulation parameters using a dedicated configuration object.
2. **Model Building (`model_builder.py`):** Use a "builder" class to translate the configuration into a structured Python dictionary that mirrors the blocks and sub-blocks of a MOOSE `.i` file.
3. **Input Generation (`input_generator.py`):** Pass the structured dictionary to a generator class that writes the final, syntactically correct `.i` file. It directly interacts with the file (I/O).

This layered approach makes the process of creating simulations highly modular, reusable, and less prone to manual error.

*Fig. 1: The high-level workflow from configuration to file generation.*

### 2. API Design and Key Components

The power of the toolkit lies in its well-defined classes, each responsible for a specific part of the generation workflow.

### 2.1. `MooseConfig`: Centralized Parameters

**File:** `src/fiberis/moose/config.py`

The foundation of any simulation is its configuration. The `MooseConfig` class, implemented as a Python `dataclass`, serves as a single source of truth for all essential parameters. This approach avoids "magic strings" or scattered variables in the code.

**API Design:**

- A `dataclass` is used for simplicity, type hinting, and automatic initialization.
- Parameters are logically grouped (e.g., mesh properties, material properties, execution settings).
- It provides default values where appropriate, making it easy to set up standard simulations.

**Example Usage:**

```python
# From: src/fiberis/moose/config.py
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class MooseConfig:
    """Configuration for the MOOSE simulation."""
    app_name: str = 'your_app'
    moose_path: str = '/path/to/moose'

    # Mesh parameters
    mesh_file: str = 'mesh.e'
    dim: int = 3

    # Material properties
    materials: Dict[str, Dict[str, float]] = field(default_factory=dict)

    # Execution control
    end_time: float = 1.0
    dt: float = 0.1
    # ...

# In a user script:
config = MooseConfig(
    mesh_file='geometry/wellbore_mesh.e',
    dim=3,
    end_time=3600,
    dt=100
)

```

### 2.2. `ModelBuilder`: Assembling the Physics (OLD)

**File:** `src/fiberis/moose/model_builder.py`

The `ModelBuilder` is the heart of the system. It takes the `MooseConfig` object and constructs a detailed, nested Python dictionary. This dictionary, `self.input_dict`, is a direct representation of the MOOSE input file structure, but in a format that is easy to manipulate programmatically.

**API Design:**

- The class is initialized with a `MooseConfig` instance.
- Dedicated methods (`build_mesh`, `build_variables`, `build_kernels`, `build_bcs`, etc.) are responsible for creating specific blocks of the input file.
- Each `build_*` method populates a key in the main `input_dict`.
- The final dictionary is retrieved using the `get_input_dict()` method.

**Example of Building the `[Mesh]` Block:**
The `build_mesh` method shows how a high-level configuration is translated into the low-level dictionary structure required by the generator.

```python
# Simplified from: src/fiberis/moose/model_builder.py
class ModelBuilder:
    def __init__(self, config: MooseConfig):
        self.config = config
        self.input_dict = {}

    def build_mesh(self):
        """Builds the [Mesh] block."""
        self.input_dict['Mesh'] = {
            'file': self.config.mesh_file,
            'type': 'FromFile'
        }

    def build_variables(self):
        """Builds the [Variables] block."""
        self.input_dict['Variables'] = {
            'porepressure': {
                'family': 'LAGRANGE',
                'order': 'FIRST'
            }
        }

    # ... other build methods for [Kernels], [BCs], etc.

    def get_input_dict(self):
        # Call all build methods to fully populate the dict
        self.build_mesh()
        self.build_variables()
        # ...
        return self.input_dict

```

### 2.2r. `ModelBuilder`: Tools to convert actual parameters to MOOSE format

TODO 

### 2.3. `MooseInputGenerator`: Writing the `.i` File

**File:** `src/fiberis/moose/input_generator.py`

This class has one primary responsibility: to take the dictionary created by `ModelBuilder` and serialize it into a correctly formatted MOOSE `.i` file.

**API Design:**

- It is initialized with the `input_dict` from the `ModelBuilder`.
- The main public method is `generate(output_path)`, which writes the file.
- Internal, private methods (`_generate_block`, `_generate_sub_block`, `_generate_key_value_pairs`) recursively traverse the dictionary and handle the specific formatting rules of the MOOSE syntax (e.g., brackets, indentation, key-value pairs).

**Core Logic:**

```python
# Simplified from: src/fiberis/moose/input_generator.py
class MooseInputGenerator:
    def __init__(self, input_dict: dict):
        self.input_dict = input_dict

    def generate(self, output_path: str):
        """Generates the MOOSE input file."""
        content = []
        for block_name, block_content in self.input_dict.items():
            content.append(self._generate_block(block_name, block_content))

        with open(output_path, 'w') as f:
            f.write('\n'.join(content))

    def _generate_block(self, name, content):
        lines = [f'[{name}]']
        # Helper methods would format the content here...
        lines.append('[]')
        return '\n'.join(lines)

```

This design cleanly separates the *what* (the model structure defined in `ModelBuilder`) from the *how* (the file syntax managed by `MooseInputGenerator`).

### 3. End-to-End Workflow Example

The following script illustrates how a user would interact with the API to generate a `.i` file.