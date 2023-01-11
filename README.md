# Noteee
This is a simple and minimal notepad. This was made using python tkinter. Has a very minimalist look and only works using keyboard bindings.


![image](https://user-images.githubusercontent.com/72241424/211765192-de1297c7-8355-4fd9-a415-50b4da886268.png)


Keybindings :-

Open existing file -> Ctrl-o

Clear the screen -> Alt-c

Save file -> Ctrl-s  

Quit -> Ctrl-q


To get the minimize/ maximize and close buttons (default) at the top, edit the code from
> root.overrideredirect(1)
to
> root.overrideredirect(0)


To convert the code into an application use
>pip install pyinstaller

>pyinstaller.exe --opnefile --icon=icon.ico code.py -w
