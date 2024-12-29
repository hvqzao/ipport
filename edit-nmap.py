#!/usr/bin/env python
'''
creates _edit file based on .nmap prepended IP to each port line, i.e.:
22/tcp open  ssh     OpenSSH

is converted to:
# 10.32.1.5:22/tcp open  ssh     OpenSSH
'''
import sys
p = list(filter(lambda x: x[:2] != '--', sys.argv[1:])) # params
if len(p) < 1:
    sys.stderr.write('Usage: '+sys.argv[0]+' <in-file1> [in-file2] ...\n')
    sys.exit(1)
o = '_edit.nmap' # omit pattern
o_len = len(o)
s = 'Nmap scan report for ' # search pattern
s_len = len(s)

def target(t):
    if t[-1] == ')':
        t = t[t.rindex('(')+1:-1]
    return t

for path in p:
    if path[-o_len:] == o:
        # do not create _edit_edit.nmap etc (skip silently)
        continue
    # get directory
    if '/' in path:
        dirname = path[:path.rindex('/')+1]
        filename = path[path.rindex('/')+1:]
    else:
        dirname = ''
        filename = path
    # insert _edit into save_as filename
    if '.' in filename:
        index = filename.rindex('.')
        save_as = '{}{}_edit{}'.format(dirname, filename[:index], filename[index:])
        del index
    else:
        save_as = '{}{}_edit'.format(dirname, filename)
    c = filter(lambda x: x, open(path).read().strip().replace('\r','\n').split('\n')) # file contents
    t = map(lambda x: x[s_len:], filter(lambda x: x[:s_len] == s, c)) # target(s)
    if not len(t):
        sys.stderr.write('{} skipped.\n'.format(filename))
        continue
    else:
        t = target(t[0])
    import re
    c[0] = '# {}'.format(c[0])
    with open(save_as,'w') as f:
        for i in c:
            if i[:s_len] == s:
                t = target(i[s_len:])
        f.write('{}\n'.format(re.sub(r'^([0-9]+)/', r'# {}:\1/'.format(t), i)))
    sys.stderr.write('{} saved.\n'.format(save_as))
