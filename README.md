# easyTypeWriter module

This module lets you quickly add type writer sound effect for inputs to your python project

Main Users : 
1. Jarvis - command line personal assistant for windows , linux and mac. [click here to visit jarvis website](https://harshnative.github.io/JarvisWebsite)
2. 100's of little school project


install module using pip command
```shell
pip install easytypeWriter
```

### external dependencies required : 


1. playsound module

Install via - 
```python
pip install playsound
```



### To import in project - 
```python
from easyTypeWriter import typeWriter
```

Then make a object instance of EasyInput class

```python
obj = typeWriter.EasyInput()
```

Now set the paths to sound effect - 
```python
obj.setEnterAudioPath("ding3.wav path here")
obj.setKeyboardAudioPath("keysound.wav path here")
```

You can get sound effects from here

1. Enter key sound effect - 
[click here to directly download](https://drive.google.com/uc?export=download&id=1mN_-vyRsHWK8qsHP16ktL9G0XX3RCbB9) . If this does not work then download it from [github page](https://github.com/harshnative/easyTypeWriter_module_python/tree/master/easyTypeWriter)

2. keyboard key sound effect - 
[click here to directly download](https://drive.google.com/uc?export=download&id=1qGSaacUgs6MEoI18W0uQOTq5yYSwo_Iv) . If this does not work then download it from [github page](https://github.com/harshnative/easyTypeWriter_module_python/tree/master/easyTypeWriter)

Now just call the takeInput() method :

```python
x = obj.takeInput(makeSound = True , messagePrompt = "" , toReturn = False)
```

Above function returns the string that is inputted by the user to x 

Now it accepts three aruguments all of which as some default value also : 

1. makeSound - accepts a bool value whether it make a type writer sound or not , remember - it slows down keyboard input , so if someone as fast typing then they may struggle. By default it is True .

2.  message promt - accepts a string value for making a prompt for asking user for input like normal input message prompt. By default it is empty

```python 
input("here is the message")
```

3. toReturn - this module can return the everycharacter that the user enters without even pressing enter. By default it is False


### Other methods - 

All methods are called automatically by start_fileShare() method. 

1. obj.setTabSpaceValue(port) - to set a custom value for how many spaces should a tab consist of . By default it is setted to 4



### Sample program - 
```python 
from easyTypeWriter import typeWriter

obj = typeWriter.EasyInput()

# setting audio files paths - you can get them from here

# Enter key sound effect - 
# link - https://drive.google.com/uc?export=download&id=1mN_-vyRsHWK8qsHP16ktL9G0XX3RCbB9 . If the file is not available to download then you can download the file from here - https://github.com/harshnative/easyTypeWriter_module_python/tree/master/easyTypeWriter

# keyboard key sound effect
# link - https://drive.google.com/uc?export=download&id=1qGSaacUgs6MEoI18W0uQOTq5yYSwo_Iv . If the file is not available to download then you can download the file from here - https://github.com/harshnative/easyTypeWriter_module_python/tree/master/easyTypeWriter

obj.setEnterAudioPath("C:/users/UserName/desktop/ding3.wav")
obj.setKeyboardAudioPath("C:/users/UserName/desktop/keysound30.wav")
x = obj.takeInput(True , "input : " )

print(x)

# output - 

# input : 123

# 123
```

### Contibute - 

[Post any issues on github](https://github.com/harshnative/easyTypeWriter_module_python)

[Check out code on github](https://github.com/harshnative/easyTypeWriter_module_python)