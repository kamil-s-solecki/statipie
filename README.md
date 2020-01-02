# statipie
## Lightweight http static files server in python

Project inspired by Gynvael's ["HTTP Server in 1h" livestream](https://www.youtube.com/watch?v=u5JQQrZDy4o). I use the same concept of starting a thread for each connection via [threading lib](https://docs.python.org/3.5/library/threading.html#module-threading).

### Important
This code is being written for educational purposes only. For security reasons it **should NOT be used** on any internet-exposed machine.

### Usage

```
./main.py [dir]
```

Serves files from `dir` at `127.0.0.1:8080`.

Uri `/` defaults to `/index.html`.

If no `dir` is passed as an argument, then serves `example_site`.  
