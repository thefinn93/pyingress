#!/usr/bin/env python
import requests
import json
import os

class Ingress:
    def __init__(self, cookiedata=None, https=False):
        self.cookies = {}
        if cookiedata is None:
            try:
                cookiedata = open("cookies.txt").read()
            except IOError:
                pass
        if cookiedata is None:
            cookiedata = raw_input("Looks like we're missing some cookie data, could you dump it here? ")
        for cookie in cookiedata.split(";"):
            key,value = cookie.split("=",1)
            self.cookies[key.strip()] = value.strip()
        self.https = https
        self.url = "://www.ingress.com/rpc/"
    
    def rpc(self, data):
        if type(data) == type(str()):
            data = json.loads(data)
        url = "https" + self.url
        if not self.https:
            url = "http" + self.url
        url += data['method']
        
        result = requests.post(url, cookies=self.cookies,
            headers={"x-csrftoken": self.cookies["csrftoken"]},
            data=json.dumps(data))
        return result.json()
        
