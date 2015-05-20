reddit-lottery
==============

Simple thread-based lottery for reddit.  Given a single reddit thread, the script finds the unique set of all users who have commented on the thread and selects winners at random.  Options are provided for including the OP in the lottery and for specifying a number of winners.

Usage
-----

    usage: lottery.py [-h] [--include-author] [-c COUNT] URL_OR_ID

    positional arguments:
      URL_OR_ID             Url or thread id for the reddit thread.

    optional arguments:
      -h, --help            show this help message and exit
      --include-author      Include the thread's original author
      -c COUNT, --count COUNT

Requirements
------------

* Python 3.x
* praw - Reddit client library

Known Issues
------------

* Some of the modules used by praw issue warning messages due to underlying sockets not being closed properly.  These can safely be ignored.
