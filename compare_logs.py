# Read a log into a list
# Extract the names of the executing workflow objects
#
# Eventually, process two logs
#
# Run a diff for stuff that executes in one log and not the other
# 
# Write the output to a separate file
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
x = '/home/eevel/test_data/tl3.txt'
z = '/home/eevel/test_data/tlo.txt'

log_output = open(z,'w')

def parse_log(a,b):
    """ Read the log, then construct a list of lists containing line #, type,
    and name of each executing object """
    log = open(a, 'r')
    lines_in = list(log)
    for line in lines_in:
        if "Active Link:" in line and '\n' in line:
            b.append([line[line.index(': ')+2:line.index('- ')], log.tell(), 'Active Link'])
        elif "<FLTR>" in line and '\n' in line:
            b.append([line[line.index('Checking \"')+10:line.index('\" ')], lines_in.index(line), 'Filter'])
        elif "<SQL" in line and '\n' in line:
            b.append([line[line.index('*/')+2:line.index('\n')], lines_in.index(line), 'SQL'])
        elif "<API >" in line and '\n' in line:
            b.append([line[line.index('*/')+2:line.index('\n')], lines_in.index(line), 'API'])
        else: 
            pass
    return b

x_out = []
parse_log(x,x_out)

for line in x_out:
    log_output.write(str(line[1])+': '+line[0]+' ('+line[2]+')\n')

