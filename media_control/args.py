from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--episode", dest="episode")
    parser.add_argument("--set", dest="path")
    parser.add_argument("--show", dest="show")
    parser.add_argument("--prev", dest="previous")

    args = parser.parse_args()

    return args
