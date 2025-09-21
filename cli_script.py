# still need to check why it doesn't work from my other terminal and format the json that is being
#printed out to look better when using --show flag.

import argparse
import json
from pathlib import Path
from datetime import datetime # to get the time each intervel was created

intervals = [1, 3, 7, 14, 31, 93, 186, 365]
DATA_FILE = "my_user_memory.json"
with open(DATA_FILE, 'r') as file:
    data = json.load(file)

# Write a new nested key into the "concept" object in the json
def add(object, concept_name):
    time = datetime.now().isoformat(timespec="seconds")
    # Create object if it doesn't exist
    if object not in data:
        data[object] = {}
    # Creates nest
    data[object][concept_name] = {
        "created_at": time,
        }
    #data[object][concept_name][time] = f"{time}"
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent = 2)
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
        '--add', 
        type=str,
        help='add new concept')
    return parser

# parse arguments
def main():
    parser = create_parser()
    args: argparse.Namespace = parser.parse_args()
    if args.show:
        show(args.show)
    elif args.add:
        # there has to be a better way to do this
        add("concepts", args.add)
    return 0

if __name__ == '__main__':
    main()