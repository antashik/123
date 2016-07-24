import tkinter

def button1_command():
    print ('button 1 default command')
def print_hellow(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num)
    print(event.x,event.y)
    #print(event.x_root, event.y_root)
    me = event.widget
    if me == button1:
        print('Hellow')
    elif me == button2:
        print('You press button2!')
    else :
        raise ValueError()


root = tkinter.Tk()
button1 = tkinter.Button(root, text="Button 1", command=button1_command)
button1.bind("<Button>", print_hellow)
button1.pack()

button2 = tkinter.Button(root, text="Button 2")
button2.bind("<Button>", print_hellow)
button2.pack()

root.mainloop()
 