#!/usr/bin/python
from gi.repository import Gtk
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.box=Gtk.Box();
	self.add(self.box)
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button,True,True,0)
        self.button = Gtk.Button(label="The Second Button")
	self.box.pack_start(self.button,True,True,0)

    def on_button_clicked(self, widget):
        print "Hello World"
	self.box.remove(self.button)
	win.show_all()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
