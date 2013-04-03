#!/usr/bin/python
from gi.repository import Gtk, Gdk

class drag_treeview_win(Gtk.Window):
   def __init__(self): 
      Gtk.Window.__init__(self,title='find truth')
      self.set_size_request(400, 300)
      box=Gtk.Box()
      self.add(box)
      model=Gtk.TreeStore(str)
      model.append(None,['today'])
      model.append(None,['tommorw'])
      treeview=Gtk.TreeView.new_with_model(model)
      render=Gtk.CellRendererText()
      column=Gtk.TreeViewColumn("date",render,text=0)
      treeview.append_column(column)
      targets = Gtk.TargetList.new([])
      targets.add_text_targets(0)
      treeview.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK,targets,Gdk.DragAction.COPY)
      treeview.connect("drag_data_get", self.drag_get_data)
      treeview.enable_model_drag_dest(targets,Gdk.DragAction.COPY)
      treeview.connect("drag_data_received",self.drag_received_data)

      sw=Gtk.ScrolledWindow()
      box.add(sw)
      sw.add(treeview)
   def drag_get_data(self, treeview, context, selection, target_id,etime):
      pass
   def drag_received_data(self, treeview, context, x, y, selection,info, etime):
      pass

win=drag_treeview_win()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
