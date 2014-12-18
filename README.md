dockerui-python
===============

python for dockerui. see https://github.com/crosbymichael/dockerui

1. 

enable ubuntu(1404) docker remote http api 
modify: /etc/default/docker.io
add:    DOCKER_OPTS='-H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock'
then:   sudo service docker.io restart

enable centos(6.5) docker remote http api 
modify: /etc/sysconfig/docker
add:    other_args="-H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock"
then:   service docker restart

2. modify server.py
data = urllib2.urlopen("http://192.168.21.4:4243/" + substr).readlines()

3.python server.py

4. open http://<ip>:8000/index.html
