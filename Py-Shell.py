import os # multife, etc
import decimal # Calculator, accurate floats
if __name__ == "__main__":
    os.system("cls")
    print("\u001b[33;1m")
    print("Importing Modules")
def load_percent(num: int):
    #round((decimal.Decimal(num) / decimal.Decimal(24)) * 100, 2)
    print(f"[{(num/24):.2%}%]", end = "\r")
import math # Calculator
load_percent(3)
import time # Time
load_percent(4)
from datetime import datetime # Time
load_percent(5)
import winsound # Alarm
load_percent(6)
import platform # Uname
load_percent(7)
from playsound import playsound # Multife Sound Player
load_percent(8)
import threading # Alarm, etc
load_percent(9)
import multiprocessing # Sound Player, etc
load_percent(10)
import shutil # Copy, remove directory, move
load_percent(11)
import wmi # Processes
load_percent(12)
import signal # Kill Process
load_percent(13)
import urllib.request # URL commands
load_percent(14)
from bs4 import BeautifulSoup # u2t
load_percent(15)
import webbrowser # u2w
load_percent(16)
import sys # ? sys.executable
load_percent(17)
import googlesearch # google
load_percent(18)
import socket # IP and p2p
load_percent(19)
import wikipedia # wikipedia
load_percent(20)
import psutil # random
load_percent(21)
import getpass # introduction via getuser
load_percent(22)
import random # take a guess
load_percent(23)
import msvcrt
load_percent(24)

#TODO: Add color changing and saving via edited config file.
#TODO: Add installation process to add config file.

playsound_process_array = []
# ^ Creating the global array, so two if statements can access it.
error_logs = ["Log Start"]

random_flag = False

p2p_enabled = False

def connect(conn):
    global p2p_enabled
    try:
        while True:
            if not p2p_enabled:
                return 0
            received = conn.recv(1024)
            if received ==' ':
                pass
            else:
                print(str(conn.getsockname()[0]) + ": " + received.decode())
    except ConnectionResetError as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
        p2p_enabled = False

def send_msg(conn):
    global p2p_enabled
    try:
        while True:
            if not p2p_enabled:
                return 0
            send_msg = input()[0:].encode("utf-8")
            if send_msg == '':
                pass
            if send_msg.decode() == "exit":
                p2p_enabled = False
            if send_msg.decode() == "quit":
                p2p_enabled = False
                sys.exit(0)
            else:
                conn.sendall(send_msg)
    except ConnectionResetError as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
        print("Client Disconnected")
        p2p_enabled = False

def thread_receiver(PORT_LISTEN: int):
    #receiver
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', int(PORT_LISTEN)))
    s.listen()
    (conn, addr) = s.accept() 
    #receiver
    
    thread1 = threading.Thread(target = connect, args = ([conn]))
    thread1.start()
    thread1.join()
    return 0

def indexists(list_input, index: int) -> bool:
    """Returns a boolean based off of whether or not the inputted [index] exists in [list_input]."""
    return index <= len(list_input) - 1

def mindexists(list_input, indices) -> bool:
    """indexists() for lists."""
    return all(index <= len(list_input) - 1 for index in indices)

def is_float(s: str) -> bool:
    """Returns a boolean based off of whether or not the inputted string [s] can be reprsented as a float. Can take arrays of strings aswell."""
    try: 
        if type(s) == str:
            float(s)
            return True
        if type(s) == list:
            return all([is_float(stri) for stri in s])
        return False
    except ValueError:
        return False

def is_int(s: str) -> bool:
    """Returns a boolean based off of whether or not the inputted string [s] can be reprsented as an integer. Can take arrays of strings aswell."""
    try: 
        if type(s) == str:
            int(s)
            return True
        if type(s) == list:
            return all([is_int(stri) for stri in s])
        return False
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
            sys.exit(0)
        if time_until == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    thread = threading.Thread(target=alarm_thread_function, args=([float(time_until)]), daemon=True)
    thread.start()
    
    printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
    return 0

def binary(la: int, starting_num = None) -> int:
    """Py-Shell Bit Manipulator"""
    printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
    num = starting_num
    while not is_int(num):
        printp("Enter Number (decimal): ", la)
        num = input()
        if num == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            sys.exit(0)
        if num == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    num = int(num)
    while True:
        try:
            printp(f"{bin(num)}; {num}; {hex(num)}\n", la + 1)
            printp(":: " if la < 2 else ": ", la)
            cmds = input().lower().split("; ")
            if cmds[0] == "exit":
                printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
                return 0
            if cmds[0] == "quit":
                printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
                print("\u001b[0m")
                sys.exit(0)
            if cmds[0] == "not":
                num = ~num
            if cmds[0] == "get":
                printp(str(1 if num & (0b1 << int(cmds[1])) != 0 else 0) + "\n", la + 1)
            if cmds[0] == "help":
                help(["help", "binary"], la + 1)
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

        
    printp("\u001b[7m-B-I-N-A-R-Y-\u001b[0m\u001b[33;1m\n", la)
    return 1

def calculator(la: int, starting_num = None) -> int:
    """Py-Shell Calculator"""
    printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
    num = starting_num
    while not is_float(num):
        printp("Enter Number: ", la)
        num = input()
        if num == "quit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            sys.exit(0)
        if num == "exit":
            printp("\u001b[7m-A-L-A-R-M-\u001b[0m\u001b[33;1m\n", la)
            return 0
    num = decimal.Decimal(num)
    while True:
        printp(f"{str(num)}\n", la + 1)
        printp(":: " if la < 2 else ": ", la)
        cmds = input().lower().split("; ")
        if cmds[0] == "exit":
            printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
            return 0
        if cmds[0] == "quit":
            printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
            print("\u001b[0m")
            sys.exit(0)
        try:
            if cmds[0] == "add":
                num += decimal.Decimal(cmds[1])
            if cmds[0] == "cos":
                num = decimal.decimal(math.cos(num))
            if cmds[0] == "div" and cmds[1] != "0":
                num /= decimal.Decimal(cmds[1])
            if cmds[0] == "help":
                help(["help", "calc"], 2)
            if cmds[0] == "inv":
                num = 1/num
            if cmds[0] == "nrt":
                num **= (1 / decimal.Decimal(cmds[1]))
            if cmds[0] == "mod" and cmds[1] != "0":
                num = num % decimal.Decimal(cmds[1])
            if cmds[0] == "mul":
                num *= decimal.Decimal(cmds[1])
            if cmds[0] == "pow":
                num **= decimal.Decimal(cmds[1])
            if cmds[0] == "sin":
                num = decimal.decimal(math.sin(num))
            if cmds[0] == "set":
                num = decimal.Decimal(cmds[1])
            if cmds[0] == "sqr":
                num = decimal.Decimal(num ** 2)
            if cmds[0] == "sqt":
                num = decimal.Decimal(math.sqrt(num))
            if cmds[0] == "sub":
                num -= decimal.Decimal(cmds[1])
            if cmds[0] == "tan":
                num = decimal.decimal(math.tan(num))
        except Exception as e:
            global error_logs
            error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
    
    printp("\u001b[7m-C-A-L-C-U-L-A-T-O-R-\u001b[0m\u001b[33;1m\n", la)
    return 1

def killprocess(cmds):
    global error_logs
    error_logs.append(f"\n{time.time()}:\nKilled Process {cmds[1]}\n")
    try:
        os.kill(int(cmds[1]), signal.SIGTERM)
    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")

def logs():
    for log in error_logs:
        printp(str(log) + "\n", 1)
    printp("Log End\n", 1)

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
            printp("help : Prints this section of the help command.\n", la)
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
            printp("help : Prints this section of the help command.\n", la)
            printp("inv : Sets the current number to one divided by the current number.\n", la)
            printp("nrt; [n] : Sets the current number to the [n]th root of the current number.\n", la)
            printp("mod; [n] : Sets the current number to the current number modulus [n].\n", la)
            printp("mul; [n] : Multiplies the current number by [n].\n", la)
            printp("pow; [n] : Sets the current number to be the current number to the power of [n].\n", la)
            printp("sin : Sets the current number to the sine of the current number.\n", la)
            printp("set; [n] : Sets the current number to [n].\n", la)
            printp("sqr : Sets the current number to the current number squared.\n", la)
            printp("sqt : Sets the current number to the square root of the current number.\n", la)
            printp("sub; [n] : Subtracts [n] from the current number.\n", la)
            printp("tan : Sets the current number to the tangent of the current number.\n\n", la)
            
            printp("Calculator is also usable in one line.\n", la)
            printp("calculator; [n1]; [o], [n2] : Uses [o] on [n1] and [n2].\n", la)
            printp("List of Operations for One-Line Calculations:\n", la)
            printp("+ : Addition\n", la + 1)
            printp("/ : Division\n", la + 1)
            printp("% : Modulus\n", la + 1)
            printp("* : Multiplication\n", la + 1)
            printp("^ : Exponentiation\n", la + 1)
            printp("- : Subtraction\n", la + 1)
            
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0
        
        if cmds[1] == "notes":
            printp("Note 1. Py-Shell is best used in Python, however, it will require downloading of modules to use in Python, all of these can be installed via pip.\n", la)
            printp("Note 2. Py-Shell can be activated via commandprompt easily by going to C:\\[username]\\ and typing \"py-shell\" if Py-Shell.bat is installed (which should happen automatically).\n", la)
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0

        if cmds[1] == "multife" or cmds[1] == "file" or cmds[1] == "files":
            printp("MULTIFE : Multi-Purpose File Explorer.\n\n", la)
            
            printp("cd; [path]; [dir] : Changes the current directory to: A. [dir] itself, B. A folder named [dir] in the current directory, or C. If [dir] is \"..\", the parent directory of the current one.\n", la)
            printp("dir; [path] : Lists all the files and folders in the current directory.\n", la)
            printp("help : Prints this section of the help command.\n", la)
            printp("playsound; [path or file] : Plays the sound file located at [path] or if the file is in the current directory, with the name of [file].\n", la)
            printp("read; [name] : Reads a file in the current directory.\n", la)
            printp("rename; [file]; [new name] : Renames [file] in the current directory to [new name].\n", la)
            printp("run; [name] : Runs [name].py file in the current directory, requires Python to be installed.\n", la)
            printp("runexe; [name] : Runs [name].exe file in the current directory.\n", la)
            printp("stopsound : stops ALL sounds played via the playsound command.\n", la)
            printp("write; [name]; [line]; [text] : Replaces line [line] in file [name] with [text].\n", la)
        
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0

        if cmds[1] == "random" or cmds[1] == "rand":
            printp("Random: Random Number Generation\n\n", la)
            
            printp("01 : Prints a random floating point number between 0 and 1.\n", la)
            printp("binary : Converts the last randomly generated number into an integer and then starts the binary command.\n", la)
            printp("calculator : Brings the last randomly generated number to the calculator.\n", la)
            printp("help : Prints this section of the help command.\n", la)
            printp("randfloat : [a]; [b] : Prints a floating point number [a] <= number <= [b].\n", la)
            printp("randint; [a]; [b]; [step]*opt : Prints a number [a] <= number <= [b], with [step] being a number that is guaranteed to be a factor of the distance between the number and [a].\n", la)
            
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
            return 0

        if cmds[1] == "roadmap":
            printp("Roadmap: Future Updates\n\n", la)
        
            printp("C+1 : Bug fixes, polishing, more commands.\n", la)
            printp("C+2 : Possible fixes for p2p, more commands.\n", la)
            printp("----\n", la)
            printp("C+1.0 : Creation of entirely new version based off curses. (Subject to Change)\n", la)
            
            printp("\u001b[7m-H-E-L-P-\u001b[0m\u001b[33;1m\n", la)
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
    
    printp("Py-Shell : Little experimental operating shell.\n\n", la)
    
    #a
    printp("alarm; [minutes]*opt : Lets you set an alarm that goes off for five seconds after a set time.\n", la)
    #b
    printp("binary : Lets you do bitwise operations on a number in binary.\n", la)
    #c
    printp("calculator; [n1]*opt; [o]*opt; [n2]*opt : Basic calculator for basic operations.\n", la)
    printp("cls : Clears the screen.\n", la)
    #d
    #e
    printp("exit : Exits the current layer, if in the highest layer, it will quit the program.\n", la)
    #f
    #g
    printp("google; [search] : Searches google for [search] and returns the first one hundred results.\n", la)
    #h
    printp("help; [cmd] : Gives you a list of things you can do using [cmd], if [cmd] is blank, it prints help about Py-Shell.\n", la)
    
    printp("List of Valid [cmd]s:\n", la + 1)
    printp("\"alarm\"\n", la + 1)
    printp("-\"binary\"\n", la + 1)
    printp("-\"calculator\"\n", la + 1)
    printp("-\"notes\"\n", la + 1)
    printp("-\"multife\"\n", la + 1)
    printp("-\"roadmap\"\n", la + 1)
    printp("-\"syntax\"\n", la + 1)
    #i
    #j
    #k
    printp("killprocess; [id]: Kills a process on your machine with [id].\n", la)
    #l
    printp("logs : Shows the error logs.\n", la)
    #m
    printp("multife : Multi-Purpose File Explorer.\n", la)
    #n
    #o
    #p
    printp("p2p : Starts p2p. Note: Very experimental and not recommended.\n", la)
    printp("processes : Prints a list of the processes running on your machine and their id.\n", la)
    printp("python : Starts Python by inputting the command \"python\" in your console (requires python installed).\n", la)
    if sys.argv[0].endswith(".py"):
        printp("source : Prints the source code of the shell, if the Python version is being used.\n", la)
    #q
    printp("quit : Quits the program, regardless of what layer you are in.\n", la)
    #r
    #s
    #t
    printp("time : Prints the current time.\n", la)
    #u
    printp("uname; [attribute]*opt : Prints a collection of information about your device. If [attribute] is set, it will print that attribute of your device (if it exists).\n", la)
    printp("url2html; [url] : Prints the HTML tags of the website at [url].\n", la)
    printp("url2text; [url]; [n]*opt : Prints the first [n] texts at the website at [url]. If [n] is not set, it will print them all.\n", la)
    printp("url2web; [url] : Opens [url] in a new tab, or if no browser is open, it will open your default browser.\n", la)
    #v
    #w
    printp("wikipedia; [article]; [sentences]*opt : Prints [sentences] sentences of a summary of the Wikipedia article about [article]. If [sentences] is left empty, it prints out the entire summary.\n", la)
    printp("wikipediasearch; [term] : Prints the search results for a term on Wikipedia, this can help you find an article.\n", la)
    #x
    #y
    #z
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
            printp(current_path + ":: " if la < 2 else ": ", la)
            cmds = input().lower().split("; ")
            if cmds[0] == "exit":
                printp("\u001b[7m-M-U-L-T-I-P-U-R-P-O-S-E-F-I-L-E-E-X-P-L-O-R-E-R-\u001b[0m\u001b[33;1m\n", la)
                return 0
            if cmds[0] == "quit":
                printp("\u001b[7m-M-U-L-T-I-P-U-R-P-O-S-E-F-I-L-E-E-X-P-L-O-R-E-R-\u001b[0m\u001b[33;1m\n", la)
                print("\u001b[0m")
                sys.exit(0)
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
            if cmds[0] == "help":
                help(["help", "multife"], la + 1)
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
            if cmds[0] == "rename":
                if cmds[1].endswith("Py-Shell.py") or cmds[1].endswith("Py-Shell.exe"):
                    printp("It is not recommended to rename Py-Shell files.\n", la)
                os.rename(cmds[1], cmds[2])
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
                if cmds[1].endswith("Py-Shell.py") or cmds[1].endswith("Py-Shell.exe"):
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

def p2p(la: int):
    printp("Note: p2p is highly experimental, was not originally made for Py-Shell and is not recommended for use.\n", la)
    global error_logs
    IP = input("Enter IP: ")
    PORT_TARGET = ""
    PORT_LISTEN = ""
    while True:
        try:
            PORT_TARGET = int(input("Enter Target Port (10,000-50,000) (Standard: 3773): "))
            PORT_LISTEN = int(input("Enter Listen Port (10,000-50,000) (Standard: 7337): "))
        except Exception as e:
            error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
            continue
        break

    while True:
        try:
            thread_receiver_thread = threading.Thread(target=thread_receiver, args = ([PORT_LISTEN]))
            thread_receiver_thread.start()
            
            # transmitter
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((IP, int(PORT_TARGET)))
            # transmitter
            
            thread2 = threading.Thread(target = send_msg, args = ([s]))
            thread2.start()
            thread2.join()
            return 0
        except Exception as e:
            error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
            continue

def processes():
    global error_logs
    error_logs.append(f"\n{time.time()}:\nChecked Processes\n")
    store = wmi.WMI()
    printp("ID         Name\n\n", 1)
    for process in store.Win32_Process():
        printp(f"{process.ProcessId:<10} {process.Name}\n", 1)

def random_command(la: int):
    printp("\u001b[7m-R-A-N-D-O-M-\u001b[0m\u001b[33;1m\n", la)
    global error_logs
    try:
        global random_flag
        last_number = 0
        while True:
            
            mem = sum(psutil.virtual_memory()) # numbers
            time_var = time.time() # number
            mem_swap = sum(psutil.swap_memory()) # numbers
            cpu = sum(psutil.cpu_times()) # numbers
            cpu_freq = sum(psutil.cpu_freq()) # numbers
            random_var = int.from_bytes(os.urandom(1), "big") if random_flag else int.from_bytes(os.urandom(1), "little") # number
            random_flag = not random_flag
            random_integer_var = random.getrandbits(1000 ** (int(random_flag) + 1))
            random.seed(a=(float(mem) + float(time_var) - float(mem_swap) + float(cpu) - float(cpu_freq) + float(random_var)))
            printp(":: " if la < 2 else ": ", la)
            cmds = input().lower().split("; ")
            
            if cmds[0] == "01":
                last_number = random.random()
                printp(f"{last_number}\n", la + 1)
            if cmds[0] == "binary":
                binary(la + 1, int(last_number))
            if cmds[0] == "calculator" or cmds[0] == "calc":
                calculator(la + 1, last_number)
            if cmds[0] == "exit":
                return 0
            if cmds[0] == "help":
                help(["help", "random"], la + 1)
            if (cmds[0] == "randfloat" or cmds[0] == "float") and mindexists(cmds, [1, 2]):
                if is_float(cmds[1:]) and cmds[2] > cmds[1]:
                    last_number = random.uniform(float(cmds[1]), float(cmds[2]))
                    printp(f"{last_number}\n", la + 1)
            if (cmds[0] == "randint" or cmds[0] == "integer") and mindexists(cmds, [1, 2]):
                if is_int(cmds[1:]) and cmds[2] > cmds[1]:
                    if indexists(cmds, 3):
                        last_number = random.randrange(int(cmds[1]), int(cmds[2]) + 1, int(cmds[3]))
                        printp(f"{last_number}\n", la + 1)
                    if not indexists(cmds, 3):
                        last_number = random.randrange(int(cmds[1]), int(cmds[2]) + 1)
                        printp(f"{last_number}\n", la + 1)
            if cmds[0] == "quit":
                sys.exit(0)

    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
    
    printp("\u001b[7m-R-A-N-D-O-M-\u001b[0m\u001b[33;1m\n", la)

def source_code():
    if sys.argv[0].endswith(".py"):
        old_path = os.getcwd()
        os.chdir(os.path.dirname(sys.argv[0]))
        with open("Py-Shell.py", "r") as source_file:
            print(source_file.read())
        os.chdir(old_path)

def stopwatch():
    start_time = time.perf_counter()
    while True:
        seconds = time.perf_counter() - start_time
        printp(f"\rHours: {round(seconds / 3600, 2)} | Minutes: {round(seconds / 60, 2)} |  Seconds: {round(seconds, 2)}", 1)
        if msvcrt.kbhit():
            printp("\n", 1)
            break

def time_command():
    global error_logs
    error_logs.append(f"\n{time.time()}:\nChecked time\n") 
    now = datetime.now()
    printp(now.strftime("%Y/%M/%D %H:%M:%S") + "\n", 1)
    printp(str(time.time()) + "\n", 1)

def uname(cmds):
    error_logs.append(f"\n{time.time()}:\nUsed uname\n")
    information = platform.uname()
    if indexists(cmds, 1):
        try:
            printp(f"{getattr(information, cmds[1])}\n", 1)
        except Exception as e:
            error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
    if not indexists(cmds, 1):
        printp(f"System: {information.system}\n", 1)
        printp(f"Network Name: {information.node}\n", 1)
        printp(f"Version: {information.release}\n", 1)
        printp(f"Machine: {information.machine}\n", 1)
        printp(f"Processor: {information.processor}\n", 1)

def u2h(cmds):
    global error_logs
    try:
        print(urllib.request.urlopen(cmds[1]).read())
    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")

def u2t(cmds):
    try:
        soup = BeautifulSoup(urllib.request.urlopen(cmds[1]).read(), "html.parser")
        
        for unwanted in soup(["script", "style"]):
            unwanted.decompose()
        
        if indexists(cmds, 2):
            print(list(soup.stripped_strings)[:int(cmds[2])])
        if not indexists(cmds, 2):
            print(list(soup.stripped_strings))
    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")

def u2w(cmds):
    global error_logs
    try:
        webbrowser.open_new_tab(cmds[1])
    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")

def wikipedia_summary(cmds):
    try:
        if indexists(cmds, 1):
            if indexists(cmds, 2):
                #print("\u001b[1m")
                printp(f"First {cmds[2]} sentences of the Wikipedia Summary for \"{cmds[1]}\"\n\n", 1)
                #print("\u001b[0m\u001b[33;1m")
                for line in wikipedia.summary(cmds[1], sentences=int(cmds[2])).split("\n"):
                    printp(line + "\n", 1)
            if not indexists(cmds, 2):
                printp(f"Wikipedia Summary for \"{cmds[1]}\"\n\n", 1)
                for line in wikipedia.summary(cmds[1]).split("\n"):
                    printp(line + "\n", 1)
    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")

def wikipedia_search(cmds):
    try:
        if indexists(commands, 1):
            #print("\u001b[1m")
            printp(f"Wikipedia Search Results for \"{commands[1]}\"\n\n", 1)
            #print("\u001b[0m\u001b[33;1m")
            for result in wikipedia.search(commands[1]):
                printp(result + "\n", 1)
    except Exception as e:
        error_logs.append(f"\n{time.time()}:\n{str(e)}\n")

if __name__ == "__main__":
    if sys.argv[0].endswith(".exe"):
        print("Verifying Py-Shellexe.bat File")
        with open(os.path.expanduser("~") + "\\" + "Py-Shellexe.bat", "w") as f:
            f.write("@echo off\n")
            f.write(sys.argv[0])
    if sys.argv[0].endswith(".py"):
        print("Verifying Py-Shell.bat File")
        with open(os.path.expanduser("~") + "\\" + "Py-Shell.bat", "w") as f:
            f.write("@echo off\n")
            f.write(f"python -u {__file__}")
    print("Note: Don't use the batch script to start a version of Py-Shell that was not the last version you used.")
    if not os.path.exists(os.path.expanduser("~") + "\\" + "Py-Shell-Data"):
        print("Creating Py-Shell-Data")
        os.mkdir(os.path.expanduser("~") + "\\" + "Py-Shell-Data")
        with open(os.path.expanduser("~") + "\\" + "Py-Shell-Data\\statistics", "w") as f:
            f.write("1") # Times Py-Shell opened.
    if os.path.exists(os.path.expanduser("~") + "\\" + "Py-Shell-Data"):
        with open(os.path.expanduser("~") + "\\" + "Py-Shell-Data\\statistics", "r") as f:
            current_num = int(f.read())
        with open(os.path.expanduser("~") + "\\" + "Py-Shell-Data\\statistics", "w") as f:
            f.write(str(current_num + 1))
    with open(os.path.expanduser("~") + "\\" + "Py-Shell-Data\\statistics", "r") as f:
        print("Reading Information from Py-Shell-Data")
        booted_up = f.readline()
    os.system("cls")
    # v These are ANSI color codes, this one makes all the text bright yellow.
    print("\u001b[33;1m")
    print(f"Py-Shell User: {getpass.getuser()} [Experimental]")
    while True:
        print("::: ", end = "")
        commands = input().lower().split("; ")
        
        if commands[0] == "exit" or commands[0] == "quit":
            print("\u001b[0m")
            sys.exit(0)
        if commands[0] == "alarm":
            error_logs.append(f"\n{time.time()}:\nUsed alarm\n")
            if indexists(commands, 1):
                try:
                    thread = threading.Thread(target=alarm_thread_function, args=([float(commands[1])]), daemon=True)
                    thread.start()
                    printp("Alarm Set.\n", 0)
                except Exception as e:
                    error_logs.append(f"\n{time.time()}:\n{str(e)}\n")
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
            if not indexists(commands, 1):
                calculator(1)
        if commands[0] == "clear" or commands[0] == "cls" or commands[0] == "clear screen":
            error_logs.append(f"\n{time.time()}:\nCleared Screen\n")
            os.system("cls")
        if commands[0] == "echo" and indexists(commands, 1):
            printp(commands[1] + "\n", 1)
        if commands[0] == "google" or commands[0] == "googlesearch":
            for result in googlesearch.search(commands[1], num_results=100):
                printp(str(result) + "\n", 1)
        if commands[0] == "help":
            error_logs.append(f"\n{time.time()}:\nEntered help\n")
            help(commands, 1)
        if commands[0] == "ip":
            IP = socket.gethostbyname(socket.gethostname())
            printp(str(IP) + "\n", 1)
        if commands[0] == "killprocess":
            killprocess(commands)
        if commands[0] == "logs":
            logs()
        if commands[0] == "multife" or commands[0] == "file" or commands[0] == "files":
            error_logs.append(f"\n{time.time()}:\nEntered multife\n")
            multife(1)
        if commands[0] == "p2p":
            p2p_enabled = True
            p2p(1)
        if commands[0] == "processes":
            processes()
        if commands[0] == "python":
            error_logs.append(f"\n{time.time()}:\nOpened Python\n")
            os.system("python")
        if commands[0] == "random" or commands[0] == "rand":
            random_command(1) # An hour and a half debugging, to realise I defined a function as "random()"
        if (commands[0] == "source" or commands[0] == "sourcecode") and sys.argv[0].endswith(".py"):
            source_code()
        if commands[0] == "stopwatch":
            stopwatch()
        if commands[0] == "time" or commands[0] == "date":
            time_command()
        if commands[0] == "uname" or commands[0] == "unix name":
            uname(commands)
        if commands[0] == "u2h" or commands[0] == "urltohtml" or commands[0] == "url2html":
            u2h(commands)
        if commands[0] == "u2t" or commands[0] == "urltotext" or commands[0] == "url2text":
            u2t(commands)
        if commands[0] == "u2w" or commands[0] == "urltoweb" or commands[0] == "url2web":
            u2w(commands)
        if commands[0] == "wikipedia":
            wikipedia_summary(commands)
        if commands[0] == "wikipediasearch":
            wikipedia_search(commands)