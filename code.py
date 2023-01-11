from tkinter import *
from tkinter import filedialog

file_name =""

root = Tk()

root.title("Centering windows")
root.resizable(False, False)
window_height = 768
window_width = 593

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



def save_as(e):
    open_file = filedialog.asksaveasfile(mode ='w', defaultextension=".txt")
    if open_file is NONE:
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
    

def clear(e):
    entry.delete(1.0, END)

def open_file(e):
    global file_name
    file = filedialog.askopenfile(mode = 'r', filetype=[('text files','*.txt')] )
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)
    file_name = file.name


def save_existing(e):
    content = entry.get("1.0", END)
    if "/" in file_name:
        with open (file_name, "w") as f:
            f.writelines(content)
    else:
        save_as(e)

    
def quit_program(e):
   root.destroy()


entry= Text(root, height = 48, width = 74, wrap = WORD)
entry.place(x=0, y =0 )
entry.config(borderwidth=0)
entry.pack(side=TOP, padx=20, pady=20)

root.config(bg="#3b4252")
entry.config(bg="#3b4252", foreground="white", insertbackground="white", spacing1=5, spacing2=2,spacing3=5)
entry.config(font=('consolas', 10))


root.overrideredirect(1)


root.bind('<Control-q>', quit_program)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_existing)
root.bind('<Alt-c>', clear)


root.mainloop()
