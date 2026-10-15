import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(prog="amgi-dogu", description="Scripts for remembering things.")
    commands = parser.add_subparsers(dest="command", required=True)

    major = commands.add_parser("major", help="Generate an Anki deck for the Mnemonic Major System.")
    major.add_argument("-o", "--output", type=Path, default=Path("major_system.apkg"),
                       help="output .apkg file (default: %(default)s)")
    major.add_argument("-n", "--deck-name", default="Major System",
                       help="Anki deck name (default: %(default)s)")

    args = parser.parse_args()
    if args.command == "major":
        from amgi_dogu.major_system import generate

        generate(args.output, args.deck_name)
        print(f"Wrote 10 digit sound cards to {args.output}")
