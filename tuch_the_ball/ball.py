import tkinter

def print_hellow(event):
    print('Hellow!')
    print((event))

root = tkinter.Tk()
button = tkinter.Button (root, text ="Button")
button.bind("Button-1", print_hellow)
button.pack()

root.mainloop()
 