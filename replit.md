# fieldviz-mini

## Overview
A tiny Python library for visualizing 2D dynamical fields, attractors, and flow lines using a compact, clean API. This is a PyPI-ready package for exploring vector fields and streamlines.

## Project Structure
```
fieldviz-mini/
├── README.md              # Package documentation
├── pyproject.toml         # Build configuration (setuptools)
├── setup.cfg              # Package discovery config
├── LICENSE                # MIT License
├── fieldviz_mini/         # Core package
│   ├── __init__.py        # Public API exports
│   ├── fields.py          # VectorField class
│   ├── integrators.py     # Euler & RK4 integrators
│   ├── visualize.py       # Plotting functions
│   └── presets.py         # Preset field configurations
├── examples/              # Usage examples
│   └── simple_attractor.py
└── tests/                 # Test suite
    ├── test_fields.py
    └── test_integrator.py
```

## Key Components
- **VectorField**: Core class for defining 2D vector fields
- **Integrators**: Euler and RK4 numerical integration methods
- **Visualization**: Quiver plots and streamline rendering
- **Presets**: spiral_sink, saddle_point, lorenz_field

## Running Locally
```bash
# Install in development mode
pip install -e .

# Run tests
pytest tests/ -v

# Run example
python examples/simple_attractor.py
```

## Building for PyPI
```bash
pip install build twine
python -m build
twine upload dist/*
```

## Recent Changes
- 2025: Initial package creation with full PyPI-ready structure

## Dependencies
- numpy
- matplotlib
