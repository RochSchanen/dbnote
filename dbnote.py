#!/usr/bin/python3
# file: dbnote.py
# created: 2021/01/14
# author: Roch Schanen

# learn how to build data base
# data are found in note files
# create data base storage
# add file to data base
# update data base
# rebuild data base from files

from os         import getcwd
from sys        import argv
from sys        import exit
from os.path    import isfile
from time       import strftime

# persist data   insert
# retrieve data  select (single)
# delete data    delete
# querry         where  (list)
# update                (keep ID)
# merge notes ?
# take the model of a library card
# allow to collect several library card in the same file ?

# default var file
csfDefault = \
f''' # file: .dbnote.var
     # content: variables for dbnote
     # created: {strftime('%Y%m%d')}
     repository = 
     author = Roch Schanen
     email = r.schanen@lancaster.ac.uk
'''

# locate system storage space
cwdPath = getcwd()
localPathParts = argv[0].split('/')
localPath = '/'.join(localPathParts[0:-1])
csfPath = [localPath, cwdPath][0] + "/.dbnote.var"

# create default file
if not isfile(csfPath):
    print(f'> create "{csfPath}"')
    fh = open(csfPath, 'w')
    fh.write(csfDefault.lstrip())
    fh.close()

# read var file
fh = open(csfPath, 'r')
varTxt = fh.read().splitlines()
fh.close()

# define internal variables
varDic = {
    'repository' : '',
    'author'     : '',
    'email'      : '',
    }

# collect vars
for l in varTxt:
    s = l.strip()
    if not l: continue 
    if l[0] == '#': continue
    if not '=' in l: continue
    var, val = l.split('=')
    if var.strip() in varDic.keys():
        varDic[var.strip()] = val.strip()

# command list
def _list():
    if len(argv):
        if argv[0] in varDic.keys():
            print(f'"{varDic[argv[0]]}"')
    else:
        for var, val in varDic.items():
            print(f'{var} = {val}')
    return

# parse command line
cmdList = {
    'list' : _list
}

if len(argv) > 1 :
    argv.pop(0)
    if argv[0] in cmdList.keys():
        cmdList[argv.pop(0)]()
        exit()

# diplay usage
print('usage:')
print('    > dbn <command> <arguments>')
print('available commands:')
print('    > dbn list')
print('        display all variables')

