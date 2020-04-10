import argparse


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--pollint',
        help='set the polling interval for the dirwatcher',
        type=float,
        default=1.0)
    parser.add_argument(
        '-f', '--filter',
        help='filters the file extension to search within for the magic word',
        default=".txt")
    parser.add_argument(
        'watch',
        help='specifies the directory to watch')
    parser.add_argument(
        'search',
        help='sets the magic word to find in the directory')
    return parser
