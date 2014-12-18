#!/usr/bin/env python
#encoding=utf-8
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import os
import hashlib
import urllib2
def HttpResponse(whtml):
    f = file(os.path.split(os.path.realpath(__file__))[0]+"/"+whtml)
    contxtlist = f.readlines()  
    context = ''.join(contxtlist)  
    return context
httpheader = '''''\ 
HTTP/1.1 200 OK 
Context-Type: text/html 
Server: Python-slp version 1.0 
Context-Length: '''
class TestHTTPHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/dockerapi"):
            m = hashlib.md5()
            m.update(self.path)
            cache_filename = m.hexdigest()
            
            #// remove /dockerapi/
            substr = self.path[11:]
            data = urllib2.urlopen("http://192.168.21.4:4243/" + substr).readlines()
#             open(cache_filename, 'wb').writelines(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.writelines(data)
        else:
            self.send_response(200)
            self.send_header("Welcome", "Docker remote")       
            self.end_headers()
            self.wfile.writelines(HttpResponse(self.path))
def start_server():
    server_address = ('', 8000)
    http_server = HTTPServer(server_address, TestHTTPHandle)
    http_server.serve_forever()

if __name__ == '__main__':
    start_server()