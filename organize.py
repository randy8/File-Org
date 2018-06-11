#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, shutil, glob, zipfile

# Splits up the files by type and moves them to a new folder accordingly
def organize():
    file_types = ['*.xlsx', '*.xls', '*.xlsm', '*.docx', '*.doc', '*.msg', '*.xlsb', '*.pdf', '*.zip']
    file_type_sans_dot = [f.strip('*.') for f in file_types]
    print(file_type_sans_dot)
    src_dir = r"."
    for file in os.listdir(src_dir):
        for i in file_type_sans_dot:
            if file.endswith(i):
                print(file + " found")
                dest_dir = "%s_files" % i 
                src_full = src_dir+"\\"+file
                if not os.path.exists(dest_dir):
                    try:
                        os.mkdir(dest_dir)
                        shutil.move(src_full, dest_dir)
                    except OSError as e:
                        print("Error moving file: " + file) 
                else:
                    shutil.copy2(src_full, dest_dir)
                    os.chdir(src_dir)
                    os.remove(file)

def unzip():
    # ".\zip_files" doesn't work since it needs to match the path 
    # print(os.getcwd())
    zip_dir = os.getcwd() + r"\zip_files"

    if not os.path.exists(zip_dir):
        pass
    else:
        os.chdir(zip_dir) # cd to dir with files
        # files = os.listdir(src_dir)
        for filename in glob.glob(os.path.join(zip_dir, '*.zip')):
                print(filename + " extracted to " + zip_dir)
                name = os.path.splitext(os.path.basename(filename))[0] # nix the extension
                if not os.path.isdir(name):
                    try:
                        zip = zipfile.ZipFile(filename)
                        # os.mkdir(name) # this is made when organize() is called
                        zip.extractall(path=name)
                        # shutil.move(name, dest_dir) # move extracted files to dest
                        # os.rename isn't working possibly due to LifeRay Sync permissions?
                    except zipfile.BadZipfile as e:
                        print("Bad zip file: " + filename)
                        try:
                            os.remove(filename)
                        except OSError as e: 
                            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                                raise # re-raise exception if a different error occurred 

if __name__ == '__main__':
   organize()
   unzip()