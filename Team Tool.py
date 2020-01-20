from tkinter import *
from win32api import GetSystemMetrics
from tkinter import ttk
user32 = ctypes.windll.user32
scrWidth = user32.GetSystemMetrics(0)
scrHeight = user32.GetSystemMetrics(1)

def Root():
    root = Tk()
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))#sets the window to full screen
    root.focus_set()
    root.bind("<Escape>", lambda e: root.destroy())
