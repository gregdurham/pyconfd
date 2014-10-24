from os.path import normpath, basename

def getv(template_var):
	return template_var.get('value') 

def getk(template_var):
	return template_var.get('key') 

def getvs(template_vars):
	tempArr = []
	for i in template_vars:
		tempArr.append(i.get('value'))
	return tempArr

def base(key):
	return basename(normpath(key))