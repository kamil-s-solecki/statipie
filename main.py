#!/usr/bin/python3

from statipie.server import Server
from statipie.server import ServerConfig
from statipie.response import ResponseGenerator
from statipie.statics_dir import StaticsDir
from util.args import parse_args


def create_server(args):

    config = ServerConfig(host=args.host, port=args.port)
    response_generator = ResponseGenerator(StaticsDir(args.directory))
    return Server(config, response_generator)


def main():
    args = parse_args()
    server = create_server(args)
    print("---- Running ----")
    print("\n  http://{}:{}".format(args.host, args.port))
    server.run()


if __name__ == '__main__':
    main()
