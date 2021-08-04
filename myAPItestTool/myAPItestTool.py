import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.scrolledtext import ScrolledText
from threading import Thread
import requests as rq
import time
import os

def response():
    global textarea
    resp = eval(rq.get("http://127.0.0.1:8000/api/crystals/").text)[0]
    textarea.insert("1.0", resp)

def ClossApp():
    global winMain
    winMain.destroy()
    os._exit(0)

def countdown(num_of_secs):
    global controllerStatus,TimeStr,timecountroller,countitem
    timecountroller = False
    while num_of_secs:
        if controllerStatus:
            TimeStr.set('{:02d}:{:02d}'.format(0, 0))
            controllerStatus = False
            timecountroller = False
            countitem = 1
            break
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        TimeStr.set(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1
    TimeStr.set('{:02d}:{:02d}'.format(0, 0))
    timecountroller = True

def Start():
    global controllerStatus,timecountroller,loopRQ,textarea,SecondInput,countitem,Startbutton,Stopbutton
    Startbutton["state"] = tk.DISABLED
    Stopbutton["state"] = tk.NORMAL
    try:
        textarea.delete("1.0",tk.END)
    except:
        pass
    try:
        Second = int(SecondInput.get())
    except:
        Stop()
        messagebox.showerror("Error","Entry value only integer,not string")
        return None
    if Second < 0:
        Stop()
        messagebox.showerror("Error","Don't enter negative values")
        return None
    elif Second >= 6000:
        Stop()
        messagebox.showerror("Error","The line of sight is 6000")
        return None
    time.sleep(0.3)
    controllerStatus = False
    countitem = 1
    loopRQ = Thread(target=LoopRQ, args=(Second,))
    timecountdownS = Thread(target=countdown, args=(Second,))
    response()
    textarea.insert("1.0", f"---------------- No.{countitem} ----------------\n")
    timecountdownS.start()
    loopRQ.start()
    
    
def LoopRQ(seconds):
    global controllerStatus,timecountroller,TimeStr,textarea,countitem
    while controllerStatus == False:
        if timecountroller:
            textarea.insert("1.0", "\n\n")
            countitem += 1
            response()
            textarea.insert("1.0", f"---------------- No.{countitem} ----------------\n")
            time.sleep(0.3)
            timecountroller = False
            timecountdownL = Thread(target=countdown, args=(seconds,))
            timecountdownL.start()
        elif controllerStatus == True:
            controllerStatus == False
            break
        else:
            time.sleep(1)
            continue

def Stop():
    global controllerStatus,timecountroller
    controllerStatus = True
    time.sleep(0.5)
    Startbutton["state"] = tk.NORMAL
    Stopbutton["state"] = tk.DISABLED
    
fontName = "標楷體"
winMainName = "myAPItestTool"
winMainVersion = " ::v0.0.1 By-Jeremy.Huang"

#------主 GUI 介面建構語法--------------------------------------
winMain = tk.Tk()  # 產生 TK 介面物件
winMain.geometry('425x410') # 設定視窗大小
winMain.resizable(width=0, height=0) # 是否可以改變視窗大小
winMain.title(winMainName + winMainVersion) # 視窗標題
# winMain.iconbitmap('APPicon/Crawler.ico') # 視窗 icon
winMain.protocol("WM_DELETE_WINDOW",ClossApp)
#----------------------------------------------
style = ttk.Style()
style.configure('my.TButton', font=(fontName, 14))
#----------------------------------------------
winMain_A = tk.Frame(winMain)
winMain_A.grid(padx=15,pady=8,row=0,column=0)
winMain_B = tk.LabelFrame(winMain,text=" Response Display Area ",font=(fontName,11))
winMain_B.grid(padx=15,pady=8,row=1,column=0,columnspan=5)
#----------------------------------------------
Startbutton = ttk.Button(winMain_A,text='Start',width=5,style='my.TButton',compound="left",command=Start)
Startbutton.grid(padx=5,pady=10,row=0,column=0)
Stopbutton = ttk.Button(winMain_A,text='Stop',width=5,style='my.TButton',compound="left",command=Stop,state=tk.DISABLED)
Stopbutton.grid(padx=5,pady=10,row=0,column=1)
#----------------------------------------------
SecondStr = tk.StringVar()
SecondStr.set(600)
SecondInput = tk.Entry(winMain_A,relief='groove',justify='center',textvariable=SecondStr,bd=2,font=(fontName,13),width=6)
SecondInput.grid(padx=10,pady=10,row=0,column=2,sticky='e')
SecondLabel = tk.Label(winMain_A,anchor="w",text="Sec.",font=(fontName,11),compound='left',width=8)
SecondLabel.grid(padx=0,pady=10,row=0,column=3,sticky='w')
#----------------------------------------------
TimeStr = tk.StringVar()
TimeStr.set("{:02d}:{:02d}".format(0,0))
TimeStrLabel = tk.Label(winMain_A,anchor="e",textvariable = TimeStr,font=(fontName,20),compound='left',width=5)
TimeStrLabel.grid(padx=5,pady=10,row=0,column=4)
#----------------------------------------------
textarea = ScrolledText(winMain_B,font=(fontName,10),width=47,height=20)
textarea.grid(padx=20,pady=20,row=1,column=0)
#----------------------------------------------
winMain.mainloop()