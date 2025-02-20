import time         # <---- can be used to slow input but I ended up not using it
import sys          # <---- used to access the lower level write methods to get around lmitations with print()
import subprocess   # <---- used to clear the screen using subsystem.run('clear',shell=True)
import tty          # <---- used to get raw input from keyboard
import termios      # <---- used to restore terminal input and display from being raw
import readline
# print('\n\n\n\n\n\n\n\n\n\n')
oldval = [27906, 5, 1215, 35387, 15, 15, [b'\x03', b'\x1c', b'\x7f', b'\x15', b'\x04', b'\x00', b'\x01', b'\x00', b'\x11', b'\x13', b'\x1a', b'\xff', b'\x12', b'\x0f', b'\x17', b'\x16', b'\xff', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00']]
#^ stores system ermios datta in a variable in case things go ... not as expected

numbers_and_symbols = { ## <----  defines a dictionary full of 6x7 ansi color code characters representing numbers and operators
    "quit": [
        "\033[0m      ", 
        "\033[0m \033[37;47m \033[0m    ", 
        "\033[37;47m   \033[0m   ", 
        "\033[0m   \033[37;47m  \033[0m ",
        "\033[0m   \033[37;47m \033[0m  ",
        "\033[0m   \033[37;47m  \033[0m ",
        "\033[0m      ",
        ],
    "clear": [
        "\033[0m      ", 
        "\033[0m \033[37;47m    \033[0m ", 
        "\033[0m \033[37;47m \033[0m    ", 
        "\033[0m \033[37;47m \033[0m    ",
        "\033[0m \033[37;47m \033[0m    ",
        "\033[0m \033[37;47m    \033[0m ", 
        "\033[0m      ", 
        ],
    "0": [
        "\033[0m      ", 
        "\033[0m \033[37;47m    \033[0m ", 
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ", 
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ", 
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ", 
        "\033[0m \033[37;47m    \033[0m ", 
        "\033[0m      ", 
        ],
    "1": [
       "\033[0m      ", 
       "\033[0m  \033[37;47m  \033[0m  ",
       "\033[0m \033[37;47m   \033[0m  ",
       "\033[0m  \033[37;47m  \033[0m  ",
       "\033[0m  \033[37;47m  \033[0m  ",
       "\033[0m \033[37;47m    \033[0m ",
       "\033[0m      "
    ],
    "2": [
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m \033[37;47m \033[0m    ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m     "
    ],

    "3": [
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m     "
    ],
    "4": [
        "\033[0m      ",
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ",
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m     "
    ],
    "5": [
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m \033[37;47m \033[0m    ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m     "
    ],
    "6": [
        "\033[0m      ",
        "\033[0m \033[37;47m \033[0m    ",
        "\033[0m \033[37;47m \033[0m    ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m     "
    ],
    "7": [
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m     "
    ],
    "8": [
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m     "
    ],
    "9": [
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m \033[37;47m \033[0m  \033[37;47m \033[0m ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m    \033[37;47m \033[0m ",
        "\033[0m     "
    ],
    "+": [
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m   \033[37;47m \033[0m  ",
        "\033[0m  \033[37;47m   \033[0m ",
        "\033[0m   \033[37;47m \033[0m  ",
        "\033[0m      ",
        "\033[0m       "
    ],
    "-": [
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        " \033[0m\033[37;47m    \033[0m ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      "
    ],
    "/": [
        "\033[0m      ",
        "\033[0m   \033[37;47m \033[0m  ",
        "\033[0m      ",
        "\033[0m  \033[37;47m   \033[0m ",
        "\033[0m      ",
        "\033[0m   \033[37;47m \033[0m  ",
        "\033[0m      "
    ],
    "*": [
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m  \033[37;47m \033[0m \033[37;47m \033[0m ",
        "\033[0m   \033[37;47m \033[0m  ",
        "\033[0m  \033[37;47m \033[0m \033[37;47m \033[0m ",
        "\033[0m      ",
        "\033[0m      "
    ],
    '=': [
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m      ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m      ",
        "\033[0m      "
    ],
    'point': [
        "\033[0m      ",
        "\033[0m  \033[37;47m  \033[0m  ",
        "\033[0m \033[37;47m    \033[0m ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m     "
    ],
   
    '.': [
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m\033[37;47m \033[0m",
        "\033[0m     "
    ],
    'dotshow': [
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m  \033[37;47m  \033[0m  ",
        "\033[0m      ",
    ],
    'space': [
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m      ",
        "\033[0m     "
    ],
    'halfspace': [
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m ",
        "\033[0m "
    ]

}

subprocess.run('clear',shell=True) # <---- clears terminal

def bigPrint(chars, color=False):   # <----  method to read list, grab dictionary values, append lines 1-7 in ansi characters to line 0 -6 to print later
    line0 = []
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    line6 = []
    for x,y in enumerate(chars): # <---- run through each character in the provided list

        getMatrix = numbers_and_symbols[str(y)]  # <---- gets the list value from the key in chars, appends them to the appropriate line 0 - 6 list

        if color != False:
            match color:
                case "RED":
                    color = "\u001b[41m"
                case "BLUE":
                    color = "\u001b[44m"
                case "GREEN":
                    color = "\u001b[42m"
                case "YELLOW":
                    color = "\u001b[43m"

            getMatrix = [x.replace("\033[37;47m", color) for x in getMatrix]

        line0.append(getMatrix[0])
        line1.append(getMatrix[1])
        line2.append(getMatrix[2])
        line3.append(getMatrix[3])
        line4.append(getMatrix[4])
        line5.append(getMatrix[5])
        line6.append(getMatrix[6])

    print(f'{"".join(line0)}\n{"".join(line1)}\n{"".join(line2)}\n{"".join(line3)}\n{"".join(line4)}\n{"".join(line5)}\n{"".join(line6)}',end='\r') # <---- prints the combined anssi code lits as images representing numbers and operators


choiceList = ['quit','clear',0,1,2,3,4,5,6,7,8,9,"+",'-','/',"*",'=','dotshow']  # <---- list representing each option, datshow is shorter than the actual one we use below.


bigPrint(choiceList)  # <----  print the menu

def pointer(pointlist):  # <---- navigate the printed menu with a pointer
    
    if len(pointlist) > 18:  
        pointlist = pointlist[len(pointlist)-18:len(pointlist)] # <---- if the list provided is too long, cut it down to the maximum size
                                                                        # this should never happen but is here just in case
    sys.stdout.write('\r\x1b[K')  # <---- clears the current line
    bigPrint(pointlist)  # <---- calls bigprint above using the pointer location

pointer(['point'])  # <---- prints the inital pointer at the starting location

def clc():      # <----  The acutal calculator 
    operand = ""
    printline = []
    preline = []
    postline = []
    answer = None
    terminalSettings = oldval
    
    sendInput = ['point']  # <---- default single entry in the pointer which rests it on the 1st option
    running = True  # <---- on/off switch for the below loop
    color = input("Enter a color preference if you have one. Invalid colors will be ignored.  red, yellow, green, or blue: ").upper()
    if not color in ["RED","BLUE","GREEN","YELLOW"]:
        color = False
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K\r\x1b[K')
    sys.stdout.write('\x1b[1B')
    sys.stdout.flush()
    while running:
        

        


        # if color != False:
        #     if color not in ["red","green","red","yellow","blue"]:
        #         print("invalid color")
        #         running = False
            
        tty.setraw(sys.stdin)   # <----  require keyboard input to be processed in its raw form which is broken into three 2-digit numbers or escape characters
        char = sys.stdin.read(1)   # <----   capture the first input 2-digit # or escape code
        if char in ['\r','\n']:  # <---- if it's the enter key
                
            if len(sendInput) == 2: # <---- if the length of sendInput, which is how we navigate the pointer, is 2, which is the clear function
                                           # Execute actions appropriate for clearing data and adjusting the line where data is printed
                printline = []
                preline = []
                postline = []
                operand = ""
                for x in range(6):  # <----  loops 6 times, each loop moves a row down and clears it of prior printed data
                        sys.stdout.write('\x1b[1B')
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        sys.stdout.flush()
                sys.stdout.write('\x1b[6A')  # <----  moves up 6 lines to where we started
                    
            elif len(sendInput) == 1: # <----  if the pointer is at the first option (quit)
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminalSettings)  # <---- restore terminal settings
                # exit()
                running = False  # <----  end the loop, killing the program

            elif 12 < len(sendInput) < 17:  # <----  if the cursur is between 13 and 16, you're selecting an operator, take appropriate actions
                if len(preline) == 0 or (len(preline) == 1 and preline[0] == "."):  # <---- if pre calculated characterss are 0, or there is one but it's a decimal, don't act
                    pass
                else:   
                    operand = choiceList[len(sendInput)-1]   # <----   set the operator variable to the selected operator
                    if "+" in printline or "-" in printline or "/" in printline or "*" in printline:  # <----  determine what the operator was because there already was one
                        if "+" in printline:
                            templine = '+'
                        if "-" in printline:
                            templine = '-'
                        if "*" in printline:
                            templine = '*'
                        if "/" in printline:
                            templine = '/'
                        if preline[0] != "-":  # <---- ensure the operand that exists isn't just a negative symbol from the preline
                            printline[printline.index(templine)] = operand  # <---- replace the old operator with the new one. going from addition to subtraction etc...
                        else:
                            printline.append(operand)  # <---- it was a negative, just append the new operand to the end of the line and move forward

                        
                    else:   # <---- otherwise, there were no prior operators so set the operand to the current selection and update the printed line
                        operand = choiceList[len(sendInput)-1]
                        printline.append(choiceList[len(sendInput)-1])
                        
            elif len(sendInput) == 18:  # <---- if the pointer is selected to the decimal point
                predot = preline.count('.')     # <----  count decimal places in the "before the operator" list
                postdot = postline.count(".")   # <----  count decimal places in the "after the operator" list
                if operand == "":   # <---- if there is no operand, you're in the "before the operator list",
                    if predot > 0:  # <----  if there is a decimal place already there, do nothing, can't have multiple decimal places in one half of an equation
                        pass
                    else:       # <----  otherwise
                        preline.append(".")    # <----  add a decimal place to the end of the "before the operator list"
                        printline.append(".")  # <----  add decimal place to the end of the printed line

                elif operand in ["-","+","*","/"]:  # <----  if there is an operator alraedy set
                    if postdot > 0:  # <----  if there is a decimal place in the "after the operator list"
                        pass  # <---- do nothing
                    else:   # <---- otherwise
                        postline.append(".")  # <---- add decimal to the end of teh "after the operator list"
                        printline.append(".")   # <----  add decimal place to the end of the printed line
                    
            
            elif len(sendInput) == 17:  # <----  if the pointer is at the equals sign
                if len(preline) != 0 and len(postline) != 0 and postline[len(postline)-1] != ".":    # <----  if there are numbers before and after the operator
                    answerlist = preline + [operand] + postline  # <----  make a list of the pre list, the operator, and the post list

                    answer = "".join([str(x) for x in answerlist])  # <----  join the list above into a string
                    answer = round(eval(answer),2)  # <----  evaluate the string (which is an equation), round the result to 2 decimal places
                    answer = str(answer)  # <----  reconvert the answer to a string
                    answer = [x for x in answer] # <----  build a list consisting of 1 character length items

                    for x in range(6):  # <----  clear six lines down and move six lines up to prep the print area, clear the "after the operator list"
                                                # assign the "before the operator list" to the answer of the last equation. Reset the operand, reset the answer
                        sys.stdout.write('\x1b[1B')
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        sys.stdout.flush()
                    sys.stdout.write('\x1b[6A')
                    printline = answer[:]
                    preline = printline[:]
                    postline = []
                    operand = ""
                    answer = None
                else:   # <---- otherwise (not numbers before or after the operand, do nothing)
                    pass

            elif len(sendInput) == 3 and len(printline) == 0:  # <----  pointer is pointer is at zero but nothing is printed, don't pritn the zero.
                pass


            else:  # <----  otherwise, if there is no operator, add to the "before the operator" list and the print line, otherwise to the "after the operator list" and printline
                if operand == "":
                    printline.append(choiceList[len(sendInput)-1])
                    preline.append(choiceList[len(sendInput)-1])
                else:
                    printline.append(choiceList[len(sendInput)-1])
                    postline.append(choiceList[len(sendInput)-1])

            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminalSettings)  # <----  restore terminal settings so not process raw input

            bigPrint(printline,color)  # <----  print the printline
            sys.stdout.write('\x1b[6A')  # <----  move up siz lines

        
        if ord(char) == 3: # <----   keyboard input is eqaul to "CTRL C", restore settings and quit
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminalSettings)
            running = False
        if char == '\x1b':  # <----  input is not a the enter key
                                   # Read the next 2 characters to see what it is
            escape_sequence = '\x1b' + sys.stdin.read(2)  # <---- assign the next captured raw input seequance to an escape character
            # print(f"Escape sequence: {repr(escape_sequence)}")
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminalSettings)  # <---- restore regular input, all possible input has been captured
            

            if escape_sequence == '\x1b[D':  # <---- check if it ws the left arrow key

                # print(f"instructions array is {len(sendInput)} long")
                if len(sendInput) > 1:  # <---- pointer is to the right of the default position (quit)
                    # print(len(sendInput)-1)
                    sendInput.pop(len(sendInput)-2)  # <---- remove the second to last item in the sendIput list, which is a "space"
                    # print(f"instructions array is {len(sendInput)} long")
                    # print(sendInput)
                    for x in range(6):  # <----  clear six lines up, re-call the pointer to current position
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        sys.stdout.flush()
                    pointer(sendInput)
                else:  # <----  otherwise, the pointer is at the default position, going left needs to wrap around, so fill the sendInput list to the right-most position
                    sendInput = ['space','space','space','space','space','space','space','space','space','space','space','space','space','space','space','space','space','point']
                    # sendInput.append('point')
                    for x in range(6):  # <----  clear six lines up and draw the poitner at the right-most position
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        sys.stdout.flush()
                    pointer(sendInput)
            elif escape_sequence == '\x1b[C':  # <----  the key pressed was the right arrow key

                if len(sendInput) < len(choiceList):  # <---- the pointer is not at the rightmost position
                    sendInput.insert(0, 'space')  # <----  Add 'space' at the beginning of the sendInput list, which will push the pointer right
                    # print(f"instructions array is {len(sendInput)} long")
                    sys.stdout.write('\x1b[6A')  # <----  move up six lines
                    sys.stdout.write('\x1b[2K\r\x1b[K')  # <---- clear the current line
                    pointer(sendInput)  # <----  redraw the pointer
                    # sys.stdout.write('\x1b[1A')
                    # print(len(sendInput))
                else:  # <----  pointer is at the right-most position and the user hit the right arrow key, needs to wrap around to the first posiiton
                    sendInput = ['point'] # <---- reset the sendInput to the initial position at the left-most option
                    for x in range(6):  # <----  clear six lines up, this will eliminate the prior printed data to the right and left which would otherwise ghost
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        sys.stdout.flush()
                    pointer(sendInput)  # <----  re-draw the pointer at the initial locaiton (quit)
            


    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminalSettings)  # <----  restore terminal settings
    # bigPrint(printline)

clc()  # <----  run the calculator


# if for some reason, the program crashes, it is possible the terminal settings will be set to collect and display raw data ... not great
# run it two more times to restore the settings to the correct settings.  If that doesn't work, open a new code window and print the following in a python file
"""
variable = termios.tcgetattr(sys.stdin)
print(variable)
"""

# copy the printout, go back to your crashed vscode terminal
# run

"""
termios.tcgetattr(sys.stdin) = copied print line
"""

# this should be required, I think I got all the bugs out. . . famous last words.


