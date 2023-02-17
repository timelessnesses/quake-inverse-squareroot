import os

linuxes = [x for x in os.listdir('dist/') if 'linux' in x]

os.system('auditwheel repair dist/%s -w dist/ --plat x86_64' % linuxes[0])