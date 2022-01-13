import sys
import click
from mycolab.genbank import search as mycolab_search, split_sequence


@click.group()
@click.version_option("1.0.4")
def main():
    """Genbank search tool"""
    pass


@main.command()
@click.argument('sequence', required=True)
@click.option('--match', default=95.0, help='Minimum match accuracy')
@click.option('--results', default=50, help='Maximum results')
def search(**kwargs):
    """Search Genbank nucleotide database"""
    sequence = kwargs.get('sequence')
    min_match = kwargs.get('match')
    max_results = kwargs.get('results')
    fastas = mycolab_search(sequence, min_match=min_match, max_results=max_results)
    for fasta in fastas:
        print(f'>{fasta["description"]}')
        seq_lines = split_sequence(fasta.get('sequence'), max_line_len=80)
        for seq_line in seq_lines:
            print(seq_line)
        print()


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("mycolab")
    main()
