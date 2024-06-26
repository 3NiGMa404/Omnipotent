"""
Script: Omnipotent Lillypad AI2
Version: 1.4.4
Name: James Pinder (https://github.com/3NiGMa404)
Date: 2024-01-10
"""
print(__doc__)

import colorama
colorama.init()

  #OKY TIME TO DO GPT STUFF
import os
path = os.path.realpath(__file__).replace(
    os.path.basename(__file__), '').replace(
    '\\', '/')




import progressbar


from itertools import product








bar = progressbar.ProgressBar(maxval=16)
bar.start()

os.system('cls')
bar.update(1)
print('\nloading datetime...', end='')
import datetime
import time
print('done')

os.system('cls')
bar.update(2)
print('\nloading custom things...', end='')
import commands





import _config_


print('done')

os.system('cls')
bar.update(3)
print('\nloading textblob...', end='')
import textblob
print('done')

os.system('cls')
bar.update(4)
print('\nloading traceback and warnings...', end='')
import traceback
import warnings
warnings.filterwarnings("ignore")

print('done')

os.system('cls')
bar.update(5)
print('\nloading random...', end='')
import random
print('done')

os.system('cls')
print("\nloading stuff I maybe don't need...", end='')
import euc_dist
import regex as re
bar.update(6)
print('done')


os.system('cls')
bar.update(7)
print('\nloading python utils...', end='')
import os
import inspect
import psutil

import shutil
process = psutil.Process(os.getpid())

print('done')

os.system('cls')
bar.update(8)
print('\nloading nlp stuff...', end='')
import spacy
import claucy
import nltk
from nltk.corpus import wordnet as wn


stemmer = nltk.stem.snowball.SnowballStemmer("english")
print('done')


os.system('cls')
bar.update(9)
print('\nloading sets...')
from sets import *
print('done')


os.system('cls')
bar.update(10)
print('\nloading databases...')


maleraw = open('male.txt', 'r').read().split('\n')
male = []
for i in maleraw:
    male.append(i.lower().strip())
femaleraw = open('female.txt', 'r').read().split('\n')
female = []
for j in femaleraw:
    female.append(j.lower().strip())
names = male + female
print('done')

os.system('cls')
bar.update(11)

print('\nloading another database...')
nlp = spacy.load("en_core_web_sm")
claucy.add_to_pipe(nlp)
print('done')

os.system('cls')
bar.update(12)
print('\nloading memory...')
from memory_file import memory_dict
if not os.path.isfile('thoughts.txt'):
    x = open('thoughts.txt', 'w+')
    x.close()
if not os.path.exists('Info'):
    os.makedirs('Info')
print('done')

os.system('cls')
bar.update(13)
print('\nloading inflection libaries...')
import lemminflect
import inflect
inflect = inflect.engine()

print('done')
os.system('cls')
bar.update(14)

print('\nloading generative AIs...')
from openai import OpenAI
import google.generativeai as genai
genai.configure(api_key=_config_.google_api_key)

print('done')
os.system('cls')
print('\nloading processes...')

os.system('python3 face_recognizer.py')

def think(line, string, statedatetime=True):
    c = open('thoughts.txt', 'a+')
    if statedatetime:
        c.write('\n' + str(datetime.datetime.now()) + '({}): '.format(line) + string)
    else:
        c.write('\n' + string)
    c.close()


think(inspect.getframeinfo(inspect.currentframe()).lineno,'\nNEW SESSION\n\n', statedatetime=False)
necessary_code=[os.path.basename(__file__),'commands.py','euc_dist.py','face_recognizer.py','inout.py','memory_file.py','sets.py','_config_.py']
lines_tot=0
chars_tot=0
for i in necessary_code:
    with open(i,'r') as r:
        lines_tot+=len(r.readlines())
        r.seek(0)
        chars_tot+=len(r.read())
think(inspect.getframeinfo(inspect.currentframe()).lineno,'Total code length is: {} lines, {} characters'.format(lines_tot,chars_tot))

def say(text):
    from inout import ret
    ret(text)

class Model:
    def __init__(self,Name, enabled, Add_to_Conv, Add_to_Prompt, Get_Response_Function, RPM):
        self.Name=Name
        self.enabled=enabled;
        self.ready=True
        self.Add_to_Conv=Add_to_Conv
        self.Add_to_Prompt=Add_to_Prompt
        self.Get_Response_Function=Get_Response_Function
        self.RPM=RPM
        self.last_time=0;

    def Get_Response(self,Conv):
        t=time.perf_counter()
        if (t-self.last_time)>(self.RPM/20) and self.enabled:
            self.last_time=t
            try:
                return self.Get_Response_Function(Conv).text.replace('\n','').replace('!','').replace('.','').replace("'",'') #.text is unfortunately Gemini-specific
            except:
                return False
        else:
            return False

            
            
        
def add_noun(name, Class, data=''):
    global mood
    if not os.path.exists('Info/' + Class):
        os.makedirs('Info/' + Class)
        
    if os.path.isfile('Info/' + Class + '/' + name +
                      '.txt'):  # Finish adding classes here
        openinfo = open('Info/' + Class + '/' + name + '.txt', 'a')
    else:
        openinfo = open('Info/' + Class + '/' + name + '.txt', 'w+')
    if not os.path.isfile('Info/OPINIONS/'+name+'.txt'):
        with open('Info/OPINIONS/'+name+'.txt','w+') as wr:                   #Yeah so make the file?!
            wr.write(str(max([-1, min([1, random.gauss(.2*mood[0], 0.3)])])))
            print('WRITING!')
    if Class == None:
        for i in os.listdir('Info/UNKNOWN'):
            for j in os.listdir('Info/' + 'UNKNOWN' + i + '/'):
                if j == name + '.txt':
                    # Maybe make an unknown 'Class' folder as well, try to use
                    # male and female names for sorting otherwise
                    openinfo = open('Info/' + i + '/' + name + '.txt', 'a')

    openinfo.write('\n' + data)
    openinfo.close()


print('done')
bar.update(15)
os.system('cls')


print('\ninitiating emotions...', end='')
# mood, polarity +happy -sad, subjectivity +passionate -calm
mood = [max([-1, min([1, random.gauss(0, 0.3)])]),
        max([-1, min([1, random.gauss(0, 0.2)])])]
st = 'I am feeling '
if mood[0] > 0.1 and mood[0] < 0.5:
    st = st + 'content and '
elif mood[0] > 0.5:
    st = st + 'happy and '
elif -0.1 < mood[0] < 0.1:
    st = st + 'neutral and '
elif -0.1 > mood[0] > -0.5:
    st = st + 'sad but '
elif mood[0] < -0.5:
    st = st + 'depressed but '
if 0.1 < mood[1] < 0.5:
    st = st + 'passionate'
elif mood[1] > 0.5:
    st = st + 'very passionate'
elif -0.1 < mood[1] < 0.1:
    st = st + 'indifferent'
elif -0.1 > mood[1] > -0.5:
    st = st + 'calm'
elif mood[1] < -0.5:
    st = st + 'very calm'
think(inspect.getframeinfo(inspect.currentframe()).lineno,st + '({},{})'.format(mood[0], mood[1]))

print('done')
bar.update(16)
def getinput():
    from inout import git
    return git()
def exit_func():
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'Saving and exiting...')
    input('Press RETURN to exit')
    raise SystemExit('Saving and exiting')
commands.commands.append(commands.command(['exit'],exit_func,['Saving and exiting...'],"This will exit the chat with the user","exit"))


mynames = ['omnipotent']
os.system('cls')
talkingto = input('who are you? ')

with open('takephoto.txt','w+') as w:
    w.write(talkingto)
gend = 'unknown'
if not os.path.exists('Info/PERSON/'+talkingto+'.txt'):
    if talkingto in male:
        add_noun(talkingto, 'PERSON', 'is male')
        gend = 'male'
    elif talkingto in female:
        add_noun(talkingto, 'PERSON', 'is female')
        gend = 'female'
    else:
        add_noun(talkingto, 'PERSON')
with open('Info/OPINIONS/'+talkingto+'.txt','r') as r:
    opinion_on_talkingto=float(r.read().split('\n')[0])
    mood[0]+=.5*opinion_on_talkingto
with open('Info/PERSON/'+talkingto+'.txt','r') as r:
    if 'female' in r.read().split('\n')[0]:
        gend='female'
    else:
        gend='male'
        
think(inspect.getframeinfo(inspect.currentframe()).lineno,"{}'s gender is {}".format(talkingto, gend))
conv = []
gpt=True
gpt_chance=0.1


# Set up the model, google generative ai (gemini)
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]



current_conv_gpt=[]
if gpt:
    with open('Info/PERSON/'+talkingto+'.txt','r') as info_file:
        information=[]
        information_on_things=[]
        
        for info in info_file.readlines():
            if '=' not in info:
                information.append(info)
            else:
                information_on_things.append('Their '+info.replace('==',' are ').replace('=',' is '))
    with open('Me.txt','r') as info_file_2:
        information_2=info_file_2.read().replace('\n',', ').replace('am','')        #Load info about ai and talkingto
        
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'Info1:{}'.format(information))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'Info2:{}'.format(information_2))
    
    happiness_out_of_10=int(round((mood[0]+1)*5))
    passion_out_of_10=int(round((mood[1]+1)*5))
    
    commands_gpt="You can perform the following actions by saying their name is chevrons (for example, say <exit> to run the exit command):\n"+"\n".join(["<"+i.name + ">: " + i.description for i in commands.commands])
    
    current_conv_gpt.append("You are an ai called Omnipotent, talking to a human called "+talkingto+". "+talkingto+', '.join(information)+('. ' if information_on_things else '')+', '.join(information_on_things)+", but you should not mention these things unless they come up naturally in conversation. You " + information_2+ ", but you should not mention these things unless they come up naturally in conversation" +"You are feeling "+str(happiness_out_of_10)+"/10 in terms of happiness, "+str(happiness_out_of_10)+"/10 in terms of general outlook and "+str(passion_out_of_10)+"/10 in terms of passion. "+commands_gpt+"\nRespond with a single sentence, in a single line, relatively informally, the only punctuation you can use are commas and chevrons")
    
    think(inspect.getframeinfo(inspect.currentframe()).lineno,"AI Prompt: {}".format(current_conv_gpt[0]))
    model1pro = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    model15pro = genai.GenerativeModel(model_name="gemini-1.5-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    
    model15flash = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    
    def mod_0th_element(st):
        global current_conv_gpt
        current_conv_gpt[0]=st
        think(inspect.getframeinfo(inspect.currentframe()).lineno,"New prompt: "+current_conv_gpt[0])
              
    def Pass(a): pass

    Gemini1Pro=Model("G1p",True,current_conv_gpt.append,mod_0th_element,model1pro.generate_content,2)
    Gemini15Pro=Model("G15p",True,Pass,Pass,model15pro.generate_content,15)
    Gemini15Flash=Model("G15f",True,Pass,Pass,model15flash.generate_content,15)   #Use pass function to make sure 
    Models=[Gemini15Pro,Gemini15Flash,Gemini1Pro]
neutral = ['maybe', 'maybe, maybe not','perhaps']

interrogatives=( "what ",  "why ",  "when ",  "where ",  "is ",  "how ",  "do ",  "does ", 
              "which ",  "are ",  "could ",  "would ", 
              "should ",  "has ",  "have ",  "whom ",  "whose ",  "dont ", "doesnt ","isnt ","can ","cant ","hasnt ","havent ", "shouldnt ", "couldnt ","wouldnt ","did ","didnt ")
def get_clauses_props_qs(sentence):
    
    global interrogatives
    
    conjunctions=('for', 'and', 'nor', 'but', 'or', 'yet', 'so')
    
    '''
    pre_doc=nlp(sentence)
    proper_nouns=[tok for tok in pre_doc if tok.pos_ == 'PROPN']
    print('proper nouns: {}'.format(proper_nouns))
    for proper_noun in proper_nouns:
        sentence=sentence.replace(str(proper_noun),str(proper_noun).capitalize())
        print(str(proper_noun) + str(proper_noun).capitalize())
    print(sentence)
    '''
    
    #We had some problems with proper noun detection (false positives, maybe clean with list of names?), input assumes proper nouns are capitalised
    doc=nlp(sentence)
    split_sent=sentence.split(' ')
    for word_iter in range(len(doc) - 1):
        if doc[word_iter].text=='does' and (doc[word_iter+1].pos_ == 'VERB' or doc[word_iter+1].text=='like'):
            split_sent[word_iter+1]=getInflection(split_sent[word_iter+1], tag='VBZ')                          
            split_sent.pop(word_iter)
            sentence=' '.join(split_sent)
            doc=nlp(sentence)
    sent=sentence
    all_qs=[]
    
    if sent.startswith(interrogatives):
        indicies_of_q_split=[0]
    else: indicies_of_q_split=[]
        
    for index in [m.start() for m in re.finditer(' and ',sent)]:
        if sent[index+5:].startswith(interrogatives):
            indicies_of_q_split.append(index+5)
    question_split = [sent[i:j] for i,j in zip(indicies_of_q_split, indicies_of_q_split[1:]+[None])]     #primary question detection
    all_qs.extend(question_split)
    all_props=[]
    
    clauses=[]
    broken_sent=sent
    '''
clause object:
 |      Parameters
 |      ----------
 |      subject : Span
 |          Subject.
 |      verb : Span
 |          Verb.
 |      indirect_object : Span, optional
 |          Indirect object, The default is None.
 |      direct_object : Span, optional
 |          Direct object. The default is None.
 |      complement : Span, optional
 |          Complement. The default is None.
 |      adverbials : list, optional
 |          List of adverbials. The default is [].
 '''
    lastclauseisq=False

    if doc[-1].pos_ in ('PROPN','PRON') and split_sent[-2]+' ' in interrogatives and split_sent[-3]!='so':
        lastclauseisq=True
        if doc[-1].pos_=='PRON':
            final_pron=doc[-1].text
        else:
            final_pron='*******************'
        if not doc._.clauses:
            last_clause_after_verb=' '.join(split_sent[:-2])
    last_clause=''
    if not doc._.clauses:
        doc._.clauses.append('')
    for clause in doc._.clauses:
        
        if clause:
            clause_words=[]
            
            for category in [clause.subject,clause.verb,clause.direct_object,clause.indirect_object]:
                if category:
                    clause_words.extend(category.text.split(' '))
            if clause.adverbials:
                for adverb in clause.adverbials:
                    clause_words.extend(adverb.text.split(' '))
            if clause.complement:
                for comp in clause.complement:
                    clause_words.extend(comp.text.split(' '))
            min_index=999
            max_index=0  #Furthest word along in clause                                            Check if sentence word before clause is interrogative?
            if broken_sent.split(' ')[0] in conjunctions:
                broken_sent=broken_sent.replace(broken_sent.split(' ')[0]+' ','',1)
            clause_text_l=[]
            broken_sent_2=broken_sent
            for word in clause_words:
                min_index=min([min_index,broken_sent_2.find(word)])                                #Currently trying to extract the clauses this way, works pretty well
                max_index=max([max_index,broken_sent_2.find(word)+len(word)])
            clause_text=broken_sent_2[min_index:max_index]
            broken_sent=broken_sent.replace(clause_text,'',1)
            
            verb=clause.verb.text
        else:
            clause_text=sentence
            clause_doc=nlp(clause_text)
            verb_ls=[]
            for i in range(len(clause_doc)):
                if clause_doc[i].pos_=='VERB':
                    verb_ls.append(clause_doc[i].text)
                    if clause_doc[i+1] !='VERB':
                        break
            verb=' '.join(verb_ls)
            funky_subject=clause_text[:clause_text.find(verb)]
            last_clause_after_verb=clause_text[clause_text.find(verb):]
        clause_is_q=False
        think(inspect.getframeinfo(inspect.currentframe()).lineno,"Clause: "+str(clause_text))
        clauses.append(clause_text)
        if lastclauseisq and clause==doc._.clauses[-1]:
            clause_is_q=True
            lasttwowords=' '.join(split_sent[-2:])
            if clause_text==lasttwowords or (' '.join(broken_sent.split(' ')[-2:])==lasttwowords and not clause):
                break


        
        last_clause_after_verb=clause_text[clause_text.find(verb):]
        for question in all_qs:
            if clause_text in question:
                clause_is_q=True
        try:
            if verb +' ' in interrogatives:
                last_clause_after_verb=' '.join(last_clause_after_verb.split(' ')[1+min(map(lambda s: last_clause_after_verb.split(' ').index(s[:-1]) if s[:-1] in last_clause_after_verb.split(' ') else 100, interrogatives)):])
            else:
                last_clause_after_verb=' '.join(last_clause_after_verb.split(' ')[:min(map(lambda s: last_clause_after_verb.split(' ').index(s[:-1]) if s[:-1] in last_clause_after_verb.split(' ') else 100, interrogatives))])
            #raise ValueError
        except ValueError:
            pass
        if clause_text.startswith(interrogatives) or clause_text in all_qs:
            clause_is_q=True
            all_qs.append(clause_text)
        
        
        
        try:
            
            edited_props=[]
            if clause:
                propositions=clause.to_propositions(as_text=True)
                for prop in propositions:
                    prop_doc=nlp(prop)
                    edited_props.append(prop.replace(prop_doc._.clauses[0].verb.text,clause.verb.text))
            else:
                edited_props.append(clause_text)
            if not clause_is_q: all_props.append(edited_props)
        except Exception as e:
            pass
    
    if lastclauseisq:
        verb_phrase=last_clause_after_verb
        for i in interrogatives: verb_phrase=verb_phrase.replace(i + ' ','')
        if clause and len(doc._.clauses)>1:
            subject_of_q=doc._.clauses[-2].subject.text if doc._.clauses[-1].subject.text == final_pron else doc._.clauses[-1].subject.text
                
        elif len(doc._.clauses)<2:
            subject_of_q=doc._.clauses[-1].subject.text
        else:
            subject_of_q=funky_subject
        q=subject_of_q+' '+verb_phrase
        real_q_lst=[]
        for word in nlp(q):
            done=False
            if (word.pos_ == 'VERB' and not done and not word.text+' ' in interrogatives):
                real_q_lst.append(stemmer.stem(word.text))
                done=True
            elif word.text=='likes'  and not done:
                real_q_lst.append('like')
                done=True
            else:
                real_q_lst.append(word.text)
            
        all_qs.append(split_sent[-2]+' '+' '.join(real_q_lst))
    return clauses, all_props, all_qs

def thisfunction(lst, s):
    if len(lst) > 0:
        for first, *rest in lst:
            s = s.replace(first, '{}', 1)
        for p in product(*lst):
            yield s.format(*p)
    else:
        yield s


def find_response(convo):
    global mood
    if convo[0].startswith('can you '):
        if convo[0].replace('can you ', '') in things_i_can_do:
            saying = random.choice(can_u_p.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(can_u_p.responses))
            return saying
        else:
            saying = random.choice(can_u_n.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(can_u_n.responses))
            return saying
    if convo[0].startswith('cant you '):
        if convo[0].replace('cant you ', '') in things_i_can_do:
            saying = random.choice(cant_u_p.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(cant_u_p.responses))
            return saying
        else:
            saying = random.choice(cant_u_n.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(cant_u_n.responses))
            return saying
    if convo[0].startswith('are you '):
        if convo[0].replace('are you ', '') in things_i_am:
            saying = random.choice(are_u_p.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(are_u_p.responses))
            return saying
        else:
            saying = random.choice(are_u_n.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(are_u_n.responses))
            return saying
    if convo[0].startswith('arent you '):
        if convo[0].replace('arent you ', '') in things_i_am:
            saying = random.choice(arent_u_p.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(arent_u_p.responses))
            return saying
        else:
            saying = random.choice(arent_u_n.responses)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Chose "' + saying + '" from ' + str(arent_u_n.responses))
            return saying
    for i in range(len(convo)):
        
        convo_memory=memory_dict                     #The nested dictionary location of the currrent convo (will be built from the for loop)
        found=True
        for phrase in convo[i:]:
            try:
                convo_memory=dict_address[phrase]
                
            except:
                found=False
                break
        
        if found:
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'memory_dict[' + ']['.join(conv[i:len(convo)]) + '] exists')
            answers=convo_memory.keys()
            if len(answers) > 0:
                think(inspect.getframeinfo(inspect.currentframe()).lineno,
                    'There are {} possible answers: {}'.format(
                        len(answers), answers))
                if len(answers) > 1 and convo[-1] in answers:
                    answers.remove(convo[-1])
                diff = []
                for i in answers:
                    text_i = textblob.TextBlob(i)
                    S_pol = [
                        text_i.sentiment.polarity,
                        text_i.sentiment.subjectivity]
                    diff.append(round(2 - euc_dist.calc(S_pol, mood), 2))
                answers_2 = []
                for i in range(len(diff)):
                    if '!' not in answers[i]:
                        answers_2.append(
                            answers[i] * (2 * int((diff[i] * 100))))
                    else:
                        answers_2.append(answers[i] * (int((diff[i] * 100))))
                saying = random.choice(answers_2).lower()
                mood[0] = (mood[0] * 0.98) + (S_pol[0] * 0.02)
                mood[1] = (mood[1] * 0.98) + (S_pol[1] * 0.02)
                for i in all_resp:
                    saying = saying.replace(i.tag, random.choice(i.responses))
                think(inspect.getframeinfo(inspect.currentframe()).lineno,'chose ' + saying + ' from ' + str(answers))
                return saying

        # Check for all of the sets' patterns
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'checking for recognized patterns...')
        count = 0
        choices = []
        '''
        #I have disabled this until further notice
        for i in all_resp:
            for h in i.beginnings:
                j = h.replace(',', '').strip()
                if convo[-1].strip().startswith(j):
                    think(inspect.getframeinfo(inspect.currentframe()).lineno,'{} starts with {} ({})'.format(convo[-1], j, i))
                    if count < 2:
                        count = count + 1
                        if i.savenoun:
                            for response in i.responses:
                                if inflect.singular_noun(
                                        convo[-1].split(' ')[1]):
                                    choices.append(
                                        response.replace('it', 'they'))
                                else:
                                    choices.append(
                                        response.replace('they', 'it'))
                        else:
                            think(inspect.getframeinfo(inspect.currentframe()).lineno,'{}:{}'.format(i.tag, i.responses))
                            choices.extend(i.responses)
        '''
        if len(choices) > 1:
            saying = random.choice(choices)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'chose ' + saying + ' from ' + str(choices))
            return saying


latestname = None
latestfemale = None
latestmale = None
latestpronoun = None


def makethird(string, male=True):
    string = string.replace('i ', '', 1)
    for i in string.split(' '):
        if lemminflect.getInflection(i, tag='VBZ'):
            if male:
                return string.replace(
                    i,
                    lemminflect.getInflection(
                        i,
                        tag='VBZ')[0]).replace(
                    'my',
                    'his').replace(
                    'mine',
                    'his').replace(
                    ' i ',
                    ' he ').replace(                       
                    'am',
                    'is')
            else:
                return string.replace(
                    i,
                    lemminflect.getInflection(
                        i,
                        tag='VBZ')[0]).replace(
                    'my',
                    'her').replace(
                    'mine',
                    'her').replace(
                    ' i ',
                    ' she ').replace(
                    'am',
                    'is')


replacements = {}
for i in all_resp:
    for j in i.responses:
        replacements.update({j: i.tag})
replacements.update({talkingto: '!speaker!'})
for i in mynames:
    replacements.update({i: '!speakingto!'})
for i in positives:
    replacements.update({i: '!pos!'})
for i in negatives:
    replacements.update({i: '!neg!'})
for i in ['he', 'she']:
    replacements.update({i: '!latestpronoun!'})


def main():
    hour = int(datetime.datetime.now().strftime("%H"))
    time_words = ['morning', 'afternoon', 'evening', 'night']
    if hour < 12:
        current_time_word = 'morning'
    if 11 < hour < 19:
        current_time_word = 'afternoon'
    if 18 < hour or hour < 2:
        current_time_word = 'evening'
    time_words.remove(current_time_word)

    resp = None
    global conv, latestname, latestfemale, latestmale, latestpronoun, latestname, mood
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'getting input...')
    theysaid = str(getinput())
    gpt_spoke=False
    if gpt:
        for cur_model in Models:
            cur_model.Add_to_Conv("input: "+theysaid)
        '''
        client.beta.threads.messages.create(thread_id=thread.id, role="user",content=theysaid)
        '''
    theysaid=theysaid.lower().replace(
            '/',
            '').replace(
            '\\',
            '').replace(
            '?',
            '').replace(
            '!',
            '').replace(
            "'",
            '').replace(
            '"',
            '')
    og_theysaid = theysaid
    
    txtblb = textblob.TextBlob(theysaid)
    mood[0] = (mood[0] * 0.97) + (txtblb.sentiment.polarity * 0.03)
    mood[1] = (mood[1] * 0.97) + (txtblb.sentiment.subjectivity * 0.03)
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'input before preprocessing: {}'.format(theysaid))

    
    if theysaid == 'reset':
        import reset
        input('Press RETURN to exit')
        raise SystemExit('Saving and exiting')
    for command in commands.commands:
        if theysaid in command.inp:
            command.func()
            resp=random.choice(command.responses)
            say(resp)
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Saving and exiting...')
            input('Press RETURN to exit')
            raise SystemExit('Saving and exiting')            #exiting here sucks, should chenge when actions are added
    choices_temp = []                                         #Don't gpt if len(choices_temp) > 0


    if (theysaid == 'what is your name' or theysaid == 'whats your name' or theysaid == 'what is ur name' or theysaid == 'what are you called' or theysaid == 'what are u called'):
        choices_temp.append(
            ['my name is !speaker!', 'i am called !speaker!', 'call me !speaker!','!speaker!','i am !speaker!','!speaker! is my name'])
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'theysaid is {}'.format(theysaid))
    opinionated = {
        'dont love':0,
        'dont like': -0.3,
        'dislike': -0.4,
        'really dont like': -0.5,
        'really dislike': -0.5,
        'hate': -0.75,
        'really hate': -0.85,
        'despise': -0.95,
        'like': 0.3,
        'really like': 0.5,
        'dont dislike': 0,
        'dont mind': 0,
        'really dont mind': 0.2,
        'love': 0.8,
        'really love': 0.9,
        'adore': 0.95}
    opiniated_reversed_pos = {
        0.95: 'adore',
        0.9: 'really love',
        0.8: 'love',
        0.5: 'really like',
        0.3: 'like',
        0.2: 'really dont mind',
        0: 'dont mind'}
    opiniated_reversed_neg = {-0.95: 'despise', -0.85: 'really hate', -0.75: 'hate', -0.5: 'really dislike', -
    0.5: 'really dont like', -0.4: 'dislike', -0.3: 'dont like', 0: 'dont love'}
    
    clauses,propositions,questions=get_clauses_props_qs(' '.join([word.capitalize() if word in names else word for word in theysaid.split(' ')]))
    
    think(inspect.getframeinfo(inspect.currentframe()).lineno,"Clauses: "+str(clauses))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,"Propositions: "+str(propositions))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,"Questions: "+str(questions))
    
    states_or_qs=[]
    statements=[]
    for i in range(len(clauses)):
        if (clauses[i].split(' ')[0]+' ') in interrogatives:
            states_or_qs.append(clauses[i])
        else:
            if len(propositions)+1>i:
                if len(propositions[i])>1:
                    states_or_qs.extend(propositions[i])
                    statements.append(propositions[i])
                else:
                    states_or_qs.append(clauses[i])
                    statements.extend(clauses[i])
            else:
                states_or_qs.append(clauses[i])
                statements.extend(clauses[i])
    think(inspect.getframeinfo(inspect.currentframe()).lineno,"State or Q: " + str(states_or_qs))
    multi_choices=[]
    
    #for state_or_q in list(dict.fromkeys(statements+list(dict.fromkeys(questions[0:theysaid.split(' ').count("and")+1])))):
    for state_or_q in states_or_qs:
        respective_choices=[]
        for i in list(opinionated.keys()):
            if state_or_q.startswith('i ' + i) or state_or_q.startswith('do you ' + i) and not resp:
                
                try:
                    rd = open(
                        'Info/Opinions/' +
                        state_or_q.replace(
                            'i ' +
                            i +
                            ' ',
                            '') +
                        '.txt',
                        'r')
                    opinion = float(rd.read())
                    rd.close()
                    newopinion = opinion + (random.gauss(0.2, 0.03) * min(
                        max([2 * opinion_on_talkingto * opinionated[i] + random.gauss(0, 0.1), -1]), 1))         #weird way to update opinions for some reason
                    with open('Info/Opinions/' + state_or_q.replace('i ' + i + ' ', '').replace('do you ' + i+' ','') + '.txt', 'w+') as opopinion:    #Add opinion of things to both opinion file and me.txt
                        opopinion.write(str(newopinion))             #opopinion=open opinion lol
                    
                except BaseException:
                    with open('Info/Opinions/' + state_or_q.replace('i ' + i + ' ', '').replace('do you ' + i+' ','') + '.txt', 'w+') as opopinion:
                        opinion = min(
                            max([mood[0] + opinionated[i] + random.gauss(0, 0.2), -1]), 1)
                        opopinion.write(str(opinion))
                        
                    if opinion >= 0:
                        for cur in opiniated_reversed_pos:
                            if opinion > cur:
                                with open('Me.txt', 'a') as opme:
                                   opme.write(makethird(opiniated_reversed_pos[cur])+' '+state_or_q.replace('i ' + i + ' ', '').replace('do you ' + i+' ',''))  

                                break
                    else:
                        for cur in opiniated_reversed_neg:
                            if opinion < cur:
                                with open('Me.txt', 'a') as opme:
                                   opme.write(makethird(opiniated_reversed_neg[cur])+' '+state_or_q.replace('i ' + i + ' ', '').replace('do you ' + i+' ',''))

                                break
                    opinion = newopinion
                difference_in_opinions=abs(opinionated[i]-opinion)
                effect_of_difference=0.63-(difference_in_opinions**0.05)
                opinion_on_talkingto+=effect_of_difference*.4   #times 100, divide by person convo counter? or line length of persons file?
                
                with open('Info/OPINIONS/'+talkingto+'.txt','w+') as w:                                                 #ADD PERSON CONVO COUNTER AS A FACTOR AS TO HOW MUCH THIS IS AFFECTED
                    w.write(str(opinion_on_talkingto))   
                
                mood[0]+=effect_of_difference*0.9

                
                if opinion >= 0:
                    for cur in opiniated_reversed_pos:
                        if opinion > cur:
                            
                            howmuchilikeit = opiniated_reversed_pos[cur]
                            if howmuchilikeit == i and random.randint(1, 3) == 3 and state_or_q.startswith('i ' + i):
                                respective_choices.append(random.choice(
                                    ['as do i', 'same', 'same here', 'agreed']))
                            elif howmuchilikeit == i and random.randint(1, 3) == 3 and state_or_q.startswith('do you ' + i):
                                respective_choices.append(random.choice(do_you_p.responses))

                            if inflect.singular_noun(
                                    state_or_q.replace('i ' + i + ' ', '')):
                                respective_choices.append(random.choice(
                                    ['i ' + howmuchilikeit + ' ' + state_or_q.replace(
                                        'i ' + i + ' ', ''),
                                     'i ' + howmuchilikeit + ' them']))
                            else:
                                respective_choices.append(random.choice(
                                    ['i ', 'well i ' + howmuchilikeit + ' ' + state_or_q.replace(
                                        'i ' + i + ' ', ''), 'i ' + howmuchilikeit + ' it']))
                            break
                else:
                    for cur in opiniated_reversed_neg:
                        if opinion < cur:
                            howmuchilikeit = opiniated_reversed_neg[cur]
                            if howmuchilikeit == i and random.randint(1, 3) == 3 and state_or_q.startswith('i ' + i) and not resp:
                                respective_choices.append(random.choice(
                                    ['same', 'same here', 'agreed']))
                            elif howmuchilikeit == i  and state_or_q.startswith('do you ' + i) and not resp:
                                respective_choices.append(random.choice(do_you_p.responses))

                            if inflect.singular_noun(
                                    state_or_q.replace('i ' + i + ' ', '')):
                                respective_choices.append(random.choice(
                                    ['i ' + howmuchilikeit + ' ' + state_or_q.replace(
                                        'i ' + i + ' ', ''),
                                     'i ' + howmuchilikeit + ' them']))
                            else:
                                
                                respective_choices.append(
                                    ['i' + howmuchilikeit + ' ' + state_or_q.replace(
                                        'i ' + i + ' ', ''), 'i' + howmuchilikeit + ' it'])
                            break

                if inflect.singular_noun(state_or_q.replace('i ' + i + ' ', '')):
                    respective_choices.append(random.choice(['i ',
                                          'well i ']) + random.choice(['do not have an opinion on ',
                                                                       'dont have any feeling towards ',
                                                                       'feel indifferent about ']) + random.choice(
                        [state_or_q.replace('i ' + i + ' ',
                                          ''),
                         'them']))
                else:
                    choices_temp.append(random.choice(['i ',
                                          'well i ']) + random.choice(['do not have an opinion on ',
                                                                       'dont have any feeling towards ',
                                                                       'feel indifferent about ']) + random.choice(
                        [state_or_q.replace('i ' + i + ' ',
                                          ''),
                         'it']))

        if state_or_q.startswith('how are you') or state_or_q.startswith('how are u') and not resp:
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Said how are you')
            if mood[0] > 0:
                respective_choices.extend(['good thanks how are you',
                                     'im good',
                                     'good',
                                     'pretty good',
                                     'i am pretty good',
                                     'good thanks'])
            elif mood[0] < 0:
                respective_choices.extend(['alright how are you',
                                     'i am alright',
                                     'i am fine',
                                     'i am fine how are you',
                                     'i am doing alright',
                                     'alright',
                                     'not great',
                                     'not great, how are you',
                                     'not so good'
                                     ])
            else:
                respective_choices.append('lit')
                think(inspect.getframeinfo(inspect.currentframe()).lineno,'Choices temp is now {}'.format(respective_choices))
        if (state_or_q.startswith('you are ') or state_or_q.startswith('are you ')):
            if state_or_q.replace(
                    'you are ',
                    '').replace(
                'are you ',
                '') in things_i_am:
                    respective_choices.append(random.choice(['!pos!, i am', '!pos!', 'i am']))
            else:

                if textblob.TextBlob(
                        state_or_q.replace(
                            'you are ',
                            '').replace(
                            'are you ',
                            '')).sentiment.polarity > -0.1:
                    respective_choices.append(random.choice(['!pos!, i am', '!pos!', 'i am']))
                    add_to_me = open('Me.txt', 'a')
                    add_to_me.write(state_or_q.replace('you are ', 'am'))
                    add_to_me.close()
                else:
                    respective_choices.append(random.choice(['!neg!, i am not', '!neg!', 'i am not','!neg!, i am not {}']).format(state_or_q.replace(
                            'you are ',
                            '').replace(
                            'are you ',
                            '')))
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'checking if {} starts with my'.format(state_or_q))
        if state_or_q.startswith('my '):
            state_or_q_split_is=state_or_q.split('is')
            state_or_q_split_are=state_or_q.split('are')
            if len(state_or_q_split_is[0]) < len(state_or_q_split_are[0]):
                the_thing=state_or_q_split_is[0]
                the_property=state_or_q_split_is[1]
                with open('Info/PERSON/'+talkingto+'.txt','a') as a:
                    a.write('\n'+the_thing+'='+the_property)
            else:
                the_thing=state_or_q_split_are[0]
                the_property=state_or_q_split_are[1]
                with open('Info/PERSON/'+talkingto+'.txt','a') as a:
                    a.write('\n'+the_thing+'=='+the_property)
            
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'checking if {} starts with i'.format(state_or_q))
        if len(state_or_q) > 1 and state_or_q.startswith('i ') and 'VB' in lemminflect.getAllInflections(
                state_or_q.split(' ')[1]) and not state_or_q.split(' ')[1] in ['do', 'can', 'will', 'would', 'could', 'should','am'] and not resp:
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'ok this is interesting')
            add_noun(talkingto, 'PERSON', makethird(state_or_q, gend == 'male'))
            think(inspect.getframeinfo(inspect.currentframe()).lineno,makethird(state_or_q, gend == 'male'))
            if state_or_q.startswith('i can '):
                if state_or_q.replace('i can ', '') in things_i_can_do:
                    respective_choices.append(random.choice(['same', 'as can i', 'so can i', state_or_q + ' too']))
                else:
                    respective_choices.append(random.choice(["yeah, i can't", "really, i can't", "can you, i can't", 'cool']))
            if state_or_q.startswith('i cant ') or state_or_q.startswith("i can't "):
                if state_or_q.replace(
                        'i cant ',
                        '').replace(
                    "i can't ",
                    '') in things_i_can_:
                    respective_choices.append(random.choice(
                        ['i can', 'why not', 'why not i can', 'really, i can']))
                else:
                    respective_choices.append(random.choice(
                    ['same', 'nor can i', "i cant either", "i also cant"]))
            if state_or_q.startswith('i am '):
                with open('Info/PERSON/'+talkingto+'.txt','a') as a:
                    a.write(state_or_q.replace('i am ', ''))
                if state_or_q.replace('i am ', '') in things_i_am:
                    respective_choices.append(random.choice(
                        ['same', 'as am i', 'so am i', state_or_q + ' too']))           
                else:                                                                    
                    
                    respective_choices.append(random.choice(
                    ["yeah i am not", "really i am not", "are you i am not", 'cool']))
            if state_or_q.startswith('i am not'):
                if state_or_q.replace('i am not', '') in things_i_am and not resp:
                    respective_choices.append(random.choice(
                        ['same', 'nor am i', 'i am also not', state_or_q + ' either']))            
                else:                                                                   
                    respective_choices.append(random.choice(
                    ["yeah i am", "really i am", "are you i am", 'cool']))

        multi_choices.append(respective_choices)
                ############END OF STATEMENT SPLIT############

    
    #stateq=list(dict.fromkeys(statements+questions[0:theysaid.split(' ').count("and")+1]))
    stateq=clauses
    theysaid = theysaid.replace(talkingto, '!speaker!')
    for cur_iter in range(len(stateq)):
        respective_choices=[]
        if stateq[cur_iter].startswith('tell me about '):
            try:
                if stateq[cur_iter].replace('tell me about ', '') == '!speaker!':
                    stateq[cur_iter] = stateq[cur_iter].replace('!speaker!', talkingto)
                rd_person_info = open(
                    'Info/PERSON/' +
                    stateq[cur_iter].replace(
                        'tell me about ',
                        '') +
                    '.txt',
                    'r')
                person_info = rd_person_info.read()
                rd_person_info.close()
                temp_pronoun = stateq[cur_iter].replace('tell me about ', '')
                if 'is male' in person_info.split('\n'):
                    temp_pronoun = 'he'
                if 'is female' in person_info.split('\n'):
                    temp_pronoun = 'she'
                choices = person_info.split('\n')
                try:
                    for i in choices:
                        if len(i) < 2:
                            choices.remove(i)
                    choices.remove('/male')
                    choices.remove('/female')
                except BaseException:
                    pass

                if len(choices) > 2:
                    facts = random.sample(choices, 2)                                  #Add a system mesage to gpt to give them info about the person in case the convo continues
                    respective_choices.append(temp_pronoun + ' ' + \
                           facts[0] + ' and ' + temp_pronoun + ' ' + facts[1])
                else:
                    think(inspect.getframeinfo(inspect.currentframe()).lineno, 'No data on person (choices < 1)')
                    raise Exception('No data on person (choices < 1)')
            except Exception as e:
                think(inspect.getframeinfo(inspect.currentframe()).lineno,str(e))
                if stateq[cur_iter].replace('tell me about ', '') in male or stateq[cur_iter].replace('what do you know about ', '') in male:
                    respective_choices.append(random.choice(['i know nothing about',
                                          'i dont know anything about ',
                                          'i dont know ',
                                          'i dont think i know ',
                                          'i dont think i know anything about ',
                                          'i cant tell you about ']) + random.choice(['him',
                                                                                      'them',
                                                                                      stateq[cur_iter].replace('tell me about ',
                                                                                                       '')]))
                if stateq[cur_iter].replace('tell me about ', '') in female:
                    respective_choices.append(random.choice(['i know nothing about',
                                          'i dont know anything about ',
                                          'i dont know ',
                                          'i dont think i know ',
                                          'i dont think i know anything about ',
                                          'i cant tell you about ']) + random.choice(['her',
                                                                                      'them',
                                                                                      stateq[cur_iter].replace('tell me about ',
                                                                                                     '')]))
        multi_choices[cur_iter].extend(respective_choices)
    for i in theysaid.split(' '):
        if i in male:
            latestmale = i
        if i in female:
            latestfemale = i
        if i in names or os.path.isfile('Info/PERSON/' + i + '.txt'):
            latestname = i
    for cur_stateq in stateq:
        try:
            if len(cur_stateq.split(' ')) > 1:
                if wn.synsets(cur_stateq.split(' ')[0])[0].pos() == 'n' and not cur_stateq.split(' ')[0] in male and not \
                cur_stateq.split(' ')[0] in female and not cur_stateq.split(
                        ' ')[0] in names and cur_stateq.split(' ')[1] in ['is', 'are'] and not os.path.isfile(
                    'Info/PERSON/' + cur_stateq.split(' ')[0] + '.txt'):
                    add_noun(
                        stemmer.stem(
                            cur_stateq.split(' ')[0]), 'NOUN', cur_stateq.replace(
                            cur_stateq.split(' ')[0] + ' ', ''))
                    add_noun(
                        stemmer.stem(
                            cur_stateq.replace(
                                cur_stateq.split(' ')[0] + ' ')),
                                '',
                            'DESCRIPTION',
                            stemmer.stem(
                                cur_stateq.split(' ')[0]))
        except BaseException:
            pass
    

    person_in_it = False
    for statement in statements:
        if statement.startswith('!speaker!'):
            add_noun(
                talkingto,
                'PERSON',
                theysaid.replace(
                    '!speaker!',
                    '').strip())
    # Saving theysaid before replacing pronouns so we can add !pronoun! later
    pretheysaid = theysaid
    prestateq=stateq

    
    for i in range(len(theysaid.split(' '))):
        theysaid.replace(current_time_word, '!currenttimeword!')

        if theysaid.split(' ')[i] == 'he':
            theysaid.split(' ')[i] = latestmale
        if theysaid.split(' ')[i] == 'she':                  #This looks funky, i think it works tho
            theysaid.split(' ')[i] = latestfemale
    for state_q_iter in range(len(stateq)):
        stateq[state_q_iter] = stateq[state_q_iter].replace(current_time_word, '!currenttimeword!')

    theysaid = ' ' + theysaid + ' '         #to test for entire words easily



    for state_q_iter in range(len(stateq)):
        for i in mynames:
            stateq[state_q_iter] =  (' '+stateq[state_q_iter]+' ').replace(i, '!speakingto!').strip()
                
            theysaid.replace(i, '!speakingto!')
    for i in theysaid.split(' '):
        if i in male:
            latestpronoun = ' he '

        if i in female:
            latestpronoun = ' she '
    for cur_question in questions:
        if cur_question.startswith('is ') and not resp:
            try:
                read_1 = open('Info/PERSON/' + cur_question.split(' ')[1], 'r')
                temp_text_1 = read_1.read()
                read_1.close()
                if cur_question.replace(
                        'is ' + cur_question.split(' ')[1] + ' ',
                        '') in temp_text_1.split('\n'):
                    resp = random.choice(positives)
                elif cur_question.replace('is ' + cur_question.split(' ')[1] + ' not ', '') in temp_text_1.split('\n'):
                    resp = random.choice(negatives)
                else:
                    resp = random.choice(
                        negatives + positives + neutral + ["i don't know"] * 5)
                    if resp in positives:
                        add_noun(
                            cur_question.split(' ')[1],
                            'PERSON',
                            'is ' +
                            cur_question.replace(
                                'is ' +
                                cur_question.split(' ')[1] +
                                ' ',
                                ''))
                    else:
                        add_noun(
                            cur_question.split(' ')[1],
                            'PERSON',
                            'is not ' +
                            cur_question.replace(
                                'is ' +
                                cur_question.split(' ')[1] +
                                ' ',
                                ''))
            except BaseException:
                pass  # Maybe add 'is' set here
            multi_choices[stateq.index(cur_question)].extend(resp)
    if gpt:    
        with open('Info/PERSON/'+talkingto+'.txt','r') as info_file:
            information=[]
            information_on_things=[]
            
            for info in info_file.readlines():
                if '=' not in info and not info in ('\n','',' '):
                    information.append(info)
                else:
                    information_on_things.append('Their '+info.replace('==',' are ').replace('=',' is '))
        with open('Me.txt','r') as info_file_2:
            information_2=info_file_2.read().replace('\n',', ').replace('am','are')        #Load info about ai and talkingto
            
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'Info1:{}'.format(information))
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'Info2:{}'.format(information_2))
        
        happiness_out_of_10=int(round((mood[0]+1)*5))
        passion_out_of_10=int(round((mood[1]+1)*5))
        
        commands_gpt="You can perform the following actions by saying their name is chevrons (for example, say <exit> to run the exit command):\n"+"\n".join(["<"+i.name + ">: " + i.description for i in commands.commands])
    
        st="You are an ai called Omnipotent, talking to a human called "+talkingto+". "+talkingto+', '.join(information)+('. ' if information_on_things else '')+', '.join(information_on_things)+", but you should not mention these things unless they come up naturally in conversation. You " + information_2+ ", but you should not mention these things unless they come up naturally in conversation" +"You are feeling "+str(happiness_out_of_10)+"/10 in terms of happiness, "+str(happiness_out_of_10)+"/10 in terms of general outlook and "+str(passion_out_of_10)+"/10 in terms of passion. "+commands_gpt+"\nRespond with a single sentence, in a single line, relatively informally, the only punctuation you can use are commas and chevrons"
    
        for cur_model in Models:
            cur_model.Add_to_Prompt(st)
        think(inspect.getframeinfo(inspect.currentframe()).lineno,"AI Prompt: {}".format(current_conv_gpt[0]))        
    if not resp and gpt and random.random()<gpt_chance:
        while not resp:
            for cur_model in Models:
                if not resp:
                    resp=cur_model.Get_Response(current_conv_gpt)
                    
                    if resp: think(inspect.getframeinfo(inspect.currentframe()).lineno,'got "{}" from {}'.format(resp,cur_model.Name))
    for i in [' he ', ' she ']:
        theysaid = theysaid.replace(i, ' !pronoun! ')
        for stateq_iter in range(len(stateq)):
            stateq[stateq_iter]=(' '+stateq[stateq_iter]+' ').replace(i,' !pronoun! ').strip()
    for i in names:
        if i in theysaid:
            theysaid = theysaid.replace(' ' + i + ' ', ' !name! ')
            replacements.update({i: '!name!'})
        for stateq_iter in range(len(stateq)):
            stateq[stateq_iter]=(' '+stateq[stateq_iter]+' ').replace(i,' !name! ').strip()
    for i in all_resp:
        for j in i.responses:
            if j ==theysaid and not j in positives and not j in negatives:
                theysaid = theysaid.replace(j, i.tag)
            for stateq_iter in range(len(stateq)):
                if j ==stateq_iter and not j in positives and not j in negatives:
                    stateq[stateq_iter]=stateq[stateq_iter].replace(j,i.tag)
                    
    for i in positives:
        theysaid = theysaid.replace(' ' + i + ' ', ' !pos! ')
        for stateq_iter in range(len(stateq)):
            stateq[stateq_iter]=(' '+stateq[stateq_iter]+' ').replace(' '+i+' ',' !name! ').strip()
    for i in negatives:
        theysaid = theysaid.replace(' ' + i + ' ', ' !neg! ')
        for stateq_iter in range(len(stateq)):
            stateq[stateq_iter]=(' '+stateq[stateq_iter]+' ').replace(' '+i+' ',' !name! ').strip()
    theysaid = theysaid.strip()

    theysaid_mod_is = None
    contractions = [
        [
            'do not', 'dont'], [
            'will not', 'wont'], [
            'can not', 'cant'], [
            'are not', 'arent'], [
            'is not', 'isnt'], [
            'were not', 'werent'], [
            'i am', 'im'],[
            "could not", "couldnt"],[
            "should not", "shouldnt"],[
            "would not", "wouldnt"],[
            "were not", "werent"],[
            "are not", "shouldnt"]
        
        ]
    for i in contractions:
        theysaid = theysaid.replace(i[1], i[0])   #not using a dict here is a crime against humanity lol
        for stateq_iter in range(len(stateq)):
            stateq[stateq_iter]=(' '+stateq[stateq_iter]+' ').replace(i[0],i[1]).strip()

        
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'input after preprocessing: {}'.format(theysaid))
    og_conv = list(conv)
    og_conv.append(og_theysaid)
    conv.append(theysaid)
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'conv:{}'.format(conv))
    ogconv2 = []
    for i in range(len(og_conv)):
        ogconv2.append(og_conv[i])
        if i != len(og_conv) - 1:
            ogconv2.append('/')
    ogconv3 = []
    for i in ogconv2:
        ogconv3.extend(i.split(' '))
    conv_f2 = []                             #IDK WHAT ANY OF THIS IS BUT LEAVE IT
    for i in range(len(conv)):
        conv_f2.append(og_conv[i])
        if i != len(conv) - 1:
            conv_f2.append('/')
    conv_f3 = []
    dictlist = []
    for key, value in replacements.items():  # Make sure this checks both theysaid and pretheysaid to find the
        # correct dictionary value that contains both sides of it
        for _ in range(theysaid.count(value)):
            if theysaid.count(key) == theysaid.count(value):
                dictlist.append([value, key])              #Dictlist is a list of all replacements to be made
    for i in conv_f2:
        conv_f3.extend(i.split(' '))
    
    for conv_version in thisfunction(dictlist, '/'.join(conv)):
        choices_temp.append(find_response(conv))
    for iteration in range(len(stateq)):
        if not multi_choices[iteration]:
            think(inspect.getframeinfo(inspect.currentframe()).lineno,str(conv + [stateq]))
            multi_choices[iteration].append(find_response(conv + stateq))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'dictlist is {}'.format(dictlist))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'thisfunction returned {}'.format(str(list(thisfunction(dictlist, '/'.join(conv))))))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'choices temp is now {}'.format(choices_temp))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'multi choices is now {}'.format(multi_choices))
    
    if not [None] in multi_choices:
        the_chosen_choices=[]
        for m_choice in multi_choices:
            the_chosen_choices.append(random.choice(m_choice))
        choices_temp.append(', '.join(the_chosen_choices))
    while 1:
        if None in choices_temp:
            choices_temp.remove(None)
        else:
            break
    if choices_temp and not resp:
        resp = random.choice(choices_temp)
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'selecting {} from {}'.format(resp, choices_temp))
                               
    

    if resp == None:
        people=[]
        with open('inframe.txt','r') as r:
            inframe_string=r.read()                             #Getting the video data and figuring out who is in the frame
            if len(inframe_string)>0:
                people=inframe_string.split('\n').remove('').remove(talkingto)
        if people:
            if people[0]!='Unknown':
                conv = []
                og_conv = []
                resp=random.choice(['hello {}','greetings {}','hi {}','how are you {}','hey {}','yo {}'])
                resp.format(people[0])
            else:
                conv = []
                og_conv = []
                resp=random.choice(['who is with you','who is that','who is this','who can i see'])
            
    if resp==None:
        for i in range(len(conv)):
        
        
            conv_memory=memory_dict                     #The nested dictionary location of the currrent convo (will be built from the for loop)
            found=True
            shortened_conv=conv[i:len(conv)]
            phrases=[]                                  #the conversation going forward
            for phrase in shortened_conv[i:]:
                phrases.append(phrase)
                if not phrase in conv_memory.keys():         #Adding all versions of conv to dict
                     memory_dict[phrase]={}       #How tf do we update the memory dictionary
                     exec_string='memory_dict'
                     for memory_phrase in phrases:
                         exec_string=exec_string+'["'+memory_phrase+'"]'     #THIS IS SO CURSED, BUT ITS THE ONLY WAY I CAN THINK TO
                     exec_string=exec_string+'={}'                         #Navigate an unknown-dimensional nested dictionary
                     think(inspect.getframeinfo(inspect.currentframe()).lineno,'exec_string is {}     MAY GOD HAVE MERCY ON OUR SOULS FOR WRITING LINE {}'.format(exec_string,inspect.getframeinfo(inspect.currentframe()).lineno - 2))
                     exec(exec_string)
                     conv_memory[phrase]={}

        conv = []
        og_conv = []

        think(inspect.getframeinfo(inspect.currentframe()).lineno,'1: ' + str(os.listdir()))
        os.chdir(path)
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'2: ' + str(os.listdir()))

    if gpt:
        while not resp:
            for cur_model in Models:
                if not resp:
                    resp=cur_model.Get_Response(current_conv_gpt)
                    
                    if resp:
                        print(resp.encode(encoding = 'UTF-8', errors = 'strict'))
                        think(inspect.getframeinfo(inspect.currentframe()).lineno,'got "{}" from {}'.format(resp.encode(encoding = 'UTF-8', errors = 'strict'),cur_model.Name))
    for command in commands.commands:
        if "<"+command.name+">" in resp:
            command.func()                 
                        
#---------------------------------------------------------Anything below here will not be run if gpt=True -----------------------------------------------------------------------------------
    if resp == None:
        if theysaid.startswith('why ') and len(theysaid.split(' ')) > 2:
            resp = random.choice(
                ["im not sure", "i dont know", "just because", "how should i know"])
        if theysaid.startswith('what ') or theysaid.startswith(
                'who ') or theysaid.startswith('where ') or theysaid.startswith('how '):
            resp = random.choice(["im not sure",
                                  "i dont know",
                                  "i dont know, " + theysaid,
                                  'how should i know'])
    if not resp:
        for phrase in memory_dict:
            if memory_dict[phrase] == {}:
                resp = phrase
                think(inspect.getframeinfo(inspect.currentframe()).lineno,'cleared and spoke')
                break
 
    if resp == None:
        resp = theysaid    #lol i don't think this is possible
    conv.append(resp)

    real_resp = ' ' + resp + ' '
    if latestname != None:
        real_resp = real_resp.replace('!name!', latestname)
    else:
        for i in real_resp.split(' '):
            if i == '!name!':
                latestname = random.choice(names)
    for i in real_resp.split(' '):
        for n in names:
            if i == n and n in male:
                latestpronoun = ' he '
            if i == n and n in female:
                latestpronoun = ' she '
        if i == '!pronoun!':
            real_resp = real_resp.replace(' !pronoun! ', latestpronoun)
        
    real_resp = real_resp.replace('!pos!', random.choice(positives))
    real_resp = real_resp.replace('!neg!', random.choice(negatives))
    real_resp = real_resp.replace('!speakingto!', talkingto)
    real_resp = real_resp.replace('!speaker!', random.choice(mynames))
    real_resp = real_resp.replace('!currenttimeword!', current_time_word)
    real_resp = real_resp.replace('!currenttime!', random.choice(time_words))
    for i in all_resp:
        real_resp = real_resp.replace(i.tag, random.choice(i.responses))      #Possible problem
    real_resp = real_resp.strip()
    for i in names:
        if i in resp:
            resp = resp.replace(' ' + i + ' ', ' !name! ')
            replacements.update({i: '!name!'})

    for key, value in replacements.items():
        resp=resp.replace(key, value)
        if key in resp: think(inspect.getframeinfo(inspect.currentframe()).lineno,'replacing {} with {} in ai response'.format(key,value))
    
    og_conv.append(real_resp)
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'og_conv: {}'.format(og_conv))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'saying {}'.format(real_resp))
    say(real_resp)
    if gpt:
        for cur_model in Models:
            cur_model.Add_to_Conv("output: "+real_resp)
    conv2 = list(conv)
    splitconv = [i.split(' ') for i in conv2]
    for j in splitconv:
        j.append('/')
    conv2 = [item for sublist in splitconv for item in sublist]

    og_conv2 = list(og_conv)

    og_splitconv = [i.split(' ') for i in og_conv2]
    for j in og_splitconv:
        j.append('/')
    og_conv2 = [item for sublist in og_splitconv for item in sublist]

    think(inspect.getframeinfo(inspect.currentframe()).lineno,'ogconv2: {}      conv2: {}'.format(og_conv2, conv2))
    dictlist = []
    for key, value in replacements.items():  # Make sure this checks both theysaid and pretheysaid to find the correct dictionary value that contains both sides of it
        for _ in range(''.join(conv2).count(value)):
            if ''.join(conv2).count(key) == ''.join(conv2).count(value):
                dictlist.append([value, key])
    for i in dictlist:
        for j in range(len(conv)):
            if i[1] in conv[j]:
                conv[j].replace(i[1], i[0])
    
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'thisfunc ' + str(list(thisfunction(dictlist, '/'.join(og_conv)))))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'dictlist={}'.format(dictlist))

    for current_conv in list(thisfunction(dictlist, '/'.join(og_conv))):
        curr_split_conv = current_conv.split('/')
        for i in range(len(curr_split_conv)):
 
            conv_memory=memory_dict                     #The nested dictionary location of the currrent convo (will be built from the for loop)
            found=True
            shortened_conv=conv[i:len(curr_split_conv)]
            phrases=[]                                  #the conversation going forward
            for phrase in shortened_conv[i:]:
                phrases.append(phrase)
                if not phrase in conv_memory.keys():         #Adding all versions of conv to dict
                     memory_dict[phrase]={}                  #How tf do we update the memory dictionary
                     exec_string='memory_dict'
                     for memory_phrase in phrases:
                         exec_string=exec_string+'["'+memory_phrase+'"]'     #THIS IS SO CURSED, BUT ITS THE ONLY WAY I CAN THINK TO
                     exec_string=exec_string+'={}'                         #Navigate an unknown-dimensional nested dictionary
                     think(inspect.getframeinfo(inspect.currentframe()).lineno,'exec_string is {}     MAY GOD HAVE MERCY ON OUR SOULS FOR WRITING LINE {}'.format(exec_string,inspect.getframeinfo(inspect.currentframe()).lineno))
                     exec(exec_string)
                     conv_memory[phrase]={}


    with open('memory_file.py','w+') as op:
        op.write('memory_dict='+str(memory_dict))
                     
    txtblb = textblob.TextBlob(real_resp)
    mood[0] = (mood[0] * 0.98) + (txtblb.sentiment.polarity * 0.02)
    mood[1] = (mood[1] * 0.98) + (txtblb.sentiment.subjectivity * 0.02)


try:
    os.system('cls')
    while 1:
        main()
except Exception as e:
    if e == 'Saving and exiting':
        print(e)
    else:
        print('\nAn unexpected error occured...:\n\n' + traceback.format_exc())
        think(inspect.getframeinfo(inspect.currentframe()).lineno,traceback.format_exc())

'''
   © Copyright 2024 James Pinder

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
