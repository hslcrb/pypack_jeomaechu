# jeomaechu (점메추) 🍱

A massive, professional-grade lunch menu recommendation engine for Python. Never worry about "What should I eat for lunch?" ever again. Featuring over 600+ curated items from authentic global cuisines to realistic everyday home meals.

---

## 🚀 Key Features

- **Massive Database**: 666+ hand-picked menu items.
- **100% Coverage Tagging**: Every item is categorized by taste, ingredient, and style.
- **Hyper-Realistic**: Includes "Real Home Meals" like "rice with seaweed snacks" or "cold rice in spicy soup."
- **Authentic Names**: Uses original pronunciations for global cuisines (e.g., *Butadon*, *Pescatore*, *Mala-xiangguo*).
- **Blazing Fast**: Optimized core engine with data caching for instant results.
- **Beautiful CLI**: Stylish terminal output powered by `rich`.

---

## 🛠 Installation

```bash
pip install .
```

---

## 💻 Usage (CLI)

The CLI is designed to be simple and intuitive.

### 🎲 Quick Pick (Default)
Just type the command and let fate decide.
```bash
jeomaechu
```

### 🎯 Specific Recommendations
Use the `pick` command for more control.

| Option | Shorthand | Description | Example |
| :--- | :--- | :--- | :--- |
| `--count` | `-n` | Number of items to recommend | `jeomaechu pick -n 5` |
| `--category`| `-c` | Filter by category | `jeomaechu pick -c "Korean (한식)"` |
| `--tag` | `-t` | Filter by mood/tag | `jeomaechu pick -t "Spicy (매콤)"` |

**Combined Example:**
```bash
# Pick 3 spicy seafood menus
jeomaechu pick -t "Seafood (해산물)" -t "Spicy (매콤)" -n 3
```

### 🔍 Exploration
Browse the massive database.
- `jeomaechu cats`: List all available food categories.
- `jeomaechu tags`: List all available mood/ingredient tags.
- `jeomaechu all`: View the **ENTIRE** menu database (formatted tables).

### ⚡ Shorthand Commands (Super Fast)
For those in a real hurry:

| Full Command | Shorthand | Filter Shorthand | Example |
| :--- | :--- | :--- | :--- |
| `jeomaechu` | `j` | - | `j` |
| `pick` | `p` | - | `j p -n 5` |
| `cats` | `c` | - | `j c` |
| `tags` | `t` | - | `j t` |
| `all` | `a` | - | `j a` |

**Category Abbreviations:**
You can use single characters for categories with `-c`:
- `한`: Korean
- `중`: Chinese
- `일`: Japanese
- `양`: Western
- `집`: Real Home Meals
- `아`: Asian
- `상`: Brand/Franchise

**Example:** `j p -c 한` (Recommended Korean menu)

---

## 🐍 Python API

Integrate the engine into your own apps.

```python
from jeomaechu import JeomMaeChu

# Initialize the optimized engine
engine = JeomMaeChu()

# Get a single random pick (Category, Menu)
cat, menu = engine.recommend_random()
print(f"How about {menu} from {cat}?")

# Get multiple picks with filters
# Returns List[Tuple[Optional[Category], Menu]]
picks = engine.recommend_many(count=10, tag="Spicy (매콤)")

# List all data
all_menus = engine.get_all_menus()
categories = engine.get_categories()
```

---

## 📑 Documentation
- [README (Korean)](README_ko.md)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE)
- [Notice](NOTICE)

---

## ⚖️ License
MIT License. See [LICENSE](LICENSE) for details.
