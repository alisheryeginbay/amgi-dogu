# amgi

This repo will contain my collection of scripts and utilities for remembering things.

## Major System Anki deck

```sh
uv run amgi major                 # writes major_system.apkg
uv run amgi major -o deck.apkg    # custom output path
```

The deck has one card for each digit (0–9), showing its consonant sounds and a hint for remembering them. Note IDs stay the same across runs, so re-importing updates the deck you already have instead of adding duplicates.
