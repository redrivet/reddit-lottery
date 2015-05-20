import sys
import random
import argparse
import praw

from praw.helpers import flatten_tree


USER_AGENT = 'Thread-specific user lottery script by /u/redrivet'

def main(thread_id, include_author=False, sample_size=1):
    print('Logging in to Reddit...')
    r = praw.Reddit(USER_AGENT)

    try:
        if '/' in thread_id:
            # Looks like a URL
            thread = r.get_submission(url=thread_id)
        else:
            # Hopefully a thread identifier
            thread = r.get_submission(submission_id=thread_id)
    except Exception:
        print('Error while searching for a thread with url or id of "{}"\n{}'.format(
            thread_id, sys.exc_info()))
        return

    users = []
    if include_author:
        print('Including original thread author.')
        users.append(thread.author.name)

    users = users + [c.author.name for c in flatten_tree(thread.comments)]
    candidates = set(users)
    print('Found {} unique users in {} comments.'.format(len(candidates), len(users)))

    print('Randomly selecting {} winners...'.format(sample_size))
    winners = random.sample(candidates, sample_size)
    print('Chosen Winners:')
    for w in winners:
        print('/u/{}'.format(w))

    print('Done!')


def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('thread', metavar='URL_OR_ID', type=str,
        help='Url or thread id for the reddit thread.')
    parser.add_argument('--include-author', action='store_true',
        help='Include the thread\'s original author')
    parser.add_argument('-c', '--count', type=int, default=1)

    return parser


if __name__ == '__main__':
    parser = _get_parser()
    args = parser.parse_args()
    main(args.thread, args.include_author, args.count)

