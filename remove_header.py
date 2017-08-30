# Removes old lanl.gov header code from markdown file

import os, sys

dr = './pages'

def rewrite_file(name, string_to_remove):
    print name.split('/')[-1]
    source_name = name[:-3] + '_temp.md'
    os.system('cp ' + name + ' ' + source_name)
    source_file = open(source_name, 'r')
    dest_name = name[:-3] + '_temp2.md'
    dest_file = open(dest_name, 'w')

    for line in source_file.readlines():
        if string_to_remove not in line:
            dest_file.write(line)
    
    os.system('cp ' + dest_name + ' ' + name)
    os.system('rm ' + source_name)
    os.system('rm ' + dest_name)

strings_to_remove = ['![](images/lagrit1.jpg){width="420" height="120"}', '![](images/lagrit2.jpg){width="180" height="120"}]',
                     '[]{#content}']

for string in strings_to_remove:
    for root, drs, fles in os.walk(dr):
        for fle in fles:
            if fle[-3:] == '.md':
                rewrite_file(os.path.join(root, fle), string)
