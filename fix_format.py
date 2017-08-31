import os, sys, textwrap

def filter_file(infile_name, character):
    outfile_name = infile_name[:-3] + '_temp.md'
    with open(infile_name, 'r') as infile, open(outfile_name, 'w') as outfile:
	data = infile.read()
	data = data.replace(character, "")
	outfile.write(textwrap.dedent(data))

dr = '/home/nknapp/deknapp.github.io/pages/'

#for root, drs, fles in os.walk(dr):
#    for fle in fles:
#        if ".md" in fle and "temp" not in fle:
#            os.remove(os.path.join(root, fle))

for root, drs, fles in os.walk(dr):
    for fle in fles:
        if ".md" in fle and "temp" in fle:
            name = os.path.join(root, fle)
            os.remove(name)
