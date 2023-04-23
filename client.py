import socket
from threading import Thread
import random
from tkinter import *
port = 6000
ip = '127.0.0.1'



def createTicket():
    global gameWindow
    global ticketGrid
    # Ticket Frame
    mianLable = Label(gameWindow, width=65, height=16,relief='ridge', borderwidth=5, bg='white')
    mianLable.place(x=95, y=119)

    xPos = 105
    yPos = 130
    for row in range(0, 3):
        rowList = []
        for col in range(0, 9):
            if(platform.system() == 'Darwin'):
                boxButton = Button(gameWindow,
                font = ("Chalkboard SE",18),
                borderwidth=3,
                pady=23,
                padx=-22,
                bg="#fff176",
                highlightbackground='#fff176',
                activebackground='#c5e1a5') 


                boxButton.place(x=xPos, y=yPos)
            else:
                boxButton = tk.Button(gameWindow, font=("Chalkboard SE",30), width=3, height=2,borderwidth=5, bg="#fff176")
                boxButton.place(x=xPos, y=yPos)

            rowList.append(boxButton)
            xPos += 64
        ticketGrid.append(rowList)
        xPos = 105
        yPos +=82

def placeNumbers():
    global ticketGrid, currentNumberList
    
    # get 5 random columns from the grid
    randomColList = []
    for i in range(3):
        randomCol = []
        counter = 0
        while (counter < 5):
            randNum = random.randint(0, 8)
            if randNum not in randomCol:
                randomCol.append(randNum)
                counter += 1
        randomColList.append(randomCol)
    
    # create a container for the numbers
    numberContainer = {0: [1, 11, 21, 31, 41, 51, 61, 71, 81],
                       1: [2, 12, 22, 32, 42, 52, 62, 72, 82],
                       2: [3, 13, 23, 33, 43, 53, 63, 73, 83],
                       3: [4, 14, 24, 34, 44, 54, 64, 74, 84],
                       4: [5, 15, 25, 35, 45, 55, 65, 75, 85],
                       5: [6, 16, 26, 36, 46, 56, 66, 76, 86],
                       6: [7, 17, 27, 37, 47, 57, 67, 77, 87],
                       7: [8, 18, 28, 38, 48, 58, 68, 78, 88],
                       8: [9, 19, 29, 39, 49, 59, 69, 79, 89]}
    
    # place the numbers on the grid
    for i in range(3):
        for j in randomColList[i]:
            series = numberContainer[j]
            number = series[random.randint(0, len(series)-1)]
            ticketGrid[i][j].config(text=str(number), font=("Helvetica", 14))
            currentNumberList.append(number)



def gameWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global dice
    global winingMessage
    global resetButton
    global flashNumberLabel


    gameWindow = Tk()
    gameWindow.title("Tambola Family Fun")
    gameWindow.geometry('800x600')

    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas2 = Canvas( gameWindow, width = 500,height = 500)
    canvas2.pack(fill = "both", expand = True)

    # Display image
    canvas2.create_image( 0, 0, image = bg, anchor = "nw")

    # Add Text
    canvas2.create_text( screen_width/4.5,50, text = "Tambola Family Fun", font=("Chalkboard SE",50), fill="#3e2723")

    createTicket()
    placeNumbers()


    # Flash Number Label
    flashNumberLabel = canvas2.create_text(400,screen_height/2.3, text = "Waiting for other players to join...", font=("Chalkboard SE",30), fill="#3e2723")

    gameWindow.resizable(True, True)
    gameWindow.mainloop()



def saveName():
    global server
    global playerName
    global nameEntry
    global nameWindow

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    server.send(playerName.encode)
def receivedMsg():
    pass

def setup():
    global server
    global ip
    global port
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,port))

    thread = Thread(target=receivedMsg)
    thread.start()

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow  = Tk()
    nameWindow.title("Tambola")
    nameWindow.attributes('-fullscreen',True)


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

setup()

# Boilerplate Code