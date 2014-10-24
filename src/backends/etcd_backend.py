import etcd
from jinja2 import Environment, FileSystemLoader

class EtcdBackend(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_values(self, etcd_vars, var):
        client = etcd.Client(host=self.host, port=self.port)
    
        for e in etcd_vars:
            try:
                path = Environment().from_string(e.values()[0]).render(var)
                result = client.read(path, recursive=True)
                if result.dir:
                    tempArr = []
                    for child in result.leaves:
                        tempVal = {'value': child.value, 'key': child.key}
                        tempArr.append(tempVal)
                    var[e.keys()[0]] = tempArr
                else:
                    var[e.keys()[0]] = {'value': result.value, 'key': result.key}
            except KeyError, e:
                raise RuntimeError("Key not found: %s" % (path))
            except:
                raise