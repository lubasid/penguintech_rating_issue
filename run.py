#!/usr/bin/python3

import os
import shutil
import csv



current_dir = os.getcwd()

acords_folder = os.path.join(current_dir, "acords")
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

	
	os.chdir(acords_folder)

	# csv_file_count = 1
	# count = 0
	# ids_per_csv = 10

	csv_file = open('acords.csv','w')

	for folder in os.listdir(acords_folder):
		current_folder =  os.path.join(acords_folder, folder)
		if os.path.isdir(current_folder):
			for file in os.listdir(current_folder):
				file_name = os.path.splitext(file)[0]
				output = (folder + "/" + file_name)
				csv_file.write(output + "\n")

	csv_file.close()



# Logic for payloads that pass or fail
# TODO: 
def process_files():

	os.chdir(acords_folder)
	folder = os.listdir(acords_folder)
	

	for file in folder:
		
		if (file.startswith("1")):
			shutil.move(file, fail_folder)

		elif (file.startswith("2")):
			shutil.move(file, pass_folder)

main()