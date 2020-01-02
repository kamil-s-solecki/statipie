#!/usr/bin/python3

import sys
from statipie.server import Server
from statipie.server import ServerConfig
from statipie.response import ResponseGenerator
from statipie.statics_dir import StaticsDir


def create_server():
    try:
        statics_dir_path = sys.argv[1]
    except IndexError:
        statics_dir_path = 'example_site'

    config = ServerConfig(port=8080)
    response_generator = ResponseGenerator(StaticsDir(statics_dir_path))
    return Server(config, response_generator)


def main():
    print("---- Running ----")
    server = create_server()
    server.run()


if __name__ == '__main__':
    main()
