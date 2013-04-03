#!/usr/bin/env python

# python-gtk-webkit presentation program.
# Copyright (C) 2009,2011 by Akkana Peck.
# Share and enjoy under the GPL v2 or later.

import sys, os
import gtk, gobject
import webkit

class PresoViewer(gtk.Window):
    def __init__(self, url):

        # Are we making screenshots? TODO: make this a command-line param.
        self.make_screenshots = True
        self.imgnum = 0

        # Size the audience will see (used for converting to images):
        self.displaywidth = 1024
        self.displayheight = 768
        # Size of the window we'll actually display:
        self.fullwidth = 1366
        self.fullheight = 768

        gtk.Window.__init__(self)

        # set the size to the size of my laptop:
        self.set_default_size(self.fullwidth, self.fullheight)
        # Optionally, run fullscreen (comment out if not desired):
        self.fullscreen()

        self._browser= webkit.WebView()
        self.add(self._browser)
        self.connect('destroy', gtk.main_quit)

        self._browser.connect("key-press-event", self.key_press_event)

        self._browser.open(url)    # throw err if url isn't defined
        self.show_all()

    def screenshot(self) :
        pixmap = self.get_snapshot(gtk.gdk.Rectangle(0, 0,
                                                     self.displaywidth,
                                                     self.displayheight))
        pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8,
                                self.displaywidth, self.displayheight)
        pixbuf.get_from_drawable(self.window, self.get_colormap(),
                                 0, 0, 0, 0,
                                 self.displaywidth, self.displayheight)
        pixbuf.save("screenshot%03d.jpg" % self.imgnum, "jpeg")

    def key_press_event(self, widget, event) :
        if event.keyval == gtk.keysyms.q and \
                 event.state == gtk.gdk.CONTROL_MASK :
            print "ctrl-Q"
            gtk.main_quit()

        elif event.string == ' ' :
            self.imgnum += 1

            # If we're in screen-shooting mode, save the current slide:
            if self.make_screenshots :
                self.screenshot()
                return False
             
        return False     # False means we haven't handled, pass event on

if __name__ == "__main__":
    if len(sys.argv) <= 1 :
        print "Usage:", sys.argv[0], "url"
        sys.exit(0)

    # Figure out if it's a filename or a url
    url = sys.argv[1]
    if url.find(':') < 0 :
        if url[0] == '/' :
            url = 'file://' + url
        else :
            url = 'file://' + os.getcwd() + '/' + url

    gobject.threads_init()
    webbrowser = PresoViewer(url)
    gtk.main()

