import shutil
import os
shutil.rmtree('Memory')
shutil.rmtree('Info')
os.mkdir('Memory')
os.mkdir('Info')
os.remove('thoughts.txt')
op=open('thoughts.txt','w+')
op.close()
