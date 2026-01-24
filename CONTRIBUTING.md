# Contributing to jeomaechu

[한국어 버전](CONTRIBUTING_ko.md)

Thank you for your interest in improving `jeomaechu`! We welcome contributions of all kinds, especially adding new delicious menu items.

## How to Contribute

1.  **Add New Menus**: If you'd like to add more lunch options, please modify `jeomaechu/data.py`. 
    -   Ensure new items are strings.
    -   Use original pronunciations for global foods.
2.  **Report Bugs**: Open an issue if something isn't working as expected.
3.  **Suggest Features**: Want a new tag or a new filtering logic? Let us know!

## Technical Rules

-   Keep `MENU_DATA` and `TAGS` consistent.
-   When adding a menu to a category, try to find a relevant tag for it so it doesn't end up in "Everything" only.
-   **Add Shorthand Commands**: You can add new Korean shorthand commands in `jeomaechu/cli.py` using Typer. Please use the `_perform_pick` helper function to maintain consistency.
-   Ensure `JeomMaeChu` core logic remains fast and CLI-agnostic.

## Code Style

We follow PEP 8. Please ensure your code is clean and properly type-hinted.
