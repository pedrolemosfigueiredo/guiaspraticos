from Tkinter import *
class App:
    def __init__(self,master):
        frame = Frame(master); frame.pack()
        self.button = Button(frame, text='SALIR', fg ='red', command = frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text = 'HOLA', command = self.say_hi)
        self.hi_there.pack(side = LEFT)
        pass
    def say_hi(self):
        print 'Hey, caramba...!'
        pass
    pass
root = Tk(); app = App(root);
root.mainloop(); root.destroy()
