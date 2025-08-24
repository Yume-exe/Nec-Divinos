# Nec-Divinos - JPG File Recovery Tool

This repository contains a simpe Pytho script for recovring deleted JPG files from the disk. This script provides a GUI for drive selection making the program feel more interactive. The tool works by scaning the raw data of a disk partition for the specific byte squences that mark the beinning and end of a JPG file.

Features:
 1. GUI: easy interfact built with tkinter.
 2. Targeted Recovery: specifically designed to find and recover JPG image files.
 3. Disk Scanning: capable of scanning a selected disk partiion.

Prerequisties:
 1. Pythoon 3.x
 2. Administrator privileges on Windows machine to access the raw disk data.

How to run:
 1. Save the code as a python file (both .py files).
 2. Open command prompt with administrator permissions.
 3. Navigate to the directory where you want your file retreieved.
 4. Run the script. The time taken for it to complete the retreival depends on how much JPG files were deleted. I experienced a few hours on my run but it can vary from user to user.

This tool is a basic example of file carving. It may not recover all deleted files and therecovered images may be corrupted or incomplete. The success of the recovery depends on various factos, including how much data has been overwritten since the files were deleted.

Tank you for reading
