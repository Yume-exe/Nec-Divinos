import tkinter as tk
from tkinter import filedialog, messagebox
from recovery_logic import recover_files, admin

def start_recovery():
    """
    Handles the user interaction for starting the file recovery process.
    """
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
