import os
import signal
import psutil

#Stop ignorant users from running this script without administrator privileges in windows
if os.name == 'nt':
    import ctypes
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run this script as administrator.")
        exit()

devmode = 0 #replaces BC with TaskMgr
version_number = "0.1.0"
important_notes = "Beware: This is a pre-release version. It is not yet ready for production use."
print("Harpocrates v" + version_number)
print(important_notes)

def main_menu():
    #Selection Choices
    print("Please select an option:")
    print("1. BCUA Soft Kill")
    print("2. BCUA Hard Kill")

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
    elif selection == "2":
        print("BCUA Hard Kill")
        print("Confirm? (Y/N)")
        confirm = input("Confirm: ")
        confirm=confirm.upper()
        if confirm == "Y":
            print("Hard Kill Confirmed")
        else :
            print("Hard Kill Cancelled")
            main_menu()

def bcua_soft_kill():
    print("BCUA Soft Kill Started.")

    if devmode == 1:
        process_name = "Taskmgr"
    else:
        process_name = "BCUA"
    pid = None

    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            break
    os.kill(pid, signal.SIGILL)

main_menu()

