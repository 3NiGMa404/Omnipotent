import shutil
import os
shutil.rmtree('Info')
os.mkdir('Info')
os.makedirs('Info/OPINIONS')
os.remove('thoughts.txt')
op=open('thoughts.txt','w+')
op.close()
os.remove('memory_file.py')
op2=open('memory_file.py','w+')
op2.write('memory_dict={}')
op2.close()

