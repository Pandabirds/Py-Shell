import os
import time
from datetime import datetime
import winsound
import threading
import shutil
os.system("cls")

if __name__ == "__main__":
    # v These are ANSI color codes, this one makes all the text bright yellow.
    print("\u001b[33;1m")
    print("Py-Shell [Experimental]")

def indexists(list_input, index: int) -> bool:
    """Returns a boolean based off of whether or not the inputted [index] exists in [list_input]."""
    return index <= len(list_input) - 1

def is_float(s: str) -> bool:
    """Returns a boolean based off of whether or not the inputted string [s] can be reprsented as a float."""
    try: 
        float(s)
        return True
    except ValueError:
        return False

def is_int(s: str) -> bool:
    """Returns a boolean based off of whether or not the inputted string [s] can be reprsented as a float."""
    try: 
        int(s)
        return True
    except ValueError:
        return False

def printp(msg: str, layers: int):
    """
    Small function to make printing indented and correct outputs easier.
    It prints [layers] amount of four spaces, and then prints string with no automated newline.
    """
    print(ic(layers), msg, end = "")

def ic(layers: int) -> str:
    string = ""
    for _ in range(layers):
        string += "    "
    return string

def alarm_thread_function(time_until: int):
    time.sleep(time_until * 60)
    winsound.Beep(1000, 5000)
    return 0

def alarm(la: int) -> int:
    """pOS Alarm System"""
    printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
    
    time_until = ""
    while not is_float(time_until):
        printp("Enter Minutes Until Alarm Starts: ", la)
        time_until = input()
        if time_until == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            quit()
        if time_until == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    thread = threading.Thread(target=alarm_thread_function, args=([float(time_until)]), daemon=True)
    thread.start()
    
    printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
    return 0

def binary(la: int) -> int:
    """pOS Bit Manipulator"""
    printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
    num = ""
    while not is_int(num):
        printp("Enter Number (decimal): ", la)
        num = input()
        if num == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            quit()
        if num == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    num = int(num)
    while True:
        try:
            printp(f"{bin(num)}; {num}; {hex(num)}\n", la + 1)
            printp(":: ", la)
            cmds = input().lower().split("; ")
            if cmds[0] == "exit":
                printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
                return 0
            if cmds[0] == "quit":
                printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
                print("\u001b[0m")
                quit(0)
            if cmds[0] == "not":
                num = ~num
            if cmds[0] == "get":
                printp(str(1 if num & (0b1 << int(cmds[1])) != 0 else 0) + "\n", la + 1)
            if cmds[0] == "intersect":
                num &= int(cmds[1])
            if cmds[0] == "lshift":
                num = num << int(cmds[1])
            if cmds[0] == "overlap":
                num |= int(cmds[1])
            if cmds[0] == "rshift":
                num = num >> int(cmds[1])
            if cmds[0] == "set":
                num |= (1 << int(cmds[1]))
            if cmds[0] == "setnum":
                num = float(cmds[1])
            if cmds[0] == "toggle":
                num ^= (1 << int(cmds[1]))
            if cmds[0] == "unset":
                num &= ~(1 << int(cmds[1]))
        except Exception:
            pass

        
    printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
    return 1

def calculator(la: int) -> int:
    """pOS Calculator"""
    printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
    num = ""
    while not is_float(num):
        printp("Enter Number: ", la)
        num = input()
        if num == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            quit()
        if num == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    num = float(num)
    while True:
        printp(f"{num}\n", la + 1)
        printp(":: ", la)
        cmds = input().lower().split("; ")
        if cmds[0] == "exit":
            printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
            return 0
        if cmds[0] == "quit":
            printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            quit(0)
        try:
            if cmds[0] == "add":
                num += float(cmds[1])
            if cmds[0] == "div" and cmds[1] != "0":
                num /= float(cmds[1])
            if cmds[0] == "mod" and cmds[1] != "0":
                num = num % float(cmds[1])
            if cmds[0] == "mul":
                num *= float(cmds[1])
            if cmds[0] == "pow":
                num **= float(cmds[1])
            if cmds[0] == "set":
                num = float(cmds[1])
            if cmds[0] == "sub":
                num -= float(cmds[1])
        except Exception:
            pass
    
    printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
    return 1

def fete(la: int) -> int:
    """pOS File Explorer and Text Editor."""
    try:
        printp("\u001b[7m-F-I-L-E-E-X-P-L-O-R-E-R-&-T-E-X-T-E-D-I-T-O-R-\u001b[0m\u001b[33;1m\n", la)
        while True:
            current_path = os.getcwd()
            current_directory = os.listdir()
            printp(current_path + ":: ", la)
            cmds = input().lower().split("; ")
            if cmds[0] == "exit":
                printp("\u001b[7m-F-I-L-E-E-X-P-L-O-R-E-R-&-T-E-X-T-E-D-I-T-O-R-\u001b[0m\u001b[33;1m\n", la)
                return 0
            if cmds[0] == "quit":
                printp("\u001b[7m-F-I-L-E-E-X-P-L-O-R-E-R-&-T-E-X-T-E-D-I-T-O-R-\u001b[0m\u001b[33;1m\n", la)
                print("\u001b[0m")
                quit(0)
            if cmds[0] == "chdir" or cmds[0] == "cd":
                if cmds[1] == "..":
                    os.chdir(os.path.join(current_path, os.pardir))
                elif os.path.exists(current_path + "\\" + cmds[1]) and os.path.isdir(current_path + "\\" + cmds[1]):
                    os.chdir(current_path + "\\" + cmds[1])
                else:
                    os.chdir(cmds[1])
            if cmds[0] == "copy":
                if os.path.exists(current_path + "\\" + cmds[1]):
                    
                    if os.path.exists(current_path + "\\" + cmds[2]):
                        shutil.copy(current_path + "\\" + cmds[1], current_path + "\\" + cmds[2])
                    
                    if (not os.path.exists(current_path + "\\" + cmds[2])) and os.path.exists(cmds[2]):
                        shutil.copy(current_path + "\\" + cmds[1], cmds[2])
                if (not os.path.exists(current_path + "\\" + cmds[1])) and os.path.exists(cmds[1]):
                    if os.path.exists(current_path + "\\" + cmds[2]):
                        shutil.copy(current_path + "\\" + cmds[1], current_path + "\\" + cmds[2])
                    
                    if (not os.path.exists(current_path + "\\" + cmds[2])) and os.path.exists(cmds[2]):
                        shutil.copy(current_path + "\\" + cmds[1], cmds[2])
            if cmds[0] == "createdirectory" or cmds[0] == "createdir" or cmds[0] == "mkdir":
                os.mkdir(current_path + "\\" + cmds[1])
            if cmds[0] == "createfile":
                created_file = open(cmds[1], "w")
                created_file.close()
            if cmds[0] == "del" or cmds[0] == "delete":
                if os.path.exists(current_path + "\\" + cmds[1]):
                    if os.path.isdir(current_path + "\\" + cmds[1]):
                        shutil.rmtree(current_path + "\\" + cmds[1])
                    if os.path.isfile(current_path + "\\" + cmds[1]):
                        os.remove(current_path + "\\" + cmds[1])
                if (not os.path.exists(current_path + "\\" + cmds[1]) and os.path.exists(cmds[1])):
                    if os.path.isdir(cmds[1]):
                        shutil.rmtree(cmds[1])
                    if os.path.isfile(cmds[1]):
                        os.remove(cmds[1])
            if cmds[0] == "dir" or cmds[0] == "listdir":
                printp(f"Directory of {current_path}\n", la)
                for item in current_directory:
                    type_of_item = "DIR" if os.path.isdir(current_path + "\\" + item) else "FILE"
                    printp(f"....\"{item}\"    {type_of_item}\n", la + 1)
            if cmds[0] == "move":
                if os.path.exists(current_path + "\\" + cmds[1]):
                    
                    if os.path.exists(current_path + "\\" + cmds[2]):
                        shutil.move(current_path + "\\" + cmds[1], current_path + "\\" + cmds[2])
                    
                    if (not os.path.exists(current_path + "\\" + cmds[2])) and os.path.exists(cmds[2]):
                        shutil.move(current_path + "\\" + cmds[1], cmds[2])
                if (not os.path.exists(current_path + "\\" + cmds[1])) and os.path.exists(cmds[1]):
                    if os.path.exists(current_path + "\\" + cmds[2]):
                        shutil.move(current_path + "\\" + cmds[1], current_path + "\\" + cmds[2])

                    if (not os.path.exists(current_path + "\\" + cmds[2])) and os.path.exists(cmds[2]):
                        shutil.move(current_path + "\\" + cmds[1], cmds[2])
            if cmds[0] == "read" and os.path.isfile(current_path + "\\" + cmds[1]) and os.path.exists(current_path + "\\" + cmds[1]):
                with open(cmds[1], "r") as target_file:
                    printp(f"CONTENTS OF {cmds[1]}:\n", la)
                    contents = target_file.readlines()
                    highest_digits = len(str(len(contents)))
                    print("\n")
                    for i, content in enumerate(contents):
                        num_of_spaces = len(str(i)) - highest_digits
                        output = ""
                        output += str(i)
                        for _ in range(num_of_spaces):
                            output += " "
                        output += "|"
                        output += content
                        print(output, end = "")
                    print("\n")
            if cmds[0] == "run":
                os.system("python -u " + current_path + "\\" + cmds[1])
            if cmds[0] == "write" and os.path.isfile(current_path + "\\" + cmds[1]) and os.path.exists(current_path + "\\" + cmds[1]):
                if os.path.getsize(current_path + "\\" + cmds[1]) > 0:
                    contents = []
                    with open(cmds[1], "r") as target_file_read:
                        contents = target_file_read.readlines()
                        contents[int(cmds[2])] = cmds[3]
                    with open(cmds[1], "w") as target_file_write:
                        target_file_write.writelines(contents)
                if os.path.getsize(current_path + "\\" + cmds[1]) <= 0:
                    with open(cmds[1], "w") as target_file_write:
                        target_file_write.writelines(cmds[3])
            
        return 0
        printp("\u001b[7m-F-I-L-E-E-X-P-L-O-R-E-R-&-T-E-X-T-E-D-I-T-O-R-\u001b[0m\u001b[33;1m\n", la)
    except Exception:
        pass

def help(cmds, la: int) -> int:
    """pOS Help Menu"""
    printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
    try:
        if cmds[1] == "alarm":
            printp("Alarm : Lets you set an alarm that goes off after a set time.\n\n", la)
            
            printp("\"Enter Minutes Until Alarm Starts: [minutes]\" : Sets the alarm to go off in [minutes] (accepts decimals).\n", la)

            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0
        
        if cmds[1] == "binary":
            printp("Binary : Lets you do bitwise operations on a number in binary.\n\n", la)
            
            printp("get; [n] : Gets the [n]th bit of the current number.\n", la)
            printp("intersect; [n] : Set the current number to be a binary number defined by all the spots where the current number has a set bit at the same place as [n].\n", la)
            printp("lshift; [n] : Shift the current number left [n] times.\n", la)
            printp("overlap; [n] : Set the current number to be a binary number defined by all the spots where there is a set bit in either the current number or [n].\n", la)
            printp("rshift; [n] : Shift the current number right [n] times.\n", la)
            printp("set; [n] : Sets the [n]th bit of the current number.\n", la)
            printp("setnum; [n] : Sets num to [n]\n", la)
            printp("toggle; [n] : Toggles the [n]th bit of the current number.\n", la)
            printp("unset; [n] : Unsets the [n]th bit of the current number.\n", la)

            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0
        
        if cmds[1] == "calc" or cmds[1] == "calculator":
            printp("Calculator : Basic calculator for basic operations.\n\n", la)
            
            printp("add; [n] : Adds [n] to the current number.\n", la)
            printp("div; [n] : Divides the current number by [n].\n", la)
            printp("mod; [n] : Sets the current number to be the current number modulus [n].\n", la)
            printp("mul; [n] : Multiplies the current number by [n].\n",la)
            printp("pow; [n] : Sets the current number to be the current number to the power of [n].\n")
            printp("set; [n] : Sets the current number to [n].\n", la)
            printp("sub; [n] : Subtracts [n] from the current number.\n", la)
            
            printp("\nCalculator is also usable in one line.\n", la)
            printp("calculator; [n1]; [o], [n2] : Uses [o] on [n1] and [n2].\n", la)
            printp("List of Operations for One-Line Calculations:\n", la)
            printp("+ : Addition\n", la + 1)
            printp("/ : Division\n", la + 1)
            printp("% : Modulus\n", la + 1)
            printp("* : Multiplication\n", la + 1)
            printp("^ : Exponentiation\n", la + 1)
            printp("- : Subtraction\n", la + 1)
            
            return 0
        
        if cmds[1] == "fete" or cmds[1] == "file" or cmds[1] == "files":
            printp("FETE : File Explorer and Text Editor.\n\n", la)
            
            printp("cd; [path]; [dir] : Changes the current directory to: A. [dir] itself, B. A folder named [dir] in the current directory, or C. If [dir] is \"..\", the parent directory of the current one.\n", la)
            printp("dir; [path] : Lists all the files and folders in the current directory.\n", la)
            printp("read; [name] : Reads a file in the current directory.\n", la)
            printp("run; [name] : Runs [name].py file in the current directory.\n", la)
            printp("write; [name]; [line]; [text] : Replaces line [line] in file [name] with [text].\n", la)
        
        return 0
        
        if cmds[1] == "syntax":
            
            printp("Colons, \":::\", \"::\", \":\", are to show input from the user.\n", la)
            printp("Layers are used to indicate how many layers of programs the user is in.\n", la)
            
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0
        
    except Exception:
        pass
    
    printp("pOS : Little experimental operating system.\n\n", la)
    
    printp("alarm; [minutes]*opt : Lets you set an alarm that goes off after a set time.\n", la)
    printp("binary : Lets you do bitwise operations on a number in binary.\n", la)
    printp("calculator; [n1]*opt; [o]*opt; [n2]*opt : Basic calculator for basic operations.\n", la)
    printp("cls : Clears the screen.\n", la)
    printp("exit : Exits the current layer, if in the highest layer, it will quit the program.\n", la)
    printp("fete : File Explorer and Text Editor.\n", la)
    printp("help; [cmd] : Gives you a list of things you can do using [cmd], if [cmd] is blank, it prints help about pOS.\n", la)
    
    printp("List of Valid [cmd]s:\n", la + 1)
    printp("\"alarm\"\n", la + 1)
    printp("-\"binary\"\n", la + 1)
    printp("-\"calculator\"\n", la + 1)
    printp("-\"fete\"\n", la + 1)
    printp("-\"syntax\"\n", la + 1)
    
    printp("time : Gives the current time.\n", la)
    printp("quit : Quits the program, no matter what layer you are in.\n", la)
    printp("python : Starts Python by inputting the command \"python\" in your console. (Requires python installed)\n", la)
    
    printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
    return 0


if __name__ == "__main__":
    while True:
        print("::: ", end = "")
        commands = input().lower().split("; ")
        
        if commands[0] == "exit" or commands[0] == "quit":
            print("\u001b[0m")
            quit(0)
        if commands[0] == "alarm":
            if indexists(commands, 1):
                try:
                    thread = threading.Thread(target=alarm_thread_function, args=([float(commands[1])]), daemon=True)
                    thread.start()
                    printp("Alarm Set.\n", 0)
                except Exception:
                    pass
            if not indexists(commands, 1):
                alarm(1)
        if commands[0] == "binary":
            binary(1)
        if commands[0] == "calc" or commands[0] == "calculator":
            if indexists(commands, 1):
                try:
                    output = 0
                    if commands[2] == "+":
                        output = float(commands[1]) + float(commands[3])
                    if commands[2] == "-":
                        output = float(commands[1]) - float(commands[3])
                    if commands[2] == "*":
                        output = float(commands[1]) * float(commands[3])
                    if commands[2] == "/":
                        output = float(commands[1]) / float(commands[3])
                    if commands[2] == "%":
                        output = float(commands[1]) % float(commands[3])
                    if commands[2] == "^" or commands[1] == "**":
                        output = float(commands[1]) ** float(commands[3])
                    printp(f"{commands[1]} {commands[2]} {commands[3]} = {output}\n", 1)
                except Exception:
                    pass
            if not indexists(commands, 1):
                calculator(1)
        if commands[0] == "clear" or commands[0] == "cls" or commands[0] == "clear screen":
            os.system("cls")
        if commands[0] == "fete" or commands[0] == "file" or commands[0] == "files":
            fete(1)
        if commands[0] == "help":
            help(commands, 1)
        if commands[0] == "python":
            os.system("python")
        if commands[0] == "time" or commands[0] == "date": 
            now = datetime.now()
            print(now.strftime("%Y/%M/%D %H:%M:%S"))