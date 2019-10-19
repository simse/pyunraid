from pyunraid.unraid import Unraid

PASSWORD = 'hotfla123As'

u = Unraid('192.168.0.4', 'root', PASSWORD)

#print(u.vms())

obj = u.users()[0]

obj.set_image('image.png')

#obj.destroy()



for attr in dir(obj):
   if hasattr( obj, attr ):
       if(attr.startswith('__')):
           continue

       print( "obj.%s = %s" % (attr, getattr(obj, attr)))
