# Description

Just another safe-code http echo server written on ```Python```

## Build

My build env:
* **Fedora 34 (Linux fedora 5.13.6-200.fc34.x86_64 #1 SMP Wed Jul 28 15:31:21 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux)**
* **podman version 3.2.3**

```
podman build .
```

## Run

podman run --network host --name echo 

### Environment

PORT - port to run (default: 8080)