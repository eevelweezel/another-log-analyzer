# Compare two logs & spit out interesting observations...
# Extract the names of the executing workflow objects
#
# Run a diff for stuff that executes in one log and not the other
# 
# Stuff that would make this more intersting: find errors, loops...?
# 
# 

# inputs... fix me, eventually.
"""
print('Logfile 1 and path:')
x = input()
print('Logfile 2 and path:')
y = input()
print('Specify a file name for output:')
z = input()
"""
print('Feed me, Seymour!')
x = '/home/eevel/test_data/tl2.txt'
y = '/home/eevel/test_data/tl1.txt'
z = '/home/eevel/test_data/tlo.txt'

log_output = open(z,'w')

def parse_log(a,b,c):
    """ Read the log, then construct a list of lists containing line #, type,
    and name of each executing object. 
    Need to make this tolerant of windows-style line endings """
    log = open(a, 'r')
    lines_in = list(log)
    for line in lines_in:
        if "Active Link:" in line and '\n' in line:
            b.append([c,line[line.index(': ')+2:line.index('- ')], log.tell(), 'Active Link'])
        elif "<FLTR>" in line and '\n' in line:
            b.append([c,line[line.index('Checking "')+10:line.index('" ')], lines_in.index(line), 'Filter'])
        elif "<SQL" in line and '\n' in line:
            b.append([c,line[line.index('*/')+2:line.index('\n')], lines_in.index(line), 'SQL'])
        elif "<API >" in line and '\n' in line:
            b.append([c,line[line.index('*/')+2:line.index('\n')], lines_in.index(line), 'API'])
        else: 
            pass
    return b


def set_builder(d,e,f):
    """ From results, construct a set of workflow object names """
    for line in d:
        if line[3] == e:
            f.add(line[3])
        else:
            pass
    return f


x_out = []
x_al = set()
x_fil = set()
x_sql = set()


parse_log(x,x_out,1)

set_builder(x_out,"Active Link",x_al)

set_builder(x_out,"Filter",x_fil)

set_builder(x_out,"SQL",x_sql)


y_out = []
y_al = set()
y_fil = set()
y_sql = set()

parse_log(y,y_out,2)

set_builder(y_out,"Active Link",y_al)

set_builder(y_out,"Filter",y_fil)

set_builder(y_out,"SQL",y_sql)


# try new test files... these are suspiciously null?

al_out = set(x_al ^ y_al)

fil_out = set(x_fil ^ y_fil)

sql_out = set(x_sql ^ y_sql)


log_output.write('Disjoint Active links:\n\n')

for line in al_out:
    log_output.write(str(line))

log_output.write('\n\n\n')  
  
log_output.write('Disjoint Filters:\n\n')

for line in fil_out:
    log_output.write(str(line))

log_output.write('\n\n\n')    

log_output.write('Disjoint SQL:\n\n')

for line in sql_out:
    log_output.write(str(line))

log_output.write('\n\n\n')    

log_output.write('Log 1 Workflow Actions:\n\n')

for line in x_out:
    log_output.write(str(line[2])+': '+line[1]+' ('+line[3]+')\n')

log_output.write('\n\n\n')

log_output.write('Log 2 Workflow Actions:\n\n')

for line in y_out:
    log_output.write(str(line[2])+': '+line[1]+' ('+line[3]+')\n')

log_output.write('\n\n\n')


