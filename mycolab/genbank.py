import requests

SEARCH_URL = "http://34.121.111.173/v1/sequences"


def split_sequence(sequence: str, max_line_len: int = 80):
    line_len = 0
    read_chars = 0
    full_seq = list(sequence)
    seq_len = len(full_seq)
    seq_line = ''
    seq_lines = []

    while read_chars < seq_len:
        while line_len < max_line_len:

            if len(full_seq) < max_line_len:
                seq_line = ''.join(full_seq)
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


def search(sequence: str):
    """
    :param sequence:
    :return:
    """

    data = {'location': True, 'match': 90, 'results': 50, "sequence": sequence}
    r = requests.post(SEARCH_URL, json=data)
    results = r.json()

    return results
