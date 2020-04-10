# Dirwatcher

Note: A good portion of this README file was originally written by madarp. All credit and rights reserved.

## About

Dirwatcher is a long running program with signal handling and logging. It was created for the purpose of monitoring file changes in a given directory while also search for a special word within the given files in a dictionary

## Commands

Type the following in your console:

python dirwatcher.py [-h][-p pollint] [-f filter] 'search_word' 'directory_to_watch'

    pollint = the interval you wish to set for the directory to be checked.
    The default value is 1.0 second.

    filter = the extension of the files you want to search through in the directory.
    The default extension is for '.txt' files.

## Testing Program Operation

Test the dirwatcher program using TWO terminal windows. In the first window, start Dirwatcher with various sets of command line arguments. Open a second terminal window and navigate to the same directory where Dirwatcher is running, and try these procedures:

    Run Dirwatcher with non-existent directory -- Every polling interval, it should complain about the missing watch directory.
    Create the watched directory with mkdir -- Dirwatcher should stop complaining.
    Add an empty file with target extension to the watched directory -- Dirwatcher should report a new file added.
    Append some magic text to first line of the empty file -- Dirwatcher should report that some magic text was found on line 1, only once.
    Append a few other non-magic text lines to the file and then another line with two or more magic texts -- Dirwatcher should correctly report the line number just once (don't report previous line numbers)
    Add a file with non-magic extension and some magic text -- Dirwatcher should not report anything
    Delete the file containing the magic text -- Dirwatcher should report the file as removed, only once.
    Remove entire watched directory -- Dirwatcher should revert to complaining about a missing watch directory, every polling interval.

## Testing the Signal Handler

To test the OS signal handler part of Dirwatcher, send a SIGTERM to your program from a separate shell window.

    While Dirwatcher is running, open a new shell terminal.
    Find the process id (PID) of your running dirwatcher.  PID is the first column listed from the ps utility.
    Send a SIGTERM to your Dirwatcher PID
    Your signal handler within your python program should be called.  Your code should exit gracefully with a Goodbye message ...

Example: How to shutdown your program

piero@Piero-MBP: ~ $ ps aux | grep dirwatcher.py
48885 ttys000    0:00.80 python dirwatcher.py
49388 ttys002    0:00.00 grep dirwatcher.py
piero@Piero-MBP: ~ $ kill -s SIGTERM 48885

2018-08-31 11:36:29.510--\_\_**main**\_\_--WARNING [MainThread ]--Received SIGINT
2018-08-31 11:36:29.834--\_\_**main**\_\_-- INFO--[MainThread ]

---

    Stopped dirwatcher.py...
    Uptime was 0:33:39.316367

---
