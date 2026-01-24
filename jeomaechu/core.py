import random
from typing import List, Optional, Tuple
from .data import MENU_DATA, TAGS

class JeomMaeChu:
    def __init__(self):
        self.menus = MENU_DATA
        self.tags = TAGS
        
        # Optimization: Pre-calculate flattened lists for faster access
        self._all_options: List[Tuple[str, str]] = [
            (cat, item) for cat, items in self.menus.items() for item in items
        ]
        self._all_menus_only: List[str] = [item for _, item in self._all_options]
        self._categories: List[str] = list(self.menus.keys())
        self._tags: List[str] = list(self.tags.keys())

    def get_all_menus(self) -> List[str]:
        """Returns a list of all unique menu names."""
        return list(set(self._all_menus_only))

    def recommend_random(self) -> Tuple[str, str]:
        """Returns a random (category, menu) tuple."""
        return random.choice(self._all_options)

    def recommend_many(self, count: int = 1, category: Optional[str] = None, tag: Optional[str] = None) -> List[Tuple[str, str]]:
        """Returns a list of unique random (category, menu) tuples with optional filtering."""
        options = self._all_options
        
        if category:
            if category in self.menus:
                options = [(category, menu) for menu in self.menus[category]]
            else:
                return []
        elif tag:
            if tag in self.tags:
                options = [(None, menu) for menu in self.tags[tag]] # Category is ambiguous for tags
            else:
                return []
        
        pick_count = min(count, len(options))
        if pick_count <= 0:
            return []
        return random.sample(options, pick_count)

    def recommend_by_category(self, category: str) -> Optional[str]:
        """Recommends a menu within a specific category."""
        if category in self.menus:
            return random.choice(self.menus[category])
        return None

    def recommend_by_tag(self, tag: str) -> Optional[str]:
        """Recommends a menu based on a mood/tag."""
        if tag in self.tags:
            return random.choice(self.tags[tag])
        return None

    def get_categories(self) -> List[str]:
        return list(self.menus.keys())

    def get_tags(self) -> List[str]:
        return list(self.tags.keys())
