import argparse


class Args:
    def __init__(self, directory, host, port):
        self.directory = directory
        self.host = host
        self.port = port


def parse_args():
    desc = 'Statipie – lightweight static files http server'
    parser = argparse.ArgumentParser(description=desc)
    dir_help = ('a directory with static files to be served '
                '(defaults to: example_site)')
    parser.add_argument('dir', type=str, nargs='?',
                        default='example_site', help=dir_help)
    parser.add_argument('--host', dest='host', default='127.0.0.1', type=str,
                        help='(default: 127.0.0.1)')
    parser.add_argument('--port', dest='port', default=8080, type=int,
                        help='(default: 8080)')

    args = parser.parse_args()
    return Args(directory=args.dir, host=args.host, port=args.port)
