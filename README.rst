*****************
File Organization
*****************

Table of Contents:

.. contents::
    :local:
    :depth: 1
    :backlinks: none
    
================
Project Overview
================
- organize.py - Organizes files by file type and moves them to <filetype>_files/. Zip files will be moved into zip_files/ then unzipped into a new directory. Properly deals with overwriting directories/files. 
- is_locked.py - Checks to see if a file is locked by attempting to enter append mode
- match.py - Enters directory and attempts to search for keywords in provided file(s), logging all matches. Needs to be updated for more file types in order to replace any data

=====
Notes
=====
Look into VBA to modify .xlsx files. 
