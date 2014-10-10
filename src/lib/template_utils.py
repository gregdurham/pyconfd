import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def build_template(template, vars_dict, template_dir):
    env = Environment(loader=FileSystemLoader(template_dir))
    populated_vars_dict = {}
    for t in template.keys():
        src = template[t].get('source')
        dst = template[t].get('dest')
        inputs = template[t].get('vars')
        try:
            src_template = env.get_template(src)
            for k,v in inputs.items():
                populated_vars_dict[k] = vars_dict.get(v)
    
            result = src_template.render(populated_vars_dict)
            return dst, result
        except TemplateNotFound, e:
            raise RuntimeError("Template %s not found in %s" % (src, template_dir))
        
def write_template(dst, content):
    try:
        fp = open(dst, 'w')
    except IOError:
        raise RuntimeError("Cannot open destination file: %s" % dst)
    else:
        fp.write(content)       
        fp.close()

    
