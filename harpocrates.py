import os
import signal
import psutil

#Stop ignorant users from running this script without administrator privileges in windows
if os.name == 'nt':
    import ctypes
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run this script as administrator.")
        exit()

devmode = 1 #replaces BC with TaskMgr. Also replaces BCUA exe with dummy.exe in same folder as harpocrates.py
version_number = "0.1.0"
important_notes = "Beware: This is a pre-release version. It is not yet ready for production use."
print("Harpocrates v" + version_number)
print(important_notes)

if devmode == 1:
    print("Dev Mode Enabled")

def main_menu():
    #Selection Choices
    print("Please select an option:")
    print("1. BCUA Soft Kill")

    #Selection Input
    selection = input("Selection: ")

    if selection == "1":
        print("BCUA Soft Kill")
        print("Confirm? (Y/N)")
        confirm = input("Confirm: ")
        confirm=confirm.upper()
        if confirm == "Y":
            print("Soft Kill Confirmed")
            bcua_soft_kill()
        else :
            print("Soft Kill Cancelled")
            main_menu()
    else:
        print("Invalid Selection")
        main_menu()

def bcua_soft_kill():
    print("BCUA Soft Kill Started.")

    #kill BCUA
    if devmode == 1:
        process_name = "Taskmgr"
        exe_name = "dummy.exe"
    else:
        process_name = "BCUA"
        exe_name = "/path/to/BCUA.exe"
    pid = None
    if os.path.isfile(exe_name) == False:
        print("BCUA not found. Please ensure that BCUA is installed and that the tool has not already been used.")
        main_menu()

    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            break
    os.kill(pid, signal.SIGILL)
    
    os.rename(exe_name, "disabled.bluecoat.exe")
    print("BCUA Soft Kill Complete.")
    main_menu()



main_menu()

