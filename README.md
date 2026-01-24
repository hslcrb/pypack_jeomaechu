# jeomaechu (점메추) 🍱

[한국어 버전](README_ko.md)

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

### ⚡ Shorthand & Pro Commands
For those in a real hurry, we support direct Korean commands for specific moods.

**Pro Korean Commands:**
| Command | Description | Based on |
| :--- | :--- | :--- |
| `집밥` / `자취` / `혼밥` | Realistic home/solo meals | Real Home Category |
| `대충` | Quick & Easy | Quick Tag |
| `한식` / `중식` / `일식` / `양식` | Main 4 categories | Respective Categories |
| `아시아` / `동남아` / `기타` | Asian cuisines (Thai, etc) | Asian Category |
| `고기` / `해물` | Favorite Ingredients | Meat / Seafood Tag |
| `매운거` / `매워` | Spicy food | Spicy Tag |
| `국물` / `해장` | Soupy / Hangover meals | Soupy Tag |
| `면` / `밥` | Noodles / Rice | Noodle / Rice Tag |
| `분식` | Korean snacks (Tteokbokki, etc) | Snack Tag |
| `술안주` / `안주` | Bar food / Snacks | Bar Food Tag |
| `건강` / `다이어트` | Healthy / Diet meals | Healthy Tag |
| `헤비` / `기름진거` | Heavy / Oily meals | Heavy Tag |
| `글로벌` / `세계` | Global cuisines | Global Tag |
| `전통` / `정통` | Authentic/Native taste | Authentic Tag |
| `일상` / `맨날` | Daily/Regular meals | Daily Tag |
| `브랜드` / `프차` | Chain restaurants | Brand Category |
| `아무거나` | Absolute random | All |

**Usage Examples:**
```bash
j 집밥        # 1 Real home meal recommendation
j 자취 -n 3   # 3 Bachelor meal recommendations
j 매워        # Spicy food recommendation
j 해장        # Soup/Hangover food recommendation
```

**System Command Shorthands:**
| Full Command | Shorthand | Example |
| :--- | :--- | :--- |
| `jeomaechu` | `j` | `j` |
| `pick` | `p` | `j p -n 5` |
| `cats` | `c` | `j c` |
| `tags` | `t` | `j t` |
| `all` | `a` | `j a` |

**Category Abbreviations (for `-c`):**
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

---
**Author:** Rheehose (Rhee Creative) (2008-2026)  
**Last Updated:** 2026.01.24 (Sat) KST
