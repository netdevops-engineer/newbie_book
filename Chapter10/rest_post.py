#! /usr/bin/env python
# coding:utf-8
import getpass
import requests
import json
import base64


if __name__ == '__main__':
    hostname = "172.20.1.12"
    port = 8080
    username = "lab"
    password = getpass.getpass()
    s = requests.Session()
    s.auth = (username, password)
    s.headers.update({"Content-Type": "applicaton/xml"})
    s.headers.update({"Accept": "applicaton/json"})
    URL = "http://%s:%d/rpc" %(hostname, port)

    payload = "<get-route-information/>"
    response = s.post(URL, data=payload)

    if response.ok:
        response_dict = json.loads(response.text)
        route_information = response_dict.get("route-information")[0]
        route_table = route_information.get("route-table")[0]
        rts = route_table.get("rt")
        for dest in rts:
            print(dest.get("rt-destination")[0].get("data"))

