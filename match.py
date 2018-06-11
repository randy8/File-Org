#!/usr/bin/env python
import re, os

path = r"."
main_dir = os.listdir(path)
log = open("log.txt", "w")
file_types = ['*.xlsx', '*.xls', '*.xlsm', '*.docx', '*.doc', '*.msg', '*.xlsb', '*.pdf', '*.zip']
file_type_sans_dot = [f.strip('*.') for f in file_types]
# print(file_type_sans_dot)

def search():
# ugly bruteforce not sure how else to go about it yet
	for sub_dir in main_dir: # working dir contains folders categorized by file type
		for i in file_type_sans_dot: # each file type's folder
			if os.path.exists(sub_dir):
				os.chdir("%s_files" % i) # e.g. cd into .\xlsx_files
				for file in os.listdir('.'):
					# is this necessary or does os module know it's current dir? or do you need '.' for it to know?
					sub_path = path + "\\" + "%s_files" % i
					# indendation error? how
					filepath = os.path.join(sub_path, file) # file = .\xlsx_files\files 
					text = open(filepath, "r")
					num_matches = 0
					keywords = "social" # might be better to split this in a new function and pass in from a .txt file
					matches = re.findall(r'[\w\.-]+@[\w\.-]+', keywords) # doesn't work for xlsx
					# TODO: figure out how to search 
					# iter_rows() might be of use
					# maybe just search for each unique file type? so group doc/docx, xlsb/xlsm/xls/xlsx, etc. possibly as helpers
					for line in text: # might work for doc due to compiler error for "matches"
						for word in matches: # regex 
							# matched = re.match(word, line): # search = pattern vs. match = start of string
						# if matched:   
							num_matches += 1
							log.write(filepath + "|" + line,) # write to file
							# redact = '*******' # obviously doesn't work (yet)
							# set line = redact
					text.close()

if __name__ == '__main__':
   search()