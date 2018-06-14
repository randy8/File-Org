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
- ``organize.py`` - Organizes files by file type and moves them to ``<filetype>_files/``. Zip files will be moved into ``zip_files/`` then unzipped into a new directory with the same title. Properly deals with overwriting directories/files
- ``is_locked.py`` - Checks to see if a file is locked by attempting to enter append mode
- ``match.py`` - Enters directory and attempts to search for keywords in provided file(s), logging all matches. Needs to be updated for more file types in order to replace any data

=====
Usage
=====
Run in the following order:: 

    py organize.py; py is_locked.py; py match.py
 
=====
Notes
=====
- Look into VBA to modify .xlsx files. 
- Getting all the libraries I needed was easy through `Anaconda <https://www.anaconda.com/download/>`_
- ``is_locked.py`` isn't as useful as I had thought since it doesn't actually tell you if the file is password-protected through the append mode check 
- User input for ``match.py`` would be better like ^F
