from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser()

    parser.add_argument('-d', '--series_dir', dest='series_dir')
    parser.add_argument('-s', '--set',  dest='set', nargs='+')

    parser.add_argument('--show', dest='show', action='store_true')
    parser.add_argument('--prev', dest='previous', action='store_true')

    args = parser.parse_args()

    return args
