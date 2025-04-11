from os import close

import pyqrcode
s="https://www.baidu.com"
ur1=pyqrcode.create(s)
ur1.svg("baidu.svg",scale=8)