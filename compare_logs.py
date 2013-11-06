# Compare two logs & spit out interesting observations...
# Extract the names of the executing workflow objects
#
# Run a diff for stuff that executes in one log and not the other
# 
# Stuff that would make this more intersting: find errors, loops...?
# 
# 


# log 1 input
print('Logfile 1 and path:')
x = input()

# log 2 input
print('Logfile 2 and path:')
y = input()

# output file
print('Specify a file name for output:')
z = input()
"""


# junk for testing only
print('Feed me, Seymour!')
x = '/home/eevel/test_data/tl2.txt'
y = '/home/eevel/test_data/tl1.txt'
z = '/home/eevel/test_data/tlo.txt'
"""
log_output = open(z,'w')

wf = ['ActiveLink', '<SQL >', '<FLTR>', '<API >']


def parse_log(a,b):
    
    """ 
    a = file input
    b = file output
    c = integer that indicated the source file...? I think C can go away. 
    
    Read the log, then construct a list of lists containing line #, type,
    and name of each executing object. 
    Need to make this tolerant of windows-style line endings 

    ... There's GOT to be a cleaner way to parse this stuff.  

    """
    
    log = open(a, 'r')
    lines_in = list(log)
    for line in lines_in:
        if "ActiveLink:" in line and '\n' in line:
            b.append([line[line.index(': ')+2:line.index('- ')], log.tell(), 'ActiveLink'])
        elif "<FLTR>" in line and '\n' in line:
            b.append([line[line.index('Checking "')+10:line.index('" ')], lines_in.index(line), '<FLTR>'])
        elif "<SQL >" in line and '\n' in line:
            b.append([line[line.index('*/')+2:line.index('\n')], lines_in.index(line), '<SQL >'])
        elif "<API >" in line and '\n' in line:
            b.append([line[line.index('*/')+2:line.index('\n')], lines_in.index(line), '<API >'])
        else: 
            pass
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
            if (j[2] == i):
                a.add(j[0])

        for k in list2:
            if (k[2] == i):
                b.add(k[0])
                
        s_out = set(a ^ b)
        
#  output distinct lines (should happen X 4)
        log_output.write('Disjoint '+i+':\n\n')
        
        for line in s_out:
                log_output.write(str(line))
                log_output.write('\n\n\n')  

# output stuff from file 1
    log_output.write('Log 1 Workflow Actions:\n\n') 
    
    for line in list1:
        log_output.write(str(line[1])+': '+line[0]+' ('+line[2]+')\n')

# output stuff from file 2
    log_output.write('Log 2 Workflow Actions:\n\n')    
    for line in list2:
        log_output.write(str(line[1])+': '+line[0]+' ('+line[2]+')\n')
    log_output.close()
    return                
    

# actual business...
munchyMunch(x,y)

print('Complete.  Check '+z+' for output.')

