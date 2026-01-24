# jeomaechu (점메추)

A professional Python package for lunch menu recommendations. Never worry about "What should I eat for lunch?" ever again.

## Features
- **Fast & Optimized**: Pre-cached datasets for instant recommendations.
- **Easy CLI**: Run `jeomaechu` directly for a quick pick.
- **Massive Menu Database**: 500+ items including franchises (Brand).
- **Pythonic API**: Clean and efficient API for developers.

## Installation
```bash
pip install .
```

## Usage (CLI)
The commands are now shorter and easier to use:

```bash
# Just run it! (Default pick)
jeomaechu

# Pick a menu (explicit)
jeomaechu pick

# Pick 5 menus at once
jeomaechu pick -n 5

# Recommended by category or tag
jeomaechu pick -c "Korean (한식)"
jeomaechu pick -t "Spicy (매콤)"

# Exploration
jeomaechu cats    # List categories
jeomaechu tags    # List tags
jeomaechu all     # Show EVERYTHING
```

## Python API
The API is optimized for performance:

```python
from jeomaechu import JeomMaeChu

engine = JeomMaeChu()

# Get one random
cat, menu = engine.recommend_random()

# Get many (Fast sampling)
results = engine.recommend_many(5)
```

## License
MIT
