import Tkinter as tk
import threading

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.canvas = tk.Canvas(self,width=850, height=400, bg="white", highlightthickness=0)
        
# ovals 1-6
        self.canvas.create_oval(50, 50, 100, 100, fill="yellow", tags ="Light_1")
        self.canvas.create_text(75, 75, text="1", fill="purple", font="Helvetica 26 bold underline", tags = "Text_1")
        self.canvas.create_oval(150, 50, 200, 100, fill="yellow", tags ="Light_2")
        self.canvas.create_text(175, 75, text="2", fill="purple", font="Helvetica 26 bold underline", tags = "Text_2")
        self.canvas.create_oval(250, 50, 300, 100, fill="yellow", tags ="Light_3")
        self.canvas.create_text(275, 75, text="3", fill="purple", font="Helvetica 26 bold underline", tags = "Text_3")
        self.canvas.create_oval(350, 50, 400, 100, fill="yellow", tags ="Light_4")
        self.canvas.create_text(375, 75, text="4", fill="purple", font="Helvetica 26 bold underline", tags = "Text_4")
        self.canvas.create_oval(450, 50, 500, 100, fill="yellow", tags ="Light_5")
        self.canvas.create_text(475, 75, text="5", fill="purple", font="Helvetica 26 bold underline", tags = "Text_5")
        self.canvas.create_oval(550, 50, 600, 100, fill="yellow", tags ="Light_6")
        self.canvas.create_text(575, 75, text="6", fill="purple", font="Helvetica 26 bold underline", tags = "Text_6")


# ovals 7-12
        self.canvas.create_oval(50, 150, 100, 200, fill="yellow", tags ="Light_7")
        self.canvas.create_text(75, 175, text="7", fill="purple", font="Helvetica 26 bold underline", tags = "Text_7")
        self.canvas.create_oval(150, 150, 200, 200, fill="yellow", tags ="Light_8")
        self.canvas.create_text(175, 175, text="8", fill="purple", font="Helvetica 26 bold underline", tags = "Text_8")
        self.canvas.create_oval(250, 150, 300, 200, fill="yellow", tags ="Light_9")
        self.canvas.create_text(275, 175, text="9", fill="purple", font="Helvetica 26 bold underline", tags = "Text_9")
        self.canvas.create_oval(350, 150, 400, 200, fill="yellow", tags ="Light_10")
        self.canvas.create_text(375, 175, text="10", fill="purple", font="Helvetica 26 bold underline", tags = "Text_10")
        self.canvas.create_oval(450, 150, 500, 200, fill="yellow", tags ="Light_11")
        self.canvas.create_text(475, 175, text="11", fill="purple", font="Helvetica 26 bold underline", tags = "Text_11")
        self.canvas.create_oval(550, 150, 600, 200, fill="yellow", tags ="Light_12")
        self.canvas.create_text(575, 175, text="12", fill="purple", font="Helvetica 26 bold underline", tags = "Text_12")



# ovals 13 - 15
        self.canvas.create_oval(50, 250, 100, 300, fill="yellow", tags ="Light_13")
        self.canvas.create_text(75, 275, text="13", fill="purple", font="Helvetica 26 bold underline", tags = "Text_13")
        self.canvas.create_oval(150, 250, 200, 300, fill="yellow", tags ="Light_14")
        self.canvas.create_text(175, 275, text="14", fill="purple", font="Helvetica 26 bold underline", tags = "Text_14")
        self.canvas.create_oval(250, 250, 300, 300, fill="yellow", tags ="Light_15")
        self.canvas.create_text(275, 275, text="15", fill="purple", font="Helvetica 26 bold underline", tags = "Text_15")



        self.canvas.pack(side="top", fill="both", expand=True)
        # self.draw_light()
        # self.aThing()

    def draw_light(self):

        for a in xrange(1,16):
            string = "Light_" + str(a)
            stringTwo = "Text_" + str(a)
            self.canvas.itemconfig(string, fill="blue")
            self.canvas.itemconfig(stringTwo, fill="blue")

            print(string)

    def draw_light_two(self):

        for a in xrange(1,16):
            string = "Light_" + str(a)
            stringTwo = "Text_" + str(a)
            self.canvas.itemconfig(string, fill="red")
            self.canvas.itemconfig(stringTwo, fill="red")

            print(string)

        # self.after(1000, self.draw_light)

    def aThing(self):
        print("does a")
        self.draw_light_two()


def main():
    app = App()
    app.mainloop()
    app.aThing()



if __name__ == "__main__":
    main()




