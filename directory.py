import os
import re
path='E:\GIDownloadLibrary\GI-Download-Library-main\src'
files= os.listdir(path)
for file in files:
    f = open(path+'\\'+file,'r')
    content=f.read()
    print(path+'\\'+file+'已加载')
    link_find = re.findall(r'(https?://[a-zA-Z0-9\.\?/%-_]*)',content)
    output=str(link_find)
    print(output+'已写入\n')
    f=open('E:\GIDownloadLibrary\GI-Download-Library-main\output.dsdb','a')
    f.write(output)
