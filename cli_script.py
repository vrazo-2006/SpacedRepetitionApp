import argparse

intervals = [1, 3, 7, 14, 31, 93, 186, 365]

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
        add(args.add)
        

    return 0

if __name__ == '__main__':
    main()