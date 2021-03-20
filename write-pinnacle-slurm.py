#! /usr/bin/env python3

# This script generates a pbs file for the AHPCC pinnacle cluster

# Define some variables
name = 'Trinity_assembly'
queue = 'comp06'
output = 'Trinity_'
node_num = 1
p_num = 32
time = 6 #in hours

print('#SBATCH -J', name)
print('#SBATCH --partition', queue)
print('#SBATCH -o', output + '%j.txt')
print('#SBATCH -e Trinity_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=aja@uark.edu')
print('#SBATCH --nodes='+ str(node_num))
print('#SBATCH --ntasks-per-node='+str(p_num))
print('#SBATCH --time=0'+str(time)+ ':00:00')
print()

print('export OMP_NUM_THREADS=32')
print()

# load required modules
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
print()

# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')
print()

# copy files from storage to scratch
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')