# Need to break out Active Links, Filters, SQL statements, and Errors
# Gen a list of these for each input
# Run a diff for stuff that executes in one log and not the other
# ... maybe allow comparison a block at a time?

# ActiveLink: CDB:EM-SetJournalDetails - Fri Jul 19 2013 10:55:00 AM
# note ": " and " -" denote start/end of name & line begins w/ "Active Link"


# set inputs
print('Logfile 1 and path:')
x = input()
print('Logfile 2 and path:')
y = input()
print('Specify a file name for output:')
z = input()

log_output = open(z,'w')

# loop through logs & parse into lists
def parse_this(a):
	lines_in[]
	log = open(a, 'r')
	for line in log:
		lines_x.append(log.readline())
	a.close()
	return lines_in

# gen a list for active link execution	
def active_links(lines_in):
	actl[]
	for line in lines_in:
		if line.startswith('Active Link',0,len(line))
			actl.append(line.tell()+' '+(line[line.index(':'):line.index('-')]))
	return actl		
			
# gen a list for filter execution	
def filters(lines_in):
	fltr[]
	for line in lines_in:
		if line.startswith('Filter',0,len(line))
			actl.append(line.tell()+' '+(line[line.index(':'):line.index('-')]))
	return fltr
			
# gen a list for SQL execution	
def sql(lines_in):
	sql_st[]
	for line in lines_in:
		if line.startswith('<SQL>',0,len(line))
			actl.append(line.tell()+' '+(line[line.index(':'):line.index('-')]))
	return sql_st

# concat the output into one string	
def concat(lines_in):
	log_out = ''
	for line in lines_in:
		log_out = log_out+item
	pickle.dump(log_out,log_output)
	return log_out

# process log & output to string
def process_log(d):
	active_links(d)
	filters(d)
	sql(d)
	concat(d)
	return d

# business starts here	
parse_this(x)	
process_log(lines_x)
parse_this(y)
process_log(lines_y)

# cleanup
log_output.close()
quit()	

