from tkinter import * 
import speedtest

root = Tk()

root.title("Internet speed test")
root.geometry("360x600")
root.resizable(False,False)
root.config(bg="#1a212d")

def Check():
    test = speedtest.Speedtest()
    Uploading =round( test.upload()/(1024*1024),2)
    upload1.config(text=Uploading)
    print(Uploading)
    
    Downloading =round( test.download()/(1024*1024),2)
    download.config(text=Downloading)
    DOWNLOAD.config(text=Downloading)
    print(Downloading)
    
    
    servernames = []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)
    print(servernames)

imahe_icon = PhotoImage(file="speedtest\drive-download-20240713T155913Z-001\logo.png")
root.iconphoto(False,imahe_icon)

#Images7
top = PhotoImage(file="speedtest/drive-download-20240713T155913Z-001/top.png")
Label(root,image=top,bg="#1a212d").pack()

MAin = PhotoImage(file="speedtest\drive-download-20240713T155913Z-001\main.png")
Label(root,image=MAin,bg="#1a212d").pack(pady=(40,0))

Button1 = PhotoImage(file="speedtest\drive-download-20240713T155913Z-001/button.png")
button = Button(root,image=Button1,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=Check).pack(pady=10)


Label(root,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)

Label(root,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)

Label(root,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)

Label(root,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)

Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)

Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)

Label(root,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=140,y=280)

Label(root,text="MBPS",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)

ping = Label(root,font="arial 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")
ping.config(text="00")

download = Label(root,font="arial 13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")
download.config(text="00")


upload1 = Label(root,font="arial 13 bold",bg="#384056",fg="white")
upload1.config(text="00")
upload1.place(x=290,y=60,anchor="center")


DOWNLOAD = Label(root,font="arial 40 bold",bg="#384056",fg="white")
DOWNLOAD.place(x=185,y=350,anchor="center")
DOWNLOAD.config(text="00")

root.mainloop()