#!/opt/local/bin/python3
#
# get_force.py
#
# python script to extract the SCF force for each step, find the lowest force step
# and produce a quick graph showing the change in force               
# to run the script type 
# python get_force.py input_file_name 
# NOTE you can close the graph by pressing "q" on keyboard
#
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
dir=os.getcwd()
#
# setup files to read
if len(sys.argv) == 1:
  print('to run the script please type: python get_force.py input_file_name')
  sys.exit()
else:
  infile=str(sys.argv[1])
  i_infile=infile.find('.log')
  if (i_infile == -1):
    base=infile
  else:
    base=infile[:i_infile]
#endif
  log_file=base+'.log'
  s='directory is '
  print('{0:}{1:}'.format(s,dir))
  s='input file is '
  print('{0:}{1:}'.format(s,log_file))
#close if

# open the file
f = open(log_file,'r')

# set some basic parameters
force=[]
new_force=[]
x_axis=[]
en_search_string='Maximum Force '

# read the if there is a first line, then read the file line by line
# if force is given split the line into array tmp and extract the force number
# and extract the force and store in an array
count=0
line=f.readline()
while line:
  line =f.readline()
#  print('{0:}'.format(line))
  if en_search_string in line:
    tmp=line.rstrip().split()
    if tmp[2] == '********':
      tmp[2]='0.5'
    force.append(float(tmp[2]))         
    count1=count+1
    print('{0:}{1:<3}{2:<.8f}'.format('step: ',count1,force[count]))
    count=count+1
# endif
#endwhile

total_steps=count
#print(total_steps)

# find the lowest force 
min_force=min(force)
min_index=force.index(min(force))
print('{0:}{1:}{2:}{3:}'.format('lowest force is step: ',min_index+1,'  force: ',min_force))

# convert to relative to lowest force 
# create x_axis which starts numbering at 1, remember python starts at zero
x=0
while x < total_steps :
  temp=(force[x] - min_force) 
  new_force.append(temp)
  x=x+1
  x_axis.append(x)
#endwhile

# plot the force 
plt.plot(x_axis,new_force,'b-')
plt.plot(x_axis,new_force,'bo')
plt.plot(min_index+1,new_force[min_index],'rs',markersize=8)
plt.ylabel('force')
plt.xlabel('step')
plt.show()

# close file
f.close()
#sys.exit()
#end
