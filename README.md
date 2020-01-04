# statipie
Travis: [![Build Status](https://travis-ci.org/kamil-s-solecki/statipie.svg?branch=master)](https://travis-ci.org/kamil-s-solecki/statipie)
## Lightweight http static files server in python

Project inspired by Gynvael's ["HTTP Server in 1h" livestream](https://www.youtube.com/watch?v=u5JQQrZDy4o). I use the same concept of starting a thread for each connection via [threading lib](https://docs.python.org/3.5/library/threading.html#module-threading).

### Important
This code is being written for educational purposes only. For security reasons it **should NOT be used** on any internet-exposed machine.

### Usage

```
./main.py [-h] [--host HOST] [--port PORT] [dir]

dir              directory with static files to serve
                 (default: 'example_site')

-h, --help       show help message and exit
--host HOST      (default: '127.0.0.1')
--port PORT      (default: 8080)
```

Uri `/` defaults to `/index.html`.

If no `dir` is passed as an argument, then [example_site](example_site/) is being served.

### Encoding
Server assumes utf-8 encoding of all text/* and application/* files
