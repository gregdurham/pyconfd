import etcd
from jinja2 import Environment, FileSystemLoader

class EtcdBackend(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_values(self, etcd_vars, var):
        client = etcd.Client()
    
        for e in etcd_vars:
            try:
                path = Environment().from_string(e.values()[0]).render(var)
                var[e.keys()[0]] = client.read(path).value
            except KeyError, e:
                raise RuntimeError("Key not found: %s" % (path))
            except:
                raise