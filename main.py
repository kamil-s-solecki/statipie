#!/usr/bin/python3

from statipie.server import Server


def main():
    print("---- Running ----")

    server = Server(8080)
    server.run()


if __name__ == '__main__':
    main()
