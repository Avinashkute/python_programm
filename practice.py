

import os
def latest_file(filepath):
    files=os.listdir(filepath)
    file=[file1 for file1 in files if os.path.isfile(os.path.join(filepath,file1))]
    res=max(file,key=lambda x:os.path.getctime(os.path.join(filepath,x)))
    return res

path=r'C:\Users\Admin\Desktop\resume'
print(latest_file(path))