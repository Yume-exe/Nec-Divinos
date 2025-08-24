import os
import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes

def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def recover_files(drive, save_dir):
    try:
        drive = f"\\\\.\\{drive}:"
        fileD = open(drive, "rb")
        size = 512
        offs = 0
        drec = False
        cntr = 0

        while True:
            byte = fileD.read(size)
            if not byte:
                break

            found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
            if found >= 0:
                drec = True
                fileN = open(os.path.join(save_dir, f"recovered_{cntr}.jpg"), "wb")
                fileN.write(byte[found:])
                cntr += 1

                while drec:
                    byte = fileD.read(size)
                    if not byte:
                        break

                    bfind = byte.find(b'\xff\xd9') 
                    if bfind >= 0:
                        fileN.write(byte[:bfind+2])
                        drec = False
                    else:
                        fileN.write(byte)

                fileN.close()

        fileD.close()
        return cntr

    except PermissionError:
        messagebox.showerror("Permission Denied", "Run the program as Administrator!")
        return 0
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return 0

def start_recovery():
    selected_drive = drive_var.get()
    if not selected_drive:
        messagebox.showwarning("No Drive Selected", "Please select a drive to scan.")
        return

    save_dir = filedialog.askdirectory(title="Select Folder to Save Recovered Files")
    if not save_dir:
        return

    result = recover_files(selected_drive, save_dir)

    if result > 0:
        messagebox.showinfo("Recovery Complete", f"Recovered {result} images!\nSaved in {save_dir}")
    else:
        messagebox.showinfo("No Files Found", "No recoverable images found.")

root = tk.Tk()
root.title("Nec Divinos")
root.geometry("400x250")

tk.Label(root, text="Select Drive to Scan:").pack(pady=5)
drive_var = tk.StringVar()
drive_dropdown = tk.OptionMenu(root, drive_var, "C", "D", "E", "F")
drive_dropdown.pack()

recover_button = tk.Button(root, text="Start Recovery", command=start_recovery)
recover_button.pack(pady=20)

if not admin():
    messagebox.showwarning("Admin Rights Needed", "Please run as Administrator for raw disk access.")

root.mainloop()

