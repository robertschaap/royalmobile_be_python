from invoke import task

app = "server.py"
port = 4000
debug = True

@task
def start(c):
    c.run("FLASK_APP={app} FLASK_RUN_PORT={port} FLASK_DEBUG={debug} flask run".format(
        app = app,
        port = port,
        debug = int(debug),
    ))
