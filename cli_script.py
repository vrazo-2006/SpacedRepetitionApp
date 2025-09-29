# still need to check why it doesn't work from my other terminal and format the json that is being
#printed out to look better when using --show flag.

import argparse
import json
from pathlib import Path
from datetime import datetime  # to get the time each intervel was created

intervals = [1, 3, 7, 14, 31, 93, 186, 365]
DATA_FILE = Path("/Users/vrazo/Desktop/code/workplace/Spaced_Repetition_App/SpacedRepetitionApp/my_user_memory.json")
DEFAULT_DATA = {"flash_cards": {}}


def save_data(payload: dict) -> None:
    DATA_FILE.write_text(json.dumps(payload, indent=2))


def load_data() -> dict:
    if not DATA_FILE.exists():
        data = DEFAULT_DATA.copy()
        save_data(data)
        return data

    raw = DATA_FILE.read_text().strip()
    if not raw:
        data = DEFAULT_DATA.copy()
        save_data(data)
        return data

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        data = DEFAULT_DATA.copy()
        save_data(data)
        return data


data = load_data()

# Write a new nested key into the "concept" object in the json
def new(object, flashcard_front, flashcard_back):
    time = datetime.now().isoformat(timespec="seconds")
    # Create object if it doesn't exist
    if object not in data:
        data[object] = {}
    # Creates nest
    data[object][flashcard_front] = {
        "created_at": time,
        "front": flashcard_front,
        "back": flashcard_back,
        }
    #data[object][concept_name][time] = f"{time}"
    save_data(data)
    return 0

# Show current concepts and their progress
def show(show):
    print(data)
    return 0

# Create parser for CLI
def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Spaced Repetition App', 
        usage = 'CLI to track spaced repetition intervals and progress')
    parser.add_argument(
        '--show', 
        action='store_true',
        help='Show progress for a specefic concept or all concepts' )
    parser.add_argument( #doesn't expect any arguments
        '--new', 
        nargs=2,
        type=str,
        help='create a new flashcard')
    return parser

# parse arguments
def main():
    parser = create_parser()
    args: argparse.Namespace = parser.parse_args()
    front, back = args.new
    if args.show:
        show(args.show)
    elif args.new:
        # there has to be a better way to do this
        new("flash_cards", front, back)
    return 0

if __name__ == '__main__':
    main()
