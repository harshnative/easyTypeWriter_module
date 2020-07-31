from threading import *
from playsound import playsound


# creating class to implement custom getch of msvcrt module getch fucntion for windows and linux seperately
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


# class of custom getch function for unix system
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# class for custom module of getch function for windows system 
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


# creating object of getch class
getch = _Getch()


# thread for enter key sound
class enterSound(Thread):
    # function name should be run 
    def run(self):
        playsound('ding3.wav')



# function to play keyboard sound using 
def sound():
    playsound('keysound.wav')

# object for enter key sound 
sound2 = enterSound()


# main module class
class EasyInput:
    
    # constructor
    def __init__(self):

        # tab space - how many spaces will tab make in string
        self.tabValue = 4

        # byte code character dictionary
        self.dict = {
            # numbers - 

                b'1' : "1" , 
                b'2' : "2" , 
                b'3' : "3" , 
                b'4' : "4" , 
                b'5' : "5" , 
                b'6' : "6" , 
                b'7' : "7" , 
                b'8' : "8" , 
                b'9' : "9" , 
                b'0' : "0" , 

            # characters Upper case - 

                b'Q' : "Q" , 
                b'W' : "W" , 
                b'E' : "E" , 
                b'R' : "R" , 
                b'T' : "T" , 
                b'Y' : "Y" , 
                b'U' : "U" , 
                b'I' : "I" , 
                b'O' : "O" , 
                b'P' : "P" , 
                b'A' : "A" , 
                b'S' : "S" , 
                b'D' : "D" , 
                b'F' : "F" , 
                b'G' : "G" , 
                b'H' : "H" , 
                b'J' : "J" , 
                b'K' : "K" , 
                b'L' : "L" , 
                b'Z' : "Z" , 
                b'X' : "X" , 
                b'C' : "C" , 
                b'V' : "V" , 
                b'B' : "B" , 
                b'N' : "N" , 
                b'M' : "M" , 

            # characters lower case -

                b'q' : "q" , 
                b'w' : "w" , 
                b'e' : "e" , 
                b'r' : "r" , 
                b't' : "t" , 
                b'y' : "y" , 
                b'u' : "u" , 
                b'i' : "i" , 
                b'o' : "o" , 
                b'p' : "p" , 
                b'a' : "a" , 
                b's' : "s" , 
                b'd' : "d" , 
                b'f' : "f" , 
                b'g' : "g" , 
                b'h' : "h" , 
                b'j' : "j" , 
                b'k' : "k" , 
                b'l' : "l" , 
                b'z' : "z" , 
                b'x' : "x" , 
                b'c' : "c" , 
                b'v' : "v" , 
                b'b' : "b" ,
                b'n' : "n" , 
                b'm' : "m" , 

            # upper num line - 

                b'!' : "!" , 
                b'@' : "@" , 
                b'#' : "#" , 
                b'$' : "$" , 
                b'%' : "%" , 
                b'^' : "^" , 
                b'&' : "&" , 
                b'*' : "*" , 
                b'(' : "(" , 
                b')' : ")" , 

            # other special characters - 

                b'`' : "`" ,
                b'~' : "~" ,
                b'-' : "-" ,
                b'_' : "_" ,
                b'=' : "=" ,
                b'+' : "+" ,
                b'[' : "[" ,
                b']' : "]" ,
                b'{' : "{" ,
                b'}' : "}" ,
                b'\\' : "\\" ,
                b'|' : "|" ,
                b'"' : '"' ,
                b"'" : "'" ,
                b';' : ";" ,
                b':' : ":" ,
                b'/' : "/" ,
                b'?' : "?" ,
                b'.' : "." ,
                b'>' : ">" ,
                b'<' : "<" ,
                b',' : "," ,
        }

    
    # set tab space value function only pass positive integer
    def setTabSpaceValue(self, value):
        try:
            self.tabValue = int(value)
            if(self.tabValue < 0):
                raise ValueError("please pass only positive integer value to setTabSpaceValue function")
        except Exception:
            raise ValueError("please pass only positive integer value to setTabSpaceValue function")


    # main function of the module
    def takeInput(self , makeSound = False , messagePrompt = "" , toReturn = False):
        string = messagePrompt
        messageLength = len(messagePrompt)

        while(1):
            
            #printing the string to show the visual output 
            print("\r{}".format(string) , end = "")
            x = getch()
            
            # if the item is not found in dictionary
            if(self.dict.get(x) == None):
                
                # if the key pressed is enter
                if(x == b"\r"):

                    # making sound
                    if(makeSound):
                        sound2.start()

                    # returning the string by cutting the message prompt from the string
                    return string[messageLength:]

                # if the key pressed is backspace
                elif(x == b"\x08"):

                    if(makeSound):
                        sound()

                    l = len(string)

                    # backspace should not earse the message prompt itself
                    if(l <= messageLength):
                        pass
                    else:

                        # erasing the string element by one for one backspace
                        string = string[:l-1]
                        print("\r" , end = "")

                        # clearing the line so that new backspaced line can be printed when teh while loop starts
                        while(l):
                            print(" " , end = "")
                            l -= 1

                # if the key pressed is backspace the add " " to the string 
                elif(x == b' '):
                    if(makeSound):
                        sound()
                    string = string + " "

                # if the key pressed is tab then add ( " " * self.tabValue ) to teh string 
                elif(x == b'\t'):
                    if(makeSound):
                        sound()
                    for _ in range(self.tabValue):
                        string = string + " "

                # if a unrecognised key is pressed then module does nothing
                else:
                    pass
            
            # adding value from the dictionary to the string
            else:
                if(makeSound):
                    sound()
                y = self.dict.get(x)
                string = string + y

            # returning if required
            if(toReturn):
                return string[messageLength:]
            

# for testing purpose only
if __name__ == "__main__":
    obj = EasyInput()            
    print("started")
    x = obj.takeInput(True , "input : " )
    print("\n" , x , sep= "")