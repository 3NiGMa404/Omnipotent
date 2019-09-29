"""
Script: Omnipotent Lillypad AI2
Version: 0.9.6
Name: James Pinder (https://github.com/3NiGMa404)
Date: 2019-09-26
"""
print(__doc__)
import psutil
import os
path=os.path.realpath(__file__).replace(os.path.basename(__file__),'').replace('\\','/')
process = psutil.Process(os.getpid())
import progressbar
import colorama
colorama.init()
bar=progressbar.ProgressBar(max_value=13)
import random
os.system('cls')
bar.update(1)
print('\nloading datetime...',end='')
import datetime
print('done')
os.system('cls')
bar.update(2)
print('\nloading shutil...',end='')
import shutil
print('done')
os.system('cls')
bar.update(3)
print('\nloading textblob...',end='')
import textblob
print('done')
os.system('cls')
bar.update(4)
print('\nloading traceback...',end='')
import traceback
print('done')
os.system('cls')
bar.update(5)
print('\nloading pyaudio...',end='')
import pyaudio
print('done')
os.system('cls')
bar.update(6)
print('done')
os.system('cls')
bar.update(7)
print('\nloading spacy...',end='')
import spacy
print('done')
os.system('cls')
bar.update(8)
print('\nloading and starting pyttsx3...',end='')
import pyttsx3
engine = pyttsx3.init()
print('done')
os.system('cls')
print('\nloading sets...')
from sets import *
print('done')
os.system('cls')
bar.update(9)
print('\nloading databases...')
nlp = spacy.load("en_core_web_sm")
maleraw=open('male.txt','r').read().split('\n')
male=[]
for i in maleraw:
    male.append(i.lower())
print('done')
bar.update(10)
os.system('cls')
print('\nloading another database...')
femaleraw=open('female.txt','r').read().split('\n')
female=[]
for j in femaleraw:
    female.append(j.lower())
names=male+female
print('done')
bar.update(11)
os.system('cls')
print('\nloading memory...')
if not os.path.exists('Memory'):
    os.makedirs('Memory')
if not os.path.isfile('thoughts.txt'):
    x=open('thoughts.txt','w+')
    x.close()
if not os.path.exists('Info'):
    os.makedirs('Info')
print('done')
bar.update(12)
os.system('cls')
print('\nloading speech...')
def think(string):
    c=open('thoughts.txt','a+')
    c.write('\n'+str(datetime.datetime.now())+': '+string)
    c.close()
def say(text):
    from routput import ret
    ret(text)
def add_noun(name,Class,data=''):
    if not os.path.exists('Info/'+Class):
        os.makedirs('Info/'+Class)
    if os.path.isfile('Info/'+Class+'/'+name+'.txt'):   #Finish adding classes here
        openinfo=open('Info/'+Class+'/'+name+'.txt','a')
    else:
        openinfo=open('Info/'+Class+'/'+name+'.txt','w+')
    if Class==None:
        for i in os.listdir('Info/UNKNOWN'):
            for j in os.listdir('Info/'+'UNKNOWN'+i+'/'):
                if j==name+'.txt':
                    openinfo=open('Info/'+i+'/'+name+'.txt','a')    #Maybe make an unknown 'Class' folder as well, try to use male and female names for sorting otherwise
                    
                                               #Add something here to add data of gender whenever a PERSON class comes through
    if name in female:
        data=data+'\n/female'
    if name in male:
        data=data+'\n/male'
    openinfo.write(data)
    openinfo.close()
print('done')
bar.update(13)
os.system('cls')
def getinput():
    from ginput import git
    return git()
mynames=['omnipotent']
talkingto=input('who are you? ')
add_noun(talkingto,'PERSON')
conv=[]
positives=['yes','yep','for sure','affirmative','definitely',"i'm afraid so",'i think so']
neutral=['maybe','maybe, maybe not']
negatives=['no','nope','nah','definitely not',"i don't think so","i'm afraid not",'nae']

#os.makedirs('hi/who are you')

think('\nNEW SESSION')    
def find_response(convo):
    if convo[0].startswith('can you '):
        if convo[0].replace('can you ','') in things_i_can_do:
            saying=random.choice(can_u_p.responses)
            think('Chose "' + saying + '" from ' + str(can_u_p.responses))
            return saying
        else:
            saying=random.choice(can_u_n.responses)
            think('Chose "' + saying + '" from ' + str(can_u_n.responses))
            return saying
    if convo[0].startswith('cant you '):
        if convo[0].replace('cant you ','') in things_i_can_do:
            saying=random.choice(cant_u_p.responses)
            think('Chose "' + saying + '" from ' + str(cant_u_p.responses))
            return saying
        else:
            saying=random.choice(cant_u_n.responses)
            think('Chose "' + saying + '" from ' + str(cant_u_n.responses))
            return saying
    if convo[0].startswith('are you '):
        if convo[0].replace('are you ','') in things_i_am:
            saying=random.choice(are_u_p.responses)
            think('Chose "' + saying + '" from ' + str(are_u_p.responses))
            return saying
        else:
            saying=random.choice(are_u_n.responses)
            think('Chose "' + saying + '" from ' + str(are_u_n.responses))
            return saying
    if convo[0].startswith('arent you '):
        if convo[0].replace('arent you ','') in things_i_am:
            saying=random.choice(arent_u_p.responses)
            think('Chose "' + saying + '" from ' + str(arent_u_p.responses))
            return saying
        else:
            saying=random.choice(arent_u_n.responses)
            think('Chose "' + saying + '" from ' + str(arent_u_n.responses))
            return saying
    for i in range(len(convo)):
        if os.path.exists('Memory/'+str('/'.join(conv[i:len(convo)]))):
            think('Memory/'+str('/'.join(conv[i:len(convo)])) + ' exists')
            answers=os.listdir('Memory/'+'/'.join(convo[i:len(convo)]))
            if len(answers)>0:
                
                saying=random.choice(answers).lower()
                for i in all_resp:
                    saying=saying.replace(i.tag,random.choice(i.responses))
                think('chose ' + saying + ' from ' + str(answers))
                return saying


        think('checking for recognized patterns...')                   #Check for all of the sets' patterns
        count=0
        choices=[]
        for i in all_resp:
            for j in i.beginnings:
                if convo[-1].startswith(j):
                    if count<2:
                        count=count+1
                        choices.append(i.responses)
        if len(choices)>1:
            saying=random.choice(i.responses)
            think('chose '+saying+' from ' + str(i.responses))
            return saying
latestname=None
latestfemale=None
latestfemale=None
latestpronoun=None
latestname=None
def main():
    global conv, latestname, latestfemale, latestmale, latestpronoun, latestname
    think('getting input...')
    theysaid=str(getinput().lower().replace('/','').replace('\\','').replace('?','').replace('!',''))
    think('input before preprocessing: {}'.format(theysaid))
    doc=nlp(theysaid)
    theysaid=theysaid.replace(talkingto,'!speaker!')
    theysaid=theysaid.replace('did you know that','')
    if theysaid=='exit':
        think('Saving and exiting...')
        raise SystemExit('Saving and exiting')
    if theysaid=='reset':
        import reset
        raise SystemExit('Saving and exiting')
    for i in theysaid.split(' '):
        if i in male:
            latestmale=i
        if i in female:
            latestfemale=i
            print('setting latestfemale to {}'.format(latestfemale))
        if i in names:
            latestname=i
    
            
    for i in mynames:
        theysaid=theysaid.replace(i,'!speakingto!')
    
    person_in_it=False
    
    if theysaid.startswith('!speaker!'):
        add_noun(talkingto,'PERSON',theysaid.replace('!speaker!','').strip())
    pretheysaid=theysaid                                                    #Saving theysaid before replacing pronouns so we can add !pronoun! later
    for i in range(len(theysaid.split(' '))):
        if theysaid.split(' ')[i]=='he':
            theysaid.split(' ')[i]=latestmale
        if theysaid.split(' ')[i]=='she':
            theysaid.split(' ')[i]=latestfemale
            
    for i in male:
        if theysaid.startswith(i):
            add_noun(i.strip(),'PERSON',theysaid.replace(i,''))
            person_in_it=True
    for i in female:
        if theysaid.startswith(i):
            add_noun(i.strip(),'PERSON',theysaid.replace(i,''))
            person_in_it=True
    if not person_in_it:        
        for ent in doc.ents:                         #Detect names first and if there are no names then run this \/ \/
            add_noun(ent.text,ent.label_,'')
    
    theysaid=' '+pretheysaid+' '
    for n in names:
        for i in theysaid.split(' '):
            if i==n and n in male:
                latestpronoun=' he '
            if i==n and n in female:
                latestpronoun=' she '
    for i in [' he ',' she ']:
        theysaid=theysaid.replace(i,' !pronoun! ')
    for i in names:
        theysaid=theysaid.replace(' '+i+' ',' !name! ')
    for i in positives:
        theysaid=theysaid.replace(' '+i+' ',' !pos! ')
    for i in negatives:
        theysaid=theysaid.replace(' '+i+' ',' !neg! ')
    theysaid=theysaid.strip()
    for i in all_resp:
        for j in i.responses:
            theysaid=theysaid.replace(' '+j+' ',' '+i.tag+' ')
    theysaid_mod_is=None
    contractions=[['do not','dont'],['will not','wont'],['can not','cant'],['are not','arent'],['is not','isnt'],['were not','werent']]
    for i in contractions:
        theysaid=theysaid.replace(i[0],i[1])
    #conjunctions_a=[' is ',' are ',' isnt ',' arent ',' were ',' werent ',' can ',' cant ', ' do ', ' dont ',' will ',' wont ']
    think('input after preprocessing: {}'.format(theysaid))
    conv.append(theysaid)
    resp=find_response(conv)
    idk=False
    if resp==None:
        idk=True
        for i in range(len(conv)):
            if not os.path.exists('Memory/'+'/'.join(conv[i:len(conv)])):
                os.makedirs('Memory/'+'/'.join(conv[i:len(conv)]))
                                  
                                  
        conv=[]
        think('1: '+str(os.listdir()))
        os.chdir(path)
        think('2: '+str(os.listdir()))
        for i in os.listdir('Memory/'):             
            if len(os.listdir('Memory/'+str(i))) == 0:
                resp=str(i)
                    
    conv.append(resp)
    real_resp=' '+resp+' '
    if latestname!=None:
        real_resp=real_resp.replace('!name!',latestname)
    else:
        for i in real_resp.split(' '):
            if i=='!name!':
                latestname=random.choice(names)
                real_resp=real_resp.replace(i,latestname)
    for i in real_resp.split(' '):
        for n in names:
            if i==n and n in male:
                latestpronoun=' he '
            if i==n and n in female:
                latestpronoun=' she '
        if i == '!pronoun!':
            real_resp=real_resp.replace(' !pronoun! ',latestpronoun)
        
    real_resp=real_resp.replace('!pos!',random.choice(positives))

    real_resp=real_resp.replace('!neg!',random.choice(negatives))
    real_resp=real_resp.replace('!speakingto!',talkingto)
    real_resp=real_resp.replace('!speaker!',random.choice(mynames))
    for i in all_resp:
        real_resp=real_resp.replace(i.tag,random.choice(i.responses))
    real_resp=real_resp.strip()
    say(real_resp)
    for i in range(len(conv)):
        if not os.path.exists('Memory/'+'/'.join(conv[i:len(conv)])):
            os.makedirs('Memory/'+'/'.join(conv[i:len(conv)]))
            if idk:
                shutil.rmtree('Memory/'+resp+'/')
try:
    os.system('cls')
    while True:
        main()
except Exception as e:
    if e=='Saving and exiting':
        print(e)
    else:
        print('\nAn unexpected error occured...:\n\n' + traceback.format_exc())
        think(traceback.format_exc())
