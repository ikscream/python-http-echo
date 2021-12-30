# Description

Just another safe-code http echo server written on ```Python```

## Build

My build env:
* _Fedora 34 (Linux fedora 5.13.6-200.fc34.x86_64 #1 SMP Wed Jul 28 15:31:21 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux)_
* _podman version 3.2.3_

```
podman build .
```

## Run


```
» podman run -e PORT=2000 --network host -e PORT=8000 --rm -d --name python-http-echo debugger0/python-http-echo:latest
» curl localhost:8000                                                                        
2021-12-30 09:12:50.122309: 127.0.0.1 GET /
```

### Environment

PORT - port to run (default: 8080)