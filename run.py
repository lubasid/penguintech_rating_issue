#!/usr/bin/python3

import os
import shutil
import csv



current_dir = os.getcwd()

source_folder = os.path.join(current_dir, "source")
fail_folder = os.path.join(current_dir, "fail")
pass_folder = os.path.join(current_dir, "pass")
results_folder = os.path.join(current_dir, "results")



def main():

	create_folders()
	create_csv()
	# process_files()


# Create pass/fail/results folders if they don't exist
def create_folders():
	if not (os.path.isdir(fail_folder)):
		os.makedirs(fail_folder)
		
	if  not (os.path.isdir(pass_folder)):
		os.makedirs(pass_folder)

	if  not (os.path.isdir(results_folder)):
		os.makedirs(results_folder)



	
# Create csv files from xml file names

# NOTE: In a .csv leading zeros in a number are removed. 
# In a .txt file leading zeros are present. 
def create_csv():

	input_folder = os.listdir(source_folder)
	os.chdir(results_folder)

	csv_file_count = 1
	count = 0
	ids_per_csv = 10

	f = open(str(csv_file_count) + '.csv','w')

	for file in input_folder:
		file_name = os.path.splitext(file)[0]

		if count < ids_per_csv:
			f.write(file_name+'\n')
			count = count +1
		if count == ids_per_csv:
			f.close()
			csv_file_count += 1
			f = open(str(csv_file_count) + '.csv','w')
			count = 0

	f.close()



# Logic for payloads that pass or fail
# TODO: 
def process_files():

	os.chdir(source_folder)
	folder = os.listdir(source_folder)
	

	for file in folder:
		
		if (file.startswith("1")):
			shutil.move(file, fail_folder)

		elif (file.startswith("2")):
			shutil.move(file, pass_folder)

main()