# Flask com rabbitMQ

Video that I watched
<https://www.youtube.com/watch?v=p23J6NTDhEk>

## Executing RabbitMQ in container - developing

basic mode

```powershell
docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3
```

Logging the basic mode

```powershell
docker logs some-rabbit
```

Executing in advanced mode, with manage GUI in:
<http://localhost:15672>

```powershell
docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Executing in advanced mode, with manage GUI in localhost and setting access credentials:

```powershell
docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management

```

## Setting up the project

Commands.

``` powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
# python .\application.py runserver 5000

```

Init a lot of processes at same time

----

Script to add objects to queue

``` powershell
start-process python .\src\publisher.py
start-process python .\src\publisher.py
```

----

Script to treat objects from notify queue

``` powershell
start-process python .\src\notify.py
start-process python .\src\notify.py
```

----

Script to treat objects from report queue

``` powershell
start-process python .\src\report.py
start-process python .\src\report.py
start-process python .\src\report.py
```
