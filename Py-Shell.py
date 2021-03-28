import os
import math
import time
from datetime import datetime
import winsound
import platform
from playsound import playsound
import threading
import multiprocessing
import shutil
import wmi
import signal
import decimal
import urllib.request
from bs4 import BeautifulSoup

#TODO: Add color changing and saving via edited config file.
#TODO: Add installation process to add config file.

playsound_process_array = []
# ^ Creating the global array, so two if statements can access it.
error_logs = ["Log Start"]

if __name__ == "__main__":
    os.system("cls")
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
    """Py-Shell Alarm System"""
    printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
    
    time_until = ""
    while not is_float(time_until):
        printp("Enter Minutes Until Alarm Starts: ", la)
        time_until = input()
        if time_until == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            quit(0)
        if time_until == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    thread = threading.Thread(target=alarm_thread_function, args=([float(time_until)]), daemon=True)
    thread.start()
    
    printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
    return 0

def binary(la: int) -> int:
    """Py-Shell Bit Manipulator"""
    printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
    num = ""
    while not is_int(num):
        printp("Enter Number (decimal): ", la)
        num = input()
        if num == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            quit(0)
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
        except Exception as e:
            global error_logs
            error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
            pass

        
    printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
    return 1

def calculator(la: int) -> int:
    """Py-Shell Calculator"""
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
    num = decimal.Decimal(num)
    while True:
        printp(f"{str(num)}\n", la + 1)
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
                num += decimal.Decimal(cmds[1])
            if cmds[0] == "cos":
                num = math.cos(num)
            if cmds[0] == "div" and cmds[1] != "0":
                num /= decimal.Decimal(cmds[1])
            if cmds[0] == "mod" and cmds[1] != "0":
                num = num % decimal.Decimal(cmds[1])
            if cmds[0] == "mul":
                num *= decimal.Decimal(cmds[1])
            if cmds[0] == "pow":
                num **= decimal.Decimal(cmds[1])
            if cmds[0] == "sin":
                num = math.sin(num)
            if cmds[0] == "set":
                num = decimal.Decimal(cmds[1])
            if cmds[0] == "sub":
                num -= decimal.Decimal(cmds[1])
            if cmds[0] == "tan":
                num = math.tan(num)
        except Exception as e:
            global error_logs
            error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
            pass
    
    printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
    return 1

def help(cmds, la: int) -> int:
    """Py-Shell Help Menu"""
    printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
    try:
        if cmds[1] == "alarm":
            printp("Alarm : Lets you set an alarm that goes off for five seconds after a set time.\n\n", la)
            
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
            printp("Calculator : Basic calculator for basic operations.\n", la)
            printp("*Note: All trigonometric commands use radians.\n\n", la)
            
            printp("add; [n] : Adds [n] to the current number.\n", la)
            printp("cos : Sets the current number to the cosine of the current number.\n", la)
            printp("div; [n] : Divides the current number by [n].\n", la)
            printp("mod; [n] : Sets the current number to the current number modulus [n].\n", la)
            printp("mul; [n] : Multiplies the current number by [n].\n",la)
            printp("pow; [n] : Sets the current number to be the current number to the power of [n].\n")
            printp("sin : Sets the current number to the sine of the current number.\n", la)
            printp("set; [n] : Sets the current number to [n].\n", la)
            printp("sub; [n] : Subtracts [n] from the current number.\n", la)
            printp("tan : Sets the current number to the tangent of the current number.\n", la)
            
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
        
        if cmds[1] == "multife" or cmds[1] == "file" or cmds[1] == "files":
            printp("MULTIFE : Multi-Purpose File Explorer.\n\n", la)
            
            printp("cd; [path]; [dir] : Changes the current directory to: A. [dir] itself, B. A folder named [dir] in the current directory, or C. If [dir] is \"..\", the parent directory of the current one.\n", la)
            printp("dir; [path] : Lists all the files and folders in the current directory.\n", la)
            printp("playsound; [path or file] : Plays the sound file located at [path] or if the file is in the current directory, with the name of [file].\n", la)
            printp("read; [name] : Reads a file in the current directory.\n", la)
            printp("run; [name] : Runs [name].py file in the current directory, requires Python to be installed.\n", la)
            printp("stopsound : stops ALL sounds played via the playsound command.\n", la)
            printp("write; [name]; [line]; [text] : Replaces line [line] in file [name] with [text].\n", la)
        
        return 0
        
        if cmds[1] == "syntax":
            
            printp("Colons, \":::\", \"::\", \":\", are to show input from the user.\n", la)
            printp("Layers are used to indicate how many layers of programs the user is in.\n", la)
            printp("In the help menu, \"*opt\" is used to show that a certain argument is optional and that the command functions without it.\n", la)
            
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0
        
    except Exception as e:
        global error_logs
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
        pass
    
    printp("Py-Shell : Little experimental operating system.\n\n", la)
    
    printp("alarm; [minutes]*opt : Lets you set an alarm that goes off for five seconds after a set time.\n", la)
    printp("binary : Lets you do bitwise operations on a number in binary.\n", la)
    printp("calculator; [n1]*opt; [o]*opt; [n2]*opt : Basic calculator for basic operations.\n", la)
    printp("cls : Clears the screen.\n", la)
    printp("exit : Exits the current layer, if in the highest layer, it will quit the program.\n", la)
    printp("help; [cmd] : Gives you a list of things you can do using [cmd], if [cmd] is blank, it prints help about Py-Shell.\n", la)
    
    printp("List of Valid [cmd]s:\n", la + 1)
    printp("\"alarm\"\n", la + 1)
    printp("-\"binary\"\n", la + 1)
    printp("-\"calculator\"\n", la + 1)
    printp("-\"multife\"\n", la + 1)
    printp("-\"syntax\"\n", la + 1)
    
    printp("logs : Shows the error logs.\n", la)
    printp("multife : Multi-Purpose File Explorer.\n", la)
    printp("python : Starts Python by inputting the command \"python\" in your console (requires python installed).\n", la)
    if __file__.endswith(".py"):
        printp("source : Prints the source code of the shell, if the Python version is being used.\n", la)
    printp("time : Prints the current time.\n", la)
    printp("uname; [attribute]*opt : Prints a collection of information about your device. If [attribute] is set, it will print that attribute of your device (if it exists).\n", la)
    printp("url2html; [url] : Prints the HTML tags of the website at [url].\n", la)
    printp("url2text; [ur]; [n]*opt : Prints the first [n] texts at the website at [url]. If [n] is not set, it will print them all.\n", la)
    printp("quit : Quits the program, no matter what layer you are in.\n", la)
    
    printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
    return 0

def multife(la: int) -> int:
    """Py-Shell Multi-Purpose File Explorer."""
    try:
        printp("\u001b[7m-M-U-L-T-I-P-U-R-P-O-S-E-F-I-L-E-E-X-P-L-O-R-E-R-\u001b[0m\u001b[33;1m\n", la)
        while True:
            global playsound_process_array
            current_path = os.getcwd()
            current_directory = os.listdir()
            printp(current_path + ":: ", la)
            cmds = input().lower().split("; ")
            if cmds[0] == "exit":
                printp("\u001b[7m-M-U-L-T-I-P-U-R-P-O-S-E-F-I-L-E-E-X-P-L-O-R-E-R-\u001b[0m\u001b[33;1m\n", la)
                return 0
            if cmds[0] == "quit":
                printp("\u001b[7m-M-U-L-T-I-P-U-R-P-O-S-E-F-I-L-E-E-X-P-L-O-R-E-R-\u001b[0m\u001b[33;1m\n", la)
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
            if (cmds[0] == "playsound" or cmds[0] == "playaudio") and os.path.exists(cmds[1]) and os.path.isfile(cmds[1]):
                playsound_process_array.append(multiprocessing.Process(target=playsound, args=(cmds[1],)))
                playsound_process_array[-1].daemon = True
                playsound_process_array[-1].start()
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
                if os.path.exists(current_path + "\\" + cmds[1]):
                    os.system("python -u " + current_path + "\\" + cmds[1])
                if os.path.exists(cmds[1]):
                    os.system("python -u " + cmds[1])
            if cmds[0] == "runexe" or cmds[0] == "runexec" or cmds[0] == "runexecutable":
                if os.path.exists(current_path + "\\" + cmds[1]):
                    os.system(current_path + "\\" + cmds[1])
                if os.path.exists(cmds[1]):
                    os.system(cmds[1])
            if cmds[0] == "write":
                if cmds[1] == "Py-Shell.py" or cmds[1] == __file__:
                    printp("*It is advised not to edit the source code of Py-Shell.\n", la)
                if os.path.isfile(current_path + "\\" + cmds[1]) and os.path.exists(current_path + "\\" + cmds[1]):
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
                if os.path.isfile(cmds[1]) and os.path.exists(cmds[1]):
                    if os.path.getsize(cmds[1]) > 0:
                        contents = []
                        with open(cmds[1], "r") as target_file_read:
                            contents = target_file_read.readlines()
                            contents[int(cmds[2])] = cmds[3]
                        with open(cmds[1], "w") as target_file_write:
                            target_file_write.writelines(contents)
                    if os.path.getsize(cmds[1]) <= 0:
                        with open(cmds[1], "w") as target_file_write:
                            target_file_write.writelines(cmds[3])
            if cmds[0] == "stopsound" or cmds[0] == "stopaudio":
                    for playsound_process in playsound_process_array:
                        playsound_process.terminate()
        return 0
        printp("\u001b[7m-M-U-L-T-I-P-U-R-P-O-S-E-F-I-L-E-E-X-P-L-O-R-E-R-\u001b[0m\u001b[33;1m\n", la)
    except Exception as e:
        global error_logs
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
        pass

if __name__ == "__main__":
    while True:
        print("::: ", end = "")
        commands = input().lower().split("; ")
        
        if commands[0] == "exit" or commands[0] == "quit":
            print("\u001b[0m")
            quit(0)
        if commands[0] == "alarm":
            error_logs.append(f"\n{time.time()}:\nUsed alarm\n")
            if indexists(commands, 1):
                try:
                    thread = threading.Thread(target=alarm_thread_function, args=([float(commands[1])]), daemon=True)
                    thread.start()
                    printp("Alarm Set.\n", 0)
                except Exception as e:
                    error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
                    pass
            if not indexists(commands, 1):
                error_logs.append(f"\n{time.time()}:\nEntered alarm\n")
                alarm(1)
        if commands[0] == "binary":
            error_logs.append(f"\n{time.time()}:\nEntered binary\n")
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
                except Exception as e:
                    error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
                    pass
            if not indexists(commands, 1):
                calculator(1)
        if commands[0] == "clear" or commands[0] == "cls" or commands[0] == "clear screen":
            error_logs.append(f"\n{time.time()}:\nCleared Screen\n")
            os.system("cls")
        if commands[0] == "killprocess":
            error_logs.append(f"\n{time.time()}:\nKilled Process {commands[1]}\n")
            try:
                os.kill(int(commands[1]), signal.SIGTERM)
            except Exception as e:
                error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
                pass
        if commands[0] == "help":
            error_logs.append(f"\n{time.time()}:\nEntered help\n")
            help(commands, 1)
        if commands[0] == "logs":
            for log in error_logs:
                printp(str(log) + "\n", 1)
            printp("Log End\n", 1)
        if commands[0] == "multife" or commands[0] == "file" or commands[0] == "files":
            error_logs.append(f"\n{time.time()}:\nEntered multife\n")
            multife(1)
        if commands[0] == "processes":
            error_logs.append(f"\n{time.time()}:\nChecked Processes\n")
            store = wmi.WMI()
            printp("ID         Name\n\n", 1)
            for process in store.Win32_Process():
                printp(f"{process.ProcessId:<10} {process.Name}\n", 1)
        if commands[0] == "python":
            error_logs.append(f"\n{time.time()}:\nOpened Python\n")
            os.system("python")
        if commands[0] == "time" or commands[0] == "date":
            error_logs.append(f"\n{time.time()}:\nChecked time\n") 
            now = datetime.now()
            printp(now.strftime("%Y/%M/%D %H:%M:%S") + "\n", 1)
            printp(str(time.time()) + "\n", 1)
        if (commands[0] == "source" or commands[0] == "sourcecode") and __file__.endswith(".py"):
            old_path = os.getcwd()
            os.chdir(os.path.dirname(__file__))
            with open("Py-Shell.py", "r") as source_file:
                print(source_file.read())
            os.chdir(old_path)
        if commands[0] == "uname" or commands[0] == "unix name":
            error_logs.append(f"\n{time.time()}:\nUsed uname\n")
            information = platform.uname()
            if indexists(commands, 1):
                try:
                    printp(f"{getattr(information, commands[1])}\n", 1)
                except Exception as e:
                    error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
                    pass
            if not indexists(commands, 1):
                printp(f"System: {information.system}\n", 1)
                printp(f"Network Name: {information.node}\n", 1)
                printp(f"Version: {information.release}\n", 1)
                printp(f"Machine: {information.machine}\n", 1)
                printp(f"Processor: {information.processor}\n", 1)
        if commands[0] == "u2h" or commands[0] == "urltohtml" or commands[0] == "url2html":
            try:
                print(urllib.request.urlopen(commands[1]).read())
            except Exception as e:
                error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
                pass
        if commands[0] == "u2t" or commands[0] == "urltotext" or commands[0] == "url2text":
            try:
                soup = BeautifulSoup(urllib.request.urlopen(commands[1]).read(), "html.parser")
                
                for unwanted in soup(["script", "style"]):
                    unwanted.decompose()
                
                if indexists(commands, 2):
                    print(list(soup.stripped_strings)[:int(commands[2])])
                if not indexists(commands, 2):
                    print(list(soup.stripped_strings))
            except Exception as e:
                error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
                pass