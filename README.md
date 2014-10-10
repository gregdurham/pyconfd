pyconfd
========================

This client uses a yml file to config vars and templates. 

A sample yml is listed below:

```
---
vars:
    env:
        - name: NAME
    etcd:
        - cluster: "/servers/{{ name }}/cluster"

templates:
    - template01:
        source: template.txt.j2
        dest: /opt/template.txt
        vars:
            name: name
            cluster: cluster
```

There are two main sections, `vars` and `templates`.

Under `vars` is `env` and `etcd`. This describes where the variables will come from. 
In this case we are looking for the environment variable `NAME` and assigning it to 
`name`, we are then using this to populate a template where we want to use the `name` 
in the string. I.e. name being `host01` would create `/servers/host01/cluster`. 
We would then contact etcd with this path, and assign the variable to `cluster`. 

Under `templates` we have a template label in this case `template01`. Under the template
label, we have a source, which looks in the directory `/etc/py-confd/templates` for a 
templates by the name of `template.txt.j2`. We want to then place the rendered template
in `/opt/template.txt`. We are then populating this template with the variables listed in
the `vars` section. As you can see these names match the names in the above `vars` section.

A sample template.txt.j2:
```
{{ cluster }}
{{ name }}
```

If run from the source project:
`NAME=host01 pyconfd --config-file default.yaml --template-dir /etc/py-confd/templates/`

Possible options:
```
--template-dir: Path to the templates directory
--config-file: Path to the templates directory
--etcd-ip: IP address of etcd server default is 127.0.0.1
--etcd-port: Port of etcd server default is 4001
--noop: Run without modifying anything
```
