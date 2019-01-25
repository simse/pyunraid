from pyunraid.unraid import Unraid

PASSWORD = 'EIido1YRp,Xe}N+eQdw1>Pw=nF6-eN5Bz)Tx>.u9^^k3nt)=Y%.U}AYlU>9?fduU'

u = Unraid('http://192.168.0.42', 'root', PASSWORD)

print(u.disks())
