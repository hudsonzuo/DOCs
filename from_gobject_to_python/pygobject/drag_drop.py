#!/usr/bin/python
from gi.repository import Gtk, Gdk, GdkPixbuf

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF,TARGET_ENTRY_BOTH) = range(3)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drag and Drop Demo")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        hbox = Gtk.Box(spacing=12)
        vbox.pack_start(hbox, True, True, 0)

        self.treeview = DragSourceTreeView()
        self.drop_area = DropArea()

        hbox.pack_start(self.treeview, True, True, 0)
        hbox.pack_start(self.drop_area, True, True, 0)

        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, True, False, 0)

        self.add_targets()

    def add_targets(self, button=None):
        targets = Gtk.TargetList.new([])
        targets.add_image_targets(TARGET_ENTRY_PIXBUF,True)
        targets.add_text_targets(TARGET_ENTRY_TEXT)

        self.drop_area.drag_dest_set_target_list(targets)
        self.treeview.drag_source_set_target_list(targets)

        #self.drop_area.drag_dest_add_text_targets()
        #self.treeview.drag_source_add_text_targets()

class DragSourceTreeView(Gtk.TreeView):

    def __init__(self):
        Gtk.TreeView.__init__(self)
        model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        self.set_model(model)
        self.add_item("Item 1", "image")
        self.add_item("Item 2", "gtk-about")
        self.add_item("Item 3", "edit-copy")
        renderer = Gtk.CellRendererPixbuf()
        #column = Gtk.TreeViewColumn("icon", renderer)
        #self.append_column(column)
	self.insert_column_with_data_func(-1, 'icon',renderer, self.icon_set_func,None)
        renderer = Gtk.CellRendererText()
        #column = Gtk.TreeViewColumn("item", renderer)
        #self.append_column(column)
	self.insert_column_with_data_func(-1, 'item',renderer, self.item_set_func,None)


        #targets.add_image_targets(TARGET_ENTRY_PIXBUF, True)
        #self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, targets, DRAG_ACTION)
        self.drag_source_set(Gdk.ModifierType.BUTTON1_MASK,[],DRAG_ACTION)
        self.connect("drag-data-get", self.on_drag_data_get)
    def icon_set_func(self,tree_column, cell, model, iter, data):
        icon = model.get_value(iter, 1)
	cell.set_property("pixbuf", icon)
    def item_set_func(self,tree_column, cell, model, iter, data):
        item = model.get_value(iter, 0)
	cell.set_property("text", item)
    def on_drag_data_get(self, widget, drag_context, data, info, time):
        print self, widget, drag_context, data, info, time
        model,selected_iter = widget.get_selection().get_selected()
        if info == TARGET_ENTRY_TEXT:
            text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
            data.set_text(text, -1)
        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = self.get_model().get_value(selected_iter, COLUMN_PIXBUF)
            data.set_pixbuf(pixbuf)
        elif info == TARGET_ENTRY_BOTH:
            pixbuf = self.get_model().get_value(selected_iter, COLUMN_PIXBUF)
            data.set_pixbuf(pixbuf)
	    print 'got to BOTH'
            text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
            data.set_text(text, -1)
    def add_item(self, text, icon_name):
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon_name, 16, 0)
        self.get_model().append([text, pixbuf])


class DropArea(Gtk.Label):

    def __init__(self):
        Gtk.Label.__init__(self, "Drop something on me!")
        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)

        self.connect("drag-data-received", self.on_drag_data_received)

    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        print self, widget, drag_context,x,y, data, info, time
        if info == TARGET_ENTRY_TEXT:
            text = data.get_text()
	    print "Received text with",text
        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = data.get_pixbuf()
            width = pixbuf.get_width()
            height = pixbuf.get_height()
            print "Received pixbuf with width %spx and height %spx" % (width, height)
        elif info == TARGET_ENTRY_BOTH:
            pixbuf = data.get_pixbuf()
            width = pixbuf.get_width()
            height = pixbuf.get_height()
            print "Received pixbuf with width %spx and height %spx" % (width, height)
            text = data.get_text()
	    print "Received text with",text

win = DragDropWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
