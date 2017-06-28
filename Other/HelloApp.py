#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import types
import bs4
from PIL import Image
from Tkinter import *
try:
	import cStringIO as cStringIO
except ImportError:
	import StringIO
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)
        

app = Application()
app.master.title('Hello')
app.mainloop()