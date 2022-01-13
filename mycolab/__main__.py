import sys
import click
from mycolab.genbank import search as mycolab_search, split_sequence


@click.group()
@click.version_option("1.0.0")
def main():
    """Genbank search tool"""
    pass


@main.command()
@click.argument('sequence', required=False)
def search(**kwargs):
    """Search Genbank nucleotide database"""
    results = mycolab_search(kwargs.get("sequence"))
    for result in results:
        print(f'>{result["description"]}')
        seq_lines = split_sequence(result.get('sequence'), max_line_len=80)
        for seq_line in seq_lines:
            print(seq_line)
        print()


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("mycolab")
    main()
