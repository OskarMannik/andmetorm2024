## Build container

```
docker build -t flask-test .
```

## Run container

```
docker run -p 0.0.0.0:5001:5001 flask-test
```

## making request

IP is from `ipconfig` field `Wireless LAN adapter Wi-Fi:`

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/send-image -Method POST -OutFile output.png
```
