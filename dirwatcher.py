import dirwatch_logger as watch
import os
import sys
import signal
import time
import datetime
import argparse

__author__ = """
Read Kathy Tran's Question on after-hours-python channel
https://stackoverflow.com/
        questions/4785244/search-a-text-file-and-print-related-lines-in-python"""


exit_flag = False


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT.
    Other signals can be mapped here as well (SIGHUP?)
    Basically it just sets a global flag,
    and main() will exit it's loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name (the python3 way)
    watch.logger.warn('Received ' + signal.Signals(sig_num).name)
    # log the signal name (the python2 way)
    signames = dict((k, v) for v, k in
                    reversed(sorted(signal.__dict__.items()))
                    if v.startswith('SIG') and not v.startswith('SIG_'))
    watch.logger.warn('Received ' + signames[sig_num])
    exit_flag = True


def scan_file(filename):
    with open(filename, "r") as f:
        lines = f.read()
        for line in lines:
            pass


def detect_added_files(files_dict):
    pass


def detect_removed_files(files_dict):
    pass


def watch_dir(polling_interval):
    files_dict = {}
    while polling_interval:
        pass


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--pollint',
        help='set the polling interval for the dirwatcher')
    parser.add_argument(
        '-s', '--search',
        help='sets the magic word to find in the directories')
    parser.add_argument(
        '-f', '--filter',
        help='filters the file extension to search within for the magic word')
    parser.add_argument(
        '-w', '--watch',
        help='specifies the directory to watch')

    return parser


def main():
    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now signal_handler will get called if OS sends
    # either of these to my process.

    while not exit_flag:
        try:
            pass
            # watch_dir(polling_interval)
        except Exception as e:
            pass
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            # put a sleep inside my while loop
            # so I don't peg the cpu usage at 100%

        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start.
    start_time = datetime.datetime.now()
    watch.logger.info(
        '\n'
        ('-' * 20) + '\n'
        'Running {0}...\n'
        'Started: {1}\n'
        ('-' * 20) + '\n'
        .format(__file__, start_time.isoformat())
    )
    parser = create_parser()

    args = parser.parse_args()
    watch_dir(args)
    total_uptime = datetime.datetime.now() - start_time

    watch.logger.info(
        '\n'
        ('-' * 20) + '\n'
        'Stopping {0}...\n'
        'Total Uptime: {1}\n'
        ('-' * 20) + '\n'
        .format(__file__, str(total_uptime))
    )

    # """Parse args, scan for urls, get images from urls"""
    # parser = create_parser()

    # if not args:
    #     parser.print_usage()
    #     sys.exit(1)

    # parsed_args = parser.parse_args(args)

    # img_urls = read_urls(parsed_args.logfile)

    # if parsed_args.todir:
    #     download_images(img_urls, parsed_args.todir)
    # else:
    #     print('\n'.join(img_urls))


if __name__ == '__main__':
    main(sys.argv[1:])
