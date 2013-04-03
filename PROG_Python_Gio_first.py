#! --*-- utf-8 --*--
#!/usr/bin/python2

from gi.repository import Gio
import sys

ff=Gio.File.new_for_commandline_arg(sys.argv[1])
ff_info=ff.query_info("*",Gio.FileQueryInfoFlags.NONE,None)
print ff_info.get_file_type()
print ff_info.get_content_type()
print ff_info.get_name()
print ff_info.get_size()
print ff_info.list_attributes("standard")
print ff_info.list_attributes("time")
print ff_info.list_attributes("unix")
print ff_info.list_attributes("mountable")
print ff_info.get_attribute_string("standard::content-type")
print ff_info.get_attribute_byte_string("standard::name")
print ff_info.get_attribute_uint64("time::created")
print ff_info.get_attribute_uint32("unix::gid")


ff_dev=Gio.File.new_for_path("/dev/sdb5")
ff_dev_info=ff.query_info("*",Gio.FileQueryInfoFlags.NONE,None)
print ff_dev_info.list_attributes("mountable")

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
gm=Gio.VolumeMonitor.get()
print "moutnted:"
mounted=gm.get_mounts()  #GMount
for it in mounted:
   print it.get_name()
   print it.get_root().get_path()  #a GFile
   print "-------------"
print "volumes:"   
voS=gm.get_volumes()
for vo in voS:
   print vo.get_name()
   print vo.get_uuid()
   print vo.get_drive().get_name()  #Drive
   print vo.get_mount()  #GMount
   print vo.get_identifier("unix-device")  #get /dev/sdXn
   print "====================="

