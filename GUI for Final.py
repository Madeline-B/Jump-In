from tkinter import *
from time import time, sleep
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg = "white")        
        self.master = master
        

    def Home(self):
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clicStartButton()
        self.startButton = Button(self, text="START",font = "Helvetica 16 ", bg = "white", command=self.clickStartButton, width = 25, height = 3)

        # place button at (0,0)
        self.startButton.place(x =(WIDTH/3.25) , y = (HEIGHT/2))

        # Makes the text
        self.text = Label(self, text="Jump In", font = "Helvetica 80 bold", bg = "white" )
        self.text.pack()


    def clickStartButton(self):
        print( " Start Clicked")
        self.startButton.destroy()
        self.text.pack_forget()
        self.colorPicker()

    def clickBack(self):
        root.attributes('-fullscreen',False)

    def colorPicker(self):
        self.pack(fill=BOTH, expand=1)

    ##        self.backButton = Button(self, text = "BACK", bg = "grey", command=self.clickBack, width = 10)
    ##        self.backButton.place(x = 25 , y = 350)

        self.text = Label(self, text="Rope Color", font = "Helvetica 60 bold", bg = "white" )
        self.text.pack()
        
        self.red = Button(self, text = "RED", bg = "red", command=self.clickRed, width = 15, height = 3)
        self.red.place(x = (WIDTH - 620) , y = (HEIGHT/3))

        self.blue = Button(self, text = "BLUE", bg = "blue", command=self.clickBlue, width = 15, height = 3)
        self.blue.place(x = (WIDTH - 460) , y = (HEIGHT/3))

        self.yellow = Button(self, text = "YELLOW", bg = "yellow", command=self.clickYellow, width = 15, height = 3)
        self.yellow.place(x = (WIDTH - 300) , y = (HEIGHT/3))

        self.purple = Button(self, text = "PURPLE", bg = "purple", command=self.clickPurple, width = 15, height = 3)
        self.purple.place(x = (WIDTH - 620) , y = (HEIGHT/1.75))

        self.green = Button(self, text = "GREEN", bg = "green", command=self.clickGreen, width = 15, height = 3)
        self.green.place(x = (WIDTH - 460) , y = (HEIGHT/1.75))

        self.orange = Button(self, text = "ORANGE", bg = "orange", command=self.clickOrange, width = 15, height = 3)
        self.orange.place(x = (WIDTH - 300) , y = (HEIGHT/1.75))
        
    def clearColor(self):
        self.red.destroy()
        self.blue.destroy()
        self.yellow.destroy()
        self.purple.destroy()
        self.green.destroy()
        self.orange.destroy()
        self.text.pack_forget()
        
    def clickRed(self):
        self.ropeColor = "red"
        self.clearColor()
        self.levelPicker()
        
    def clickBlue(self):
        self.ropeColor = "blue"
        self.clearColor()
        self.levelPicker()
        
    def clickYellow(self):
        self.ropeColor = "yellow"
        self.clearColor()
        self.levelPicker()
        
    def clickPurple(self):
        self.ropeColor = "purple"
        self.clearColor()
        self.levelPicker()
        
    def clickGreen(self):
        self.ropeColor = "green"
        self.clearColor()
        self.levelPicker()
        
    def clickOrange(self):
        self.ropeColor = "orange"
        self.clearColor()
        self.levelPicker()

    def levelPicker(self):
        self.pack(fill=BOTH, expand=1)
        
        #Creates the buttons
        self.easyButton = Button(self, text="SLOW",bg = "white",activebackground = "green", command=self.clickEasyButton, width = 20,height = 3)
        self.easyButton.place(x = (WIDTH/2.5),  y = (HEIGHT/3))
        self.medButton = Button(self, text="MEDUIM",bg = "white", activebackground = "yellow", command=self.clickMedButton, width = 20,height = 3)
        self.medButton.place(x = (WIDTH/2.5), y = (HEIGHT/2))
        self.hardButton = Button(self, text="FAST",bg = "white", activebackground = "red", command=self.clickHardButton, width = 20,height = 3)
        self.hardButton.place(x = (WIDTH/2.5), y = (HEIGHT/1.5))
        
        # Makes the text
        self.text = Label(self, text="Turning Speed", font = "Helvetica 70 bold", bg = "white" )
        self.text.pack()

    #clears the screen
    def clearLevel(self):
        self.easyButton.destroy()
        self.medButton.destroy()
        self.hardButton.destroy()
        self.text.pack_forget()
       
    # creates the jumprope    
    def createRope(self):
        self.x = 0
        self.score = 0
        self.clearLevel()
        self.c = Canvas(self, height = HEIGHT, width = WIDTH, bg="white")
        self.c.pack()

        
        self.oval = self.c.create_oval(325,140,(325+150),(140 +200), fill = "grey")
        
        self.l = self.c.create_line((WIDTH/2),HEIGHT,(WIDTH/2),(HEIGHT/2), width=5, fill = self.ropeColor)

        self.l2 = self.c.create_line((WIDTH - 200),HEIGHT,(WIDTH/2),(HEIGHT/2), width=5, fill = "white")
        self.l3 = self.c.create_line(WIDTH,(HEIGHT/2),(WIDTH/2),(HEIGHT/2), width=5, fill = "white")

        self.l4 = self.c.create_line(((WIDTH/2) + 200),0,(WIDTH/2),(HEIGHT/2), width=5, fill = "white")
        self.l5 = self.c.create_line((WIDTH/2),0,(WIDTH/2),(HEIGHT/2), width=5, fill = "white")

        self.l6 = self.c.create_line(200,((HEIGHT/2)- 250),(WIDTH/2),(HEIGHT/2), width=5, fill = "white")
        self.l7 = self.c.create_line(0,(HEIGHT/2),(WIDTH/2),(HEIGHT/2), width=5, fill = "white")

        self.l8 = self.c.create_line(((WIDTH/2)-200),HEIGHT,(WIDTH/2),(HEIGHT/2), width=5, fill = "white")
        

        #self.oval = self.c.create_oval(350+15,180+15,(435) ,(300), fill = "grey")
        self.scorepic = self.c.create_text((WIDTH/2),(HEIGHT/2),text = self.score,font = "Times 100 bold", fill = "black")

    # creates the rope animation   
    def turnRope(self):
        alist = [self.l, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8]
        print(self.x)
        self.c.itemconfig(alist[self.x], fill= "white")
        if (self.x == 7):
            self.c.itemconfig(alist[3], fill= "white")
            self.x = -1
            self.score += 1
            self.c.itemconfig(self.scorepic,text = self.score)
        if (self.x < 7):
            self.x += 1
        
        if (self.score == 3):
            self.x 
            self.endScreen()
        else:
            self.c.itemconfig(alist[self.x], fill= self.ropeColor)
            self.c.after(self.speed,self.turnRope)

    def clearRope(self):
        self.c.pack_forget()
        
    def endScreen(self):
        self.clearRope()
        self.text2 = Label(self, text="SCORE", font = "Helvetica 80 bold", bg = "white" )
        self.text2.place(x = 50, y = 35)

        self.scorepic2 = Label(self, text= self.score, font = "Helvetica 70 bold", bg = "white" )
        self.scorepic2.place(x = 200, y = 150)

        self.restart = Button(self, text="RESTART",font = "Helvetica 16 ", bg = "white", command = self.clickRestart, width = 20, height = 3)
        self.restart.place(x = 500, y = 50)


        self.newColor = Button(self, text="COLOR",font = "Helvetica 16 ", bg = "white", command = self.clickNewColor, width = 20, height = 3)
        self.newColor.place(x = 500, y = 175)

        self.newLevel = Button(self, text="SPEED",font = "Helvetica 16 ", bg = "white", command = self.clickNewSpeed, width = 20, height = 3)
        self.newLevel.place(x = 500, y = 300)
        
    def f(self):
        pass
    def clearEnd(self):
        #self.newLevel.destroy()
        self.restart.destroy()
        self.newColor.destroy()
        self.scorepic2.pack_forget()

    def clickRestart(self):
        print("restart Clicked")
        self.clearEnd()
        self.createRope()
        self.turnRope()
        

    def clickNewColor(self):
        print(" color Clicked")
        self.clearEnd()
        self.colorPicker()

    def clickNewSpeed(self):
        print(" new speed Clicked")
        self.clearEnd()
        self.levelPicker()
        
        
    def clickEasyButton(self):
        self.speed = 2000
        self.createRope()
        self.c.after(self.speed,self.turnRope)
        print(self.ropeColor)

    def clickMedButton(self):
        self.speed = 1000
        self.createRope()
        self.c.after(self.speed,self.turnRope)
        print(self.ropeColor)
        
    def clickHardButton(self):
        self.speed = 500
        self.createRope()
        self.c.after(self.speed,self.turnRope)
        print(self.ropeColor)

HEIGHT = 480
WIDTH = 800

root = Tk()
app = Window(root).Home()
root.wm_title("Jump In")
#root.attributes('-fullscreen',True)
root.geometry("{0}x{1}".format(WIDTH, HEIGHT))
root.mainloop()

