import argparse
import json
from pathlib import Path

intervals = [1, 3, 7, 14, 31, 93, 186, 365]

DATA_FILE = "my_user_memory.json"

with open(DATA_FILE, 'r') as file:
    data = json.load(file)

# Write a new nested key into the "concept" object in the json
def add_new_concept(object, concept_name):

    # Create object if it doesn't exist
    if object not in data:
        data[object] = {}

    # Add nested object
    data[object][concept_name] = concept_name

    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent = 2)

    return 0

# Add a new concept
def add(add):
    print(add)


    return 0

# Show current concepts and their progress
def show(show):
    print(show)


    return 0

# Create parser
def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Spaced Repetition App', 
        usage = 'CLI to track spaced repetition intervals and progress')
    parser.add_argument(
        '--show', 
        type=str,
        help='Show progress for a specefic concept or all concepts' )
    parser.add_argument(
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
        add_new_concept("concepts", args.add)
        

    return 0

if __name__ == '__main__':
    main()