import argparse


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--pollint',
        help='set the polling interval for the dirwatcher',
        default=1.0)
    parser.add_argument(
        '-s', '--search',
        help='sets the magic word to find in the directories')
    parser.add_argument(
        '-f', '--filter',
        help='filters the file extension to search within for the magic word',
        default=".txt")
    parser.add_argument(
        '-w', '--watch',
        help='specifies the directory to watch')

    return parser
