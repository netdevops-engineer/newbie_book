#!/usr/bin/env python

from flask import Flask, request
from sys import stdout


app = Flask(__name__)

@app.route("/", methods=["POST"])
def command():
    command = request.form["command"]
    if "65535:65282" not in command and "announce route" in command :
        command = command + " community 65535:65282"
    stdout.write("%s\n" %command)
    stdout.flush()

    return "%s\n" %command

if __name__ == "__main__":
    app.run()
