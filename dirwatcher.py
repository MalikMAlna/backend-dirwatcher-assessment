import logging
import os
import sys
import signal
import time
import datetime
import dirwatcher_parser as wparse

__author__ = """
Read Kathy Tran's Question on after-hours-python channel
https://stackoverflow.com/questions/4785244/
    search-a-text-file-and-print-related-lines-in-python
    Received desperately need help from Jake H.
    Worked with Piero and the friday gang on on this as a demo"""

# Globals
exit_flag = False

# Logging Setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s--%(levelname)s--%(name)s--%(message)s")
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)


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
    logger.warn('Received ' + signal.Signals(sig_num).name)
    global exit_flag
    exit_flag = True


def scan_file(filename, magic_word, start_line):
    """Scans files for word starting on the last line where the scan ended"""
    with open(filename, "r") as f:
        search_idx = 0
        for search_idx, line in enumerate(f):
            if search_idx >= start_line:
                if magic_word in line:
                    logger.info(
                        "Found {}! in {} at line {}"
                        .format(magic_word, filename, (search_idx + 1)))
        return search_idx + 1


def watch_dir(dirpath, magic_word, extension, pollint):
    """Watches current directory for file changes"""
    files_dict = {}
    while not exit_flag:
        # Adding files to watch
        for filename in os.listdir(dirpath):
            if filename.endswith(extension) and filename not in files_dict:
                logger.info("{} has been added".format(filename))
                files_dict[filename] = 0
        # Removing files from watch
        for filename in list(files_dict):
            if filename not in os.listdir(dirpath):
                files_dict.pop(filename)
                logger.info(f"{filename} has been removed")
        # Scanning Remaining Files
        for filename in files_dict:
            full_path = os.path.join(dirpath, filename)
            files_dict[filename] = scan_file(
                full_path, magic_word, files_dict[filename])
        time.sleep(pollint)


def main(args):
    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now signal_handler will get called if OS sends
    # either of these to my process.
    start_time = datetime.datetime.now()
    logger.info(
        '\n'
        f'{"-"*40}\n'
        f'Process ID: {os.getpid()}\n'
        f'Running {__file__}...\n'
        f'Started: {start_time.isoformat()}\n'
        f'{"-"*40}\n'
    )

    parser = wparse.create_parser()
    args = parser.parse_args(args)
    logger.info(
        f"Searching in {args.watch} for {args.filter}"
        f" files with {args.search}")
    while not exit_flag:
        try:
            watch_dir(args.watch, args.search, args.filter, args.pollint)
            logger.debug("Watching directory...")
        except FileNotFoundError:
            logger.warning(args.watch + " does not exist!")
        except Exception:
            logger.exception("Unhandled Exception! You have work to do!")
        time.sleep(5.0)

    # Final exit point happens here
    # Logs a message that we are shutting down
    # Includes the overall uptime since program start.

    total_uptime = datetime.datetime.now() - start_time
    logger.info(
        '\n'
        f'{"-"*40}\n'
        f'Stopped {__file__}...\n'
        f'Total Uptime: {str(total_uptime)}\n'
        f'{"-"*40}\n'
    )


if __name__ == '__main__':
    main(sys.argv[1:])
