#!/usr/bin/env python3
import sys

# 
# Stuff that would make this more intersting: find errors, loops...?
# 

def parse_log(a,b):
    
    """ 
    a = file input
    b = file output 
    
    Read the log, convert to universal line endings, then construct a list of 
    lists containing line #, type, and name of each object.   

    um... error handling...?

    """
    
    with open(a, 'rt+') as log:
        lines_in = list(log)
        for i in lines_in:
            if '\r\n' in i:
                l = i.replace('\r\n','\n')
                lines_in.insert(lines_in.index(i),l)
                lines_in.remove(i)
            else:
                pass
            continue
        for line in lines_in:
            check_exec = 'YAY! THING!'
            try:
                if 'ActiveLink:' in line:
                    if 'True' in lines_in[lines_in.index(line)+2]:
                        check_exec = '\n    true\n' 
                    else: 
                        check_exec = '\n    false\n'
                    b.append([line[line.index(': ')+2:line.index('- ')], lines_in.index(line)+1, 'ActiveLink', check_exec])
                elif '<FLTR>' in line:
                    if 'Passed' in lines_in[lines_in.index(line)+1]:
                        check_exec = '\n    true\n' 
                    else: 
                        check_exec = '\n    false\n'
                    b.append([line[line.index('Checking "')+10:line.index('" ')], lines_in.index(line)+1, '<FLTR>', check_exec])
                elif '<SQL >' in line and ('OK' not in line):
                    if 'OK' in lines_in[lines_in.index(line)+1]:
                        check_exec = '\n    true\n' 
                    else: 
                        check_exec = '\n    false\n'
                    b.append([line[line.index('*/')+2:(line.index('\n'))], lines_in.index(line)+1, '<SQL >', check_exec])
                elif '<API >' in line and ('\n' in line) and ('call' not in line) and ('OK' not in line):
                    if 'error' not in line:
                        check_exec = '\n    true\n' 
                    else: 
                        check_exec = '\n    false\n'
                    b.append([line[line.index('*/')+2:(line.index('\n'))], lines_in.index(line)+1, '<API >', check_exec])
                else: 
                    continue
            except ValueError: 
#                b.append(' - ')
                continue
        return b


def munchyMunch(l1,l2):
# Expects a list w/ two items - wf type & output list
# list1 = input 1
# list2 = input 2
    list1 = []
    list2 = []

    
# parse files    
    parse_log(l1, list1)
    parse_log(l2, list2)
    
# loop through wf types, compare logs 1 & 2  
# clear variables @ each iteration
    for i in wf:
    
        a = set()
        b = set()
        s_out = set()
        
        for j in list1:    
            try:
                if (j[2] == i):
                    a.add(j[0])
            except ValueError:
                continue
        for k in list2:
            try:
                if (k[2] == i):
                    b.add(k[0])
            except ValueError:
                continue    
        s_out = set(a ^ b)
        
#  output distinct lines (should happen X 4)
        log_output.write('Disjoint '+i+':\n\n')
        
        for line in s_out:
                log_output.write(str(line)+'\n')
        log_output.write('\n\n\n')  

# output stuff from file 1
    log_output.write('Log 1 Workflow Actions:\n\n') 
    
    for line in list1:
        log_output.write(str(line[1])+': '+line[0]+' ('+line[2]+') '+line[3]+'\n')
    
    log_output.write('\n\n\n')   
# output stuff from file 2
    log_output.write('Log 2 Workflow Actions:\n\n')    
    for line in list2:
        log_output.write(str(line[1])+': '+line[0]+' ('+line[2]+') '+line[3]+'\n')
    log_output.close()
    return                
    

# actual business...

with open(sys.argv[3],'wt+') as log_output:
    wf = ['ActiveLink', '<SQL >', '<FLTR>', '<API >']
    munchyMunch(sys.argv[1],sys.argv[2])
    print('Complete.  Check '+sys.argv[3]+' for output.')

