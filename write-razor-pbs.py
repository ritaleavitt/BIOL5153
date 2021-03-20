#! /usr/bin/env python3

# This script generates a pbs file for the AHPCC razor cluster

# define some variables
queue = 'onenode16core'
wall = 3 # This is in hours
name = 'test'
output = 'test'
node_num = 1
p_num = 1

# This section prints the headr/required info for the pbs script
print('#PBS -N', name) #job name
print('#PBS -q', queue) #which queue to use 
print('#PBS -j oe') #join the STDOUT and STDERR into a single file
print('#PBS -o', output + '$PBS_JOBID') #set the name of the job output file
print('#PBS -l nodes=' + str(node_num) + ':ppn='+ str(p_num)) #how many resources to ask for (nodes=num nodes), (ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') #set the wall time (default to 1 hr)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# load necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

#commands for this job
print("insert commands here")