"""Generate an Anki deck for the Mnemonic Major System.

The deck contains one card per digit (0-9), mapping the digit to its consonant sounds.
"""

from pathlib import Path

import genanki

# Fixed IDs so re-importing the deck updates existing notes instead of duplicating them.
DECK_ID = 1_739_201_874
SOUND_MODEL_ID = 1_739_201_875

SOUNDS: dict[str, tuple[str, str]] = {
    "0": ("s, z, soft c", "<b>z</b> is the first letter of <b>z</b>ero"),
    "1": ("t, d, th", "<b>t</b> has one downstroke"),
    "2": ("n", "<b>n</b> has two downstrokes"),
    "3": ("m", "<b>m</b> has three downstrokes"),
    "4": ("r", "fou<b>r</b> ends in <b>r</b>"),
    "5": ("l", "<b>L</b> is the Roman numeral for 50"),
    "6": ("j, sh, ch, soft g, zh", "a mirrored <b>J</b> looks like 6"),
    "7": ("k, hard c, hard g, q", "<b>K</b> is made of two 7s"),
    "8": ("f, v, ph", "a cursive <b>f</b> looks like 8"),
    "9": ("p, b", "<b>p</b> is a mirrored 9"),
}

CSS = """
.card { font-family: -apple-system, Helvetica, Arial, sans-serif; font-size: 28px;
        text-align: center; color: #222; background: #fff; }
.nightMode .card, .night_mode .card { color: #eee; background: #2b2b2b; }
.big { font-size: 64px; font-weight: 600; }
.hint { color: #888; font-size: 20px; }
"""

SOUND_MODEL = genanki.Model(
    SOUND_MODEL_ID,
    "Major System: Sound",
    fields=[{"name": "Digit"}, {"name": "Sounds"}, {"name": "Hint"}],
    templates=[
        {
            "name": "Digit -> Sounds",
            "qfmt": '<div class="big">{{Digit}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer">{{Sounds}}'
            '<div class="hint">{{Hint}}</div>',
        },
    ],
    css=CSS,
    sort_field_index=0,
)


def build_deck(deck_name: str) -> genanki.Deck:
    deck = genanki.Deck(DECK_ID, deck_name)
    for digit, (sounds, hint) in SOUNDS.items():
        deck.add_note(genanki.Note(
            model=SOUND_MODEL,
            fields=[digit, sounds, hint],
            guid=genanki.guid_for("major-sound", digit),
        ))
    return deck


def generate(output: Path, deck_name: str = "Major System") -> None:
    genanki.Package(build_deck(deck_name)).write_to_file(output)
