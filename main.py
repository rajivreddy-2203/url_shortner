import pyshorteners
import pyperclip
from tkinter import *

shortner = Tk()
shortner.geometry('400x400')
shortner.title("URL Shortner")
shortner.configure(bg="#49A")

url = StringVar()
url_short_address = StringVar()

def urlShortner():
    urlAddress = url.get()
    urlShort = pyshorteners.Shortener().tinyurl.short(urlAddress)
    url_short_address.set(urlShort)

def copyUrl():
    url_short = url_short_address.get()
    pyperclip.copy(url_short)

Label(shortner, text="URL Shortner", font="Helvetica").pack(pady=(50,10))
Entry(shortner, textvariable=url).pack(pady=5)
Button(shortner, text="Shorten the URL", command=urlShortner).pack(pady=7)
Entry(shortner, textvariable=url_short_address).pack(pady=5)
Button(shortner, text="Copy URL", command=copyUrl).pack(pady=5)

shortner.mainloop()