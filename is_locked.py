#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, time, glob

def is_locked(filepath):
    # checks if a file is locked by opening it in append mode
    # a file is locked when an exception is thrown
    locked = None
    file_object = None
    if os.path.exists(filepath):
        try:
            print("Attempting to open %s." % filepath)
            buffer_size = 8 # read first 8 (arbitrary value) chars
            # if append mode is accessible, the file is unencrypted
            file_object = open(filepath, 'a', buffer_size)
            if file_object:
                print("%s is not locked." % filepath)
                locked = False
        except IOError as err:
            print("The following file is locked: %s" % filepath)
            locked = True
        finally:
            if file_object:
                file_object.close()
                print("%s closed." % filepath)
    else:
        print("%s not found." % filepath)
    return locked

# determines if files are ready to be checked
def wait_for_files(filepaths):
    wait_time = 5
    for filepath in filepaths:
        while not os.path.exists(filepath):
            print("%s hasn't arrived. Waiting %s seconds." % (filepath, wait_time))
            time.sleep(wait_time)
        locked_files = []
        while is_locked(filepath):
            print("%s is currently in use. Waiting %s seconds." % (filepath, wait_time))
            time.sleep(wait_time)
            locked_files.extend(filepath)
    print(locked_files) # doesn't recognize excel as encrypted

# creates a list of file (names) based on file types then joins the full path as a string literal in a new list
def get_file_dirs():
    list_of_files = [] # creates list to be populated 
    file_types = ('*.xlsx', '*.xls', '*.xlsm', '*.docx', '*.doc', '*.msg', '*.xlsb', '*.pdf', '*.zip') # tuple of filetypes
    for files in file_types: # account for other file types
        list_of_files.extend(glob.glob(files)) 
    # print(list_of_files)
    new_list = [os.path.join('.', file) for file in list_of_files]
    print(new_list, "\n", "############################## Starting lock check... ##############################")
    return wait_for_files(new_list)

# Test
if __name__ == '__main__':
    # files = [r"dirs"]
    get_file_dirs()
    # print(wait_for_files(get_file_dirs()))
