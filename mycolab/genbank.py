import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


SEARCH_URL = "https://mycolab.org/api/genbank/v1/query"


def split_sequence(sequence: str, max_line_len: int = 80):
    """
    Split single-line FASTA sequence into multiple lines
    :param sequence: FASTA sequence
    :param max_line_len: Maximum sequence chars per line
    :return: List of sequence lines
    """
    line_len = 0
    read_chars = 0
    full_seq = list(sequence)
    seq_len = len(full_seq)
    seq_line = ''
    seq_lines = []

    while read_chars < seq_len:

        while line_len < max_line_len:

            if (len(full_seq) + line_len) <= max_line_len:
                seq_line += ''.join(full_seq)
                read_chars = seq_len
                break

            if len(full_seq) > 0:
                seq_line += full_seq.pop(0)
            else:
                break

            line_len = len(seq_line)
            read_chars += 1

        seq_lines.append(seq_line)
        line_len = 0
        seq_line = ''

    return seq_lines


def search(sequence: str, min_match: float = 95.0, max_results: int = 50):
    """
    Search MycoLab Genbank API
    :param sequence: FASTA sequence
    :param min_match: Minimum match accuracy
    :param max_results: Maximum number of Genbank results
    :return: Mycolab Genbank API Sequences
    """

    data = {'location': True, 'match': min_match, 'results': max_results, "sequence": sequence}
    r = requests.post(SEARCH_URL, json=data, verify=False)
    results = r.json()

    return results
