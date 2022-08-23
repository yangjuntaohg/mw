import os
import time
img_dir = os.path.abspath('../Campro/debug').split('src')[0] + "/img/"
print(os.path.abspath('../Campro/debug') + "/img/")
print(os.path.abspath('../Campro/debug').split('src'))
print(os.path.abspath('../Campro/debug').split('src')[0])
print(img_dir)
print(os.path.abspath('../Campro/debug') + "/img/{}.jpg".format(str(time.asctime())))
