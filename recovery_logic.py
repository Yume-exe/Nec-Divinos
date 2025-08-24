import os
import ctypes
from tkinter import messagebox

def admin():
    """
    Checks if the program is running with administrator privileges.
    Returns True if it is, False otherwise.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def recover_files(drive, save_dir):
    """
    Scans a given drive for JPEG files and saves them to a specified directory.
    
    Args:
        drive (str): The letter of the drive to scan (e.g., "C").
        save_dir (str): The path to the directory to save the recovered files.

    Returns:
        int: The number of files successfully recovered.
    """
    try:
        drive_path = f"\\\\.\\{drive}:"
        with open(drive_path, "rb") as fileD:
            size = 512
            drec = False
            cntr = 0

            while True:
                byte = fileD.read(size)
                if not byte:
                    break

                # Find the JPEG start-of-image (SOI) marker
                found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
                if found >= 0:
                    drec = True
                    fileN = open(os.path.join(save_dir, f"recovered_{cntr}.jpg"), "wb")
                    fileN.write(byte[found:])
                    cntr += 1

                    while drec:
                        next_byte = fileD.read(size)
                        if not next_byte:
                            break

                        # Find the JPEG end-of-image (EOI) marker
                        bfind = next_byte.find(b'\xff\xd9')
                        if bfind >= 0:
                            fileN.write(next_byte[:bfind+2])
                            drec = False
                        else:
                            fileN.write(next_byte)
                    
                    fileN.close()

        return cntr

    except PermissionError:
        messagebox.showerror("Permission Denied", "Run the program as Administrator!")
        return 0
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return 0
