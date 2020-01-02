#!/usr/bin/python3

from statipie.server import Server
from statipie.server import ServerConfig
from statipie.response import ResponseGenerator


def main():
    print("---- Running ----")

    config = ServerConfig(port=8080)
    response_generator = ResponseGenerator()
    server = Server(config, response_generator)
    server.run()


if __name__ == '__main__':
    main()
