from os import name
import socket
from _thread import *
from tkinter import *
from PIL import ImageTk,Image


# message_show = ""
chat = ""
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

message_window = Tk()
message_window.geometry("500x300")
message_window.resizable(0,0)

#bg of message box
bg_of_message = ImageTk.PhotoImage(Image.open("final_message_box.py\message_box_bg.png"))
bg_place = Label(image = bg_of_message)
bg_place.place(x=0,y=0)

#welcome
welcome = Label(message_window,text = "welcome",font=("Pattaya",30),fg = "#ffffff",bg = "#ff6666")
welcome.place(x=200,y=20)

#name
name_label = Label(message_window,text = "Please Enter your name:",font=("Pattaya",14),bg = "#ff6666")
name_label.place(x=30,y=80)
name = StringVar()
name_entry = Entry(bd= 1,bg = "#ffffff",font= ("Arial",18),width = 20,textvariable=name)
name_entry.place(x=230,y=80)

#host
host_label = Label(message_window,text = "Please Enter Host:",font=("Pattaya",14),bg = "#ff6666")
host_label.place(x=30,y=140)
host = StringVar()
host_entry = Entry(bd= 1,bg = "#ffffff",font= ("Arial",18),width = 20,textvariable=host)
host_entry.place(x=230,y=142)

#port
port_label = Label(message_window,text = "Please Enter Port No.:",font=("Pattaya",14),bg = "#ff6666")
port_label.place(x=30,y=200)
port = StringVar()
port_entry = Entry(bd= 1,bg = "#ffffff",font= ("Arial",18),width = 20,textvariable=port)
port_entry.place(x=230,y=200)



def sending(name):
    global server
    global chat
    data =name+": "+ chat.get()
    
    send_data = data.encode()
    server.send(send_data)

    

img = "final_message_box.py\\bg.png"

#creating main function\working
def mainwindow(client_name,host_no,port_no):
    global chat
    port_no = int(port_no)
    
    server.connect((host_no,port_no))

    message_window.destroy()
    
    main= Tk()
    main.geometry("400x500")
    main.resizable(0,0)

    #mainbg
    image = Image.open(img)
    bg = ImageTk.PhotoImage(image)

    label_bg = Label(main,image = bg)
    label_bg.place(x=0,y=0)

    chat_box = Label(main,text = "Chat",font=("Pattaya",30),fg = "#3b323b",bg = "white")
    chat_box.place(x=20,y=15)

    box = Label(main,text = "Box",font=("Pattaya",30),fg = "#ff6666",bg = "white")
    box.place(x=100,y=15)
    def reciving():
        global server
        
    
        while True:
            try:
                recive_data = server.recv(2048)
                message_show.insert(END,recive_data.decode()+"\n \n",)
            except:
                message_show.insert(END,"Error")


        


    message_show = Text(main,width = 32,font = ("",15),height=16, fg = "white",bg = "#3b323b")
    message_show.place(x=20,y=60)


    
    chat = StringVar()
    chat_entry = Entry(main,textvariable=chat,width = 25,font = ("",15))
    chat_entry.place(x=20,y=450)

    
    send_button = Button(main,text = "Send",bg = "#42ff7c",fg = "black",\
        command = lambda:sending(client_name),width = 5)
    send_button.place(x=320,y=450)




    start_new_thread(reciving,())







    main.mainloop()











#submit Button
but_sub  = Button(message_window,bg = "#42ff7c",fg = "black",width = 10,\
    text = "Submit",height = 2,command = lambda:mainwindow(name.get(),host.get(),port.get()))
but_sub.place(x=200,y=250)





message_window.mainloop()