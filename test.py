from pyunraid.unraid import Unraid

PASSWORD = 'hotfla123As'

u = Unraid('http://192.168.0.4', 'root', PASSWORD)

#print(u.vms())

obj = u.vms()[1]

obj.force_stop()

for attr in dir(obj):
   if hasattr( obj, attr ):
       if(attr.startswith('__')):
           continue

       print( "obj.%s = %s" % (attr, getattr(obj, attr)))
