op=open('sets.py', 'r')
rd=op.read()
op.close()

lines=rd.split('\n')
newlines=[]
listofbegs=[]
for i in lines:
    mod=i
    '''
    if '_n=' in i and not 'negatives' in i and not 'positives' in i:
        mod=i[:i.find(']')+1]+'+negatives'+i[i.find(']')+1:]
    elif '_p=' in i and not 'negatives' in i and not 'positives' in i:
        mod=i[:i.find(']')+1]+'+positives'+i[i.find(']')+1:]
    if '_n=' in i or '_p=' in i:
        first_bit=mod.split('=')[0].replace('_n','').replace('_p','')
        mod_first_bit='"'+first_bit.replace('_',' ').replace(' u',' you')+' "'                #Uncomment when formatting from beginning
        if 'nt' in mod_first_bit:
            mod_first_bit=mod_first_bit+','+str(mod_first_bit.replace('nt',"n't"))
            
        mod_first_bit='['+mod_first_bit+']'
        pos=mod.find('ves,')
        mod=mod[:pos+4]+mod_first_bit+mod[pos+4:]
        print(mod)
    first_bit_again=mod.split('=')[0]
    pos2=mod.find('],')
    mod=mod[:pos2+2]+'"!'+first_bit_again+'!"'+mod[pos2+2:]

    if not 'True' in mod:
        if 'noun' in mod:
            pos=mod.find(',)')
            mod=mod[:pos+1]+'True'+mod[pos+1:]
        else:
            pos=mod.find(',)')
            mod=mod.replace(',)',')')
'''
    first_bit_again_again_lol=mod.split('=')[0]
    if '_p=' in mod or '_n=' in mod:
        listofbegs.append(first_bit_again_again_lol)
    print(mod)
    newlines.append(mod)
newlines.append('all_resp=['+','.join(listofbegs)+']')
    
op=open('sets.py', 'w+')
op.write('\n'.join(newlines))
op.close()
