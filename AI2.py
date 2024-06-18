"""
Script: Omnipotent Lillypad AI2
Version: 1.4.3
Name: James Pinder (https://github.com/3NiGMa404)
Date: 2024-01-10
"""
from sets import *
import spacy
import pyaudio
import traceback
import textblob
import shutil
import datetime
import random
import colorama
import progressbar
import pyinflect
import inflect
import nltk
from itertools import product
from nltk.corpus import wordnet as wn
import commands                 #PLEASE MAKE SURE ALL RESP=... LINES AFTER RANDOM GPT ARE ENCLOSED WITHIN A IF NOT RESP
import os
import inspect
import psutil
import euc_dist
import warnings
from memory_file import memory_dict
from openai import OpenAI

warnings.filterwarnings("ignore")
print(__doc__)
os.system('cls')   #On windows only
os.system('python3 face_recognizer.py')
inflect = inflect.engine()
path = os.path.realpath(__file__).replace(
    os.path.basename(__file__), '').replace(
    '\\', '/')
process = psutil.Process(os.getpid())
colorama.init()
bar = progressbar.ProgressBar(maxval=13)
bar.start()
os.system('cls')
bar.update(1)
print('\nloading datetime...', end='')
print('done')
os.system('cls')
bar.update(2)
print('\nloading shutil...', end='')
print('done')
os.system('cls')
bar.update(3)
print('\nloading textblob...', end='')
print('done')
os.system('cls')
bar.update(4)
print('\nloading traceback...', end='')
print('done')
os.system('cls')
bar.update(5)
print('\nloading pyaudio...', end='')
print('done')
os.system('cls')
bar.update(6)
print('done')
os.system('cls')
bar.update(7)
print('\nloading spacy...', end='')
print('done')
os.system('cls')
print('\nloading sets...')
print('done')
os.system('cls')
bar.update(8)
print('\nloading database...')
nlp = spacy.load("en_core_web_sm")
maleraw = open('male.txt', 'r').read().split('\n')
male = []
for i in maleraw:
    male.append(i.lower().strip())
print('done')
bar.update(9)
os.system('cls')
print('\nloading another database...')
femaleraw = open('female.txt', 'r').read().split('\n')
female = []
for j in femaleraw:
    female.append(j.lower().strip())
names = male + female
print('done')
bar.update(10)
os.system('cls')
print('\nloading memory...')

if not os.path.isfile('thoughts.txt'):
    x = open('thoughts.txt', 'w+')
    x.close()
if not os.path.exists('Info'):
    os.makedirs('Info')
print('done')
bar.update(11)
os.system('cls')
print('\nloading speech...')

def think(line, string, statedatetime=True):
    c = open('thoughts.txt', 'a+')
    if statedatetime:
        c.write('\n' + str(datetime.datetime.now()) + '({}): '.format(line) + string)
    else:
        c.write('\n' + string)
    c.close()


think(inspect.getframeinfo(inspect.currentframe()).lineno,'\nNEW SESSION\n\n', statedatetime=False)


def say(text):
    from inout import ret
    ret(text)


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
bar.update(12)
os.system('cls')


print('\nloading speech...')
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


bar.update(13)
def getinput():
    from inout import git
    return git()



mynames = ['omnipotent']
os.system('cls')
talkingto = input('who are you? ')

with open('takephoto.txt','w+') as w:
    w.write(talkingto)
gend = 'unknown'
if not os.path.exists('info/PERSON/'+talkingto+'.txt'):
    if talkingto in male:
        add_noun(talkingto, 'PERSON', 'is male')
        add_noun(talkingto, 'PERSON', '/male')
        gend = 'male'
    elif talkingto in female:
        add_noun(talkingto, 'PERSON', 'is female')
        add_noun(talkingto, 'PERSON', '/female')
        gend = 'female'
    else:
        add_noun(talkingto, 'PERSON')
with open('Info/OPINIONS/'+talkingto+'.txt','r') as r:
    opinion_on_talkingto=float(r.read().split('\n')[0])
    mood[0]+=.5*opinion_on_talkingto                    #???
think(inspect.getframeinfo(inspect.currentframe()).lineno,"{}'s gender is {}".format(talkingto, gend))
conv = []
gpt=False
gpt_chance=0.1

if gpt:
    with open(talkingto+'.txt','r') as info_file:
        information=[]
        information_on_things=[]
        
        for info in info_file.read().replace('\n',', '):
            if '=' not in info:
                information.append(info)
            else:
                information_on_things.append('Their '+info.replace('==',' are ').replace('=',' is '))
    with open('Me.txt','r') as info_file_2:
        information_2=info_file_2.read().replace('\n',', ').replace('am','')        #Load info about ai and talkingto
    client = OpenAI()
    happiness_out_of_10=int(round((mood[0]+1)*5))
    passion_out_of_10=int(round((mood[1]+1)*5))
    assistant = client.beta.assistants.retrieve("OmnipotentGPT4")
    thread=client.beta.threads.create()
    client.beta.threads.messages.create(
    thread_id=thread.id,
    role="system",
    content="You are an ai called omnipotent, talking to a human called "+talkingto+". "+talkingto+information+'. '+information_on_things+". You " + information_2+ "You are feeling "+str(happiness_out_of_10)+"/10 in terms of happiness, "+str(happiness_out_of_10)+"/10 in terms of general outlook and "+str(passion_out_of_10)+"/10 in terms of emotionalness. Respond with a single sentence, not too formal, encapsulated with quotations"
    )
    
neutral = ['maybe', 'maybe, maybe not','perhaps']


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
        if pyinflect.getInflection(i, tag='VBZ'):
            if male:
                return string.replace(
                    i,
                    pyinflect.getInflection(
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
                    pyinflect.getInflection(
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
        client.beta.threads.messages.create(thread_id=thread.id, role="user",content=theysaid)

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

    theysaid = theysaid.replace(talkingto, '!speaker!')
    if theysaid == 'exit':
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'Saving and exiting...')
        input('Press RETURN to exit')
        raise SystemExit('Saving and exiting')
    if theysaid == 'reset':
        import reset
        input('Press RETURN to exit')
        raise SystemExit('Saving and exiting')
    for command in commands.commands:
        if theysaid in command.inp:
            command.func()
            say(random.choice(command.responses))
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Saving and exiting...')
            input('Press RETURN to exit')
            raise SystemExit('Saving and exiting')
    choices_temp = []
    if random.random()<gpt_chance and gpt:
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)
        while client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id) != 'completed':
            pass
        multi_resps_from_gpt=''
        for message in client.beta.threads.messages.list(thread_id=thread.id):
            if message.role != 'assistant':
                multi_resps_from_gpt=''
            else:
                multi_resps_from_gpt=multi_resps_from_gpt + '. '+ message[1:-1]
                
        resp=multi_resps_from_gpt

    if not resp and (theysaid == 'what is your name' or theysaid == 'whats your name' or theysaid == 'what is ur name' or theysaid == 'what are you called' or theysaid == 'what are u called'):
        choices_temp.append(
            ['my name is !speaker!', 'i am called !speaker!', 'call me !speaker!'])
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
    for i in list(opinionated.keys()):
        if theysaid.startswith('i ' + i) or theysaid.startswith('do you ' + i) and not resp:
            
            try:
                rd = open(
                    'Info/Opinions/' +
                    theysaid.replace(
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
                with open('Info/Opinions/' + theysaid.replace('i ' + i + ' ', '').replace('do you ' + i+' ','') + '.txt', 'w+') as opopinion:    #Add opinion of things to both opinion file and me.txt
                    opopinion.write(str(newopinion))             #opopinion=open opinion lol
                
            except BaseException:
                with open('Info/Opinions/' + theysaid.replace('i ' + i + ' ', '').replace('do you ' + i+' ','') + '.txt', 'w+') as opopinion:
                    opinion = min(
                        max([mood[0] + opinionated[i] + random.gauss(0, 0.2), -1]), 1)
                    opopinion.write(str(opinion))
                    
                if opinion >= 0:
                    for cur in opiniated_reversed_pos:
                        if opinion > cur:
                            with open('Me.txt', 'a') as opme:
                               opme.write(makethird(opiniated_reversed_pos[cur])+' '+theysaid.replace('i ' + i + ' ', '').replace('do you ' + i+' ',''))  

                            break
                else:
                    for cur in opiniated_reversed_neg:
                        if opinion < cur:
                            with open('Me.txt', 'a') as opme:
                               opme.write(makethird(opiniated_reversed_neg[cur])+' '+theysaid.replace('i ' + i + ' ', '').replace('do you ' + i+' ',''))

                            break
                opinion = newopinion
            difference_in_opinions=abs(opinionated[i]-opinion)
            effect_of_difference=0.63-(difference_in_opinions**0.05)
            opinion_on_talkingto+=effect_of_difference*.4   #times 100, divide by person convo counter? or line length of persons file?
            
            with open('Info/OPINIONS/'+talkingto+'.txt','w+') as w:                                                 #ADD PERSON CONVO COUNTER AS A FACTOR AS TO HOW MUCH THIS IS AFFECTED
                w.write(str(opinion_on_talkingto))   
            
            mood[0]+=effect_of_difference*0.9

            
            if opinion >= 0 and not resp:
                for cur in opiniated_reversed_pos:
                    if opinion > cur:
                        
                        howmuchilikeit = opiniated_reversed_pos[cur]
                        if howmuchilikeit == i and random.randint(1, 3) == 3 and theysaid.startswith('i ' + i):
                            resp = random.choice(
                                ['as do i', 'same', 'same here', 'agreed'])
                        elif howmuchilikeit == i and random.randint(1, 3) == 3 and theysaid.startswith('do you ' + i):
                            resp=random.choice(do_you_p.responses)
                        if not resp:
                            if inflect.singular_noun(
                                    theysaid.replace('i ' + i + ' ', '')):
                                resp = random.choice(
                                    ['i ' + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''),
                                     'i ' + howmuchilikeit + ' them'])
                            else:
                                resp = random.choice(
                                    ['i ', 'well i ' + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''), 'i ' + howmuchilikeit + ' it'])
                        break
            else:
                for cur in opiniated_reversed_neg:
                    if opinion < cur:
                        howmuchilikeit = opiniated_reversed_neg[cur]
                        if howmuchilikeit == i and random.randint(1, 3) == 3 and theysaid.startswith('i ' + i) and not resp:
                            resp = random.choice(
                                ['same', 'same here', 'agreed'])
                        elif howmuchilikeit == i and random.randint(1, 2) == 2 and theysaid.startswith('do you ' + i) and not resp:
                            resp=random.choice(do_you_p.responses)
                        if not resp:
                            if inflect.singular_noun(
                                    theysaid.replace('i ' + i + ' ', '')):
                                resp = random.choice(
                                    ['i ' + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''),
                                     'i ' + howmuchilikeit + ' them'])
                            else:
                                
                                resp = random.choice(
                                    ['i' + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''), 'i' + howmuchilikeit + ' it'])
                        break
            if not resp:
                if inflect.singular_noun(theysaid.replace('i ' + i + ' ', '')):
                    resp = random.choice(['i ',
                                          'well i ']) + random.choice(['do not have an opinion on ',
                                                                       'dont have any feeling towards ',
                                                                       'feel indifferent about ']) + random.choice(
                        [theysaid.replace('i ' + i + ' ',
                                          ''),
                         'them'])
                else:
                    resp = random.choice(['i ',
                                          'well i ']) + random.choice(['do not have an opinion on ',
                                                                       'dont have any feeling towards ',
                                                                       'feel indifferent about ']) + random.choice(
                        [theysaid.replace('i ' + i + ' ',
                                          ''),
                         'it'])

    if theysaid.startswith('how are you') or theysaid.startswith('how are u') and not resp:
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'Said how are you')
        if mood[0] > 0:
            choices_temp.extend(['good thanks how are you',
                                 'im good',
                                 'good',
                                 'pretty good',
                                 'im pretty good',
                                 'good thanks'])
        elif mood[0] < 0:
            choices_temp.extend(['alright how are you',
                                 'im alright',
                                 'im fine',
                                 'im fine how are you',
                                 'im doing alright',
                                 'alright'])
        else:
            choices_temp.append('lit')
            think(inspect.getframeinfo(inspect.currentframe()).lineno,'Choices temp is now {}'.format(choices_temp))
    if (theysaid.startswith('you are ') or theysaid.startswith('are you ')) and not resp:
        if theysaid.replace(
                'you are ',
                '').replace(
            'are you ',
            '') in things_i_am:
                resp = random.choice(['!pos!, i am', '!pos!', 'i am'])
        else:

            if textblob.TextBlob(
                    theysaid.replace(
                        'you are ',
                        '').replace(
                        'are you ',
                        '')).sentiment.polarity > -0.1:
                resp = random.choice(['!pos!, i am', '!pos!', 'i am'])
                add_to_me = open('Me.txt', 'a')
                add_to_me.write(theysaid.replace('you are ', 'am'))
                add_to_me.close()
            else:
                if not resp:
                    resp = random.choice(['!neg!, i am', '!neg!', 'i am not'])
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'checking if {} starts with my'.format(theysaid))
    if theysaid.startswith('my '):
        theysaid_split_is=theysaid.split('is')
        theysaid_split_are=theysaid.split('are')
        if len(theysaid_split_is[0]) < len(theysaid_split_are[0]):
            the_thing=theysaid_split_is[0]
            the_property=theysaid_split_is[1]
            with open('Info/PERSON/'+talkingto+'.txt','a') as a:
                a.write('\n'+the_thing+'='+the_property)
        else:
            the_thing=theysaid_split_are[0]
            the_property=theysaid_split_are[1]
            with open('Info/PERSON/'+talkingto+'.txt','a') as a:
                a.write('\n'+the_thing+'=='+the_property)
        
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'checking if {} starts with i'.format(theysaid))
    if len(theysaid) > 1 and theysaid.startswith('i ') and 'VB' in pyinflect.getAllInflections(
            theysaid.split(' ')[1]) and not theysaid.split(' ')[1] in ['do', 'can', 'will', 'would', 'could', 'should','am'] and not resp:
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'ok this is interesting')
        add_noun(talkingto, 'PERSON', makethird(theysaid, gend == 'male'))
        think(inspect.getframeinfo(inspect.currentframe()).lineno,makethird(theysaid, gend == 'male'))
        if theysaid.startswith('i can '):
            if theysaid.replace('i can ', '') in things_i_can_do:
                resp = random.choice(
                    ['same', 'as can i', 'so can i', theysaid + ' too'])
            else:
                resp = random.choice(
                    ["yeah, i can't", "really, i can't", "can you, i can't", 'cool'])
        if theysaid.startswith('i cant ') or theysaid.startswith("i can't "):
            if theysaid.replace(
                    'i cant ',
                    '').replace(
                "i can't ",
                '') in things_i_can_do and not resp:
                resp = random.choice(
                    ['i can', 'why not', 'why not i can', 'really, i can'])
            else:
                if not resp:
                    resp = random.choice(
                    ['same', 'nor can i', "i cant either", "i also cant"])
        if theysaid.startswith('i am '):
            with open('Info/PERSON/'+talkingto+'.txt','a') as a:
                a.write(theysaid.replace('i am ', ''))
            if theysaid.replace('i am ', '') in things_i_am and not resp:
                resp = random.choice(
                    ['same', 'as am i', 'so am i', theysaid + ' too'])            #YOU WERE HALFWAY THROUGH THIS LAST TIME
            else:                                                                    #Checking if the ai is things that people are
                if not resp:
                    resp = random.choice(
                    ["yeah i am not", "really i am not", "are you i am not", 'cool'])
        if theysaid.startswith('i am not'):
            if theysaid.replace('i am not', '') in things_i_am and not resp:
                resp = random.choice(
                    ['same', 'nor am i', 'i am also not', theysaid + ' either'])            #YOU WERE HALFWAY THROUGH THIS LAST TIME
            else:                                                                    #Checking if the ai is things that people are
                if not resp:
                    resp = random.choice(
                    ["yeah i am", "really i am", "are you i am", 'cool'])
    if theysaid.startswith('tell me about ') and not resp:
        try:
            if theysaid.replace('tell me about ', '') == '!speaker!':
                theysaid = theysaid.replace('!speaker!', talkingto)
            rd_person_info = open(
                'Info/PERSON/' +
                theysaid.replace(
                    'tell me about ',
                    '') +
                '.txt',
                'r')
            person_info = rd_person_info.read()
            rd_person_info.close()
            temp_pronoun = theysaid.replace('tell me about ', '')
            if 'male' in person_info.split(
                    '\n') or 'is male' in person_info.split('\n'):
                temp_pronoun = 'he'
            if 'female' in person_info.split(
                    '\n') or 'is female' in person_info.split('\n'):
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
                facts = random.sample(choices, 2)
                resp = temp_pronoun + ' ' + \
                       facts[0] + ' and ' + temp_pronoun + ' ' + facts[1]
            else:
                raise Exception('No data (choices < 1)')
        except Exception as e:
            think(inspect.getframeinfo(inspect.currentframe()).lineno,str(e))
            if theysaid.replace('tell me about ', '') in male or theysaid.replace('what do you know about ', '') in male:
                resp = random.choice(['i know nothing about',
                                      'i dont know anything about ',
                                      'i dont know ',
                                      'i dont think i know ',
                                      'i dont think i know anything about ',
                                      'i cant tell you about ']) + random.choice(['him',
                                                                                  'them',
                                                                                  theysaid.replace('tell me about ',
                                                                                                   '')])
            if theysaid.replace('tell me about ', '') in female:
                resp = random.choice(['i know nothing about',
                                      'i dont know anything about ',
                                      'i dont know ',
                                      'i dont think i know ',
                                      'i dont think i know anything about ',
                                      'i cant tell you about ']) + random.choice(['her',
                                                                                  'them',
                                                                                  theysaid.replace('tell me about ',
                                                                                                   '')])
            theysaid.replace(talkingto, '!speaker!')
    for i in theysaid.split(' '):
        if i in male:
            latestmale = i
        if i in female:
            latestfemale = i
        if i in names or os.path.isfile('Info/PERSON/' + i + '.txt'):
            latestname = i
    try:
        if len(theysaid.split(' ')) > 1:
            if wn.synsets(theysaid.split(' ')[0])[0].pos() == 'n' and not theysaid.split(' ')[0] in male and not \
            theysaid.split(' ')[0] in female and not theysaid.split(
                    ' ')[0] in names and theysaid.split(' ')[1] in ['is', 'are'] and not os.path.isfile(
                'Info/PERSON/' + theysaid.split(' ')[0] + '.txt'):
                add_noun(
                    nltk.PorterStemmer(
                        theysaid.split(' ')[0]).stem(), 'NOUN', theysaid.replace(
                        theysaid.split(' ')[0] + ' ', ''))
                add_noun(
                    nltk.PorterStemmer(
                        theysaid.replace(
                            theysaid.split(' ')[0] + ' ',
                            ''),
                        'DESCRIPTION',
                        nltk.PorterStemmer(
                            theysaid.split(' ')[0]).stem()))
    except BaseException:
        pass

    for i in mynames:
        theysaid = theysaid.replace(i, '!speakingto!')

    person_in_it = False
    if theysaid.startswith('!speaker!'):
        add_noun(
            talkingto,
            'PERSON',
            theysaid.replace(
                '!speaker!',
                '').strip())
    # Saving theysaid before replacing pronouns so we can add !pronoun! later
    pretheysaid = theysaid
    for i in range(len(theysaid.split(' '))):
        if i == current_time_word:
            theysaid = theysaid.replace(
                theysaid.split(' ')[i], '!currenttimeword!')
        if i in time_words:
            theysaid = theysaid.replace(theysaid.split(' ')[i], '!timeword!')
        if theysaid.split(' ')[i] == 'he':
            theysaid.split(' ')[i] = latestmale
        if theysaid.split(' ')[i] == 'she':
            theysaid.split(' ')[i] = latestfemale

    theysaid = ' ' + pretheysaid + ' '
    for n in names:
        for i in theysaid.split(' '):
            if i == n and n in male:
                latestpronoun = ' he '

            if i == n and n in female:
                latestpronoun = ' she '

    if theysaid.startswith('is ') and not resp:
        try:
            read_1 = open('Info/PERSON/' + theysaid.split(' ')[1], 'r')
            temp_text_1 = read_1.read()
            read_1.close()
            if theysaid.replace(
                    'is ' + theysaid.split(' ')[1] + ' ',
                    '') in temp_text_1.split('\n'):
                resp = random.choice(positives)
            elif theysaid.replace('is ' + theysaid.split(' ')[1] + ' not ', '') in temp_text_1.split('\n'):
                resp = random.choice(negatives)
            else:
                resp = random.choice(
                    negatives + positives + neutral + ["i don't know"] * 5)
                if resp in positives:
                    add_noun(
                        theysaid.split(' ')[1],
                        'PERSON',
                        'is ' +
                        theysaid.replace(
                            'is ' +
                            theysaid.split(' ')[1] +
                            ' ',
                            ''))
                else:
                    add_noun(
                        theysaid.split(' ')[1],
                        'PERSON',
                        'is not ' +
                        theysaid.replace(
                            'is ' +
                            theysaid.split(' ')[1] +
                            ' ',
                            ''))
        except BaseException:
            pass  # Maybe add 'is' set here

    for i in [' he ', ' she ']:
        theysaid = theysaid.replace(i, ' !pronoun! ')
    for i in names:
        if i in theysaid:
            theysaid = theysaid.replace(' ' + i + ' ', ' !name! ')
            replacements.update({i: '!name!'})
    for i in all_resp:
        for j in i.responses:
            if j ==theysaid and not j in positives and not j in negatives:
                theysaid = theysaid.replace(j, i.tag)
    for i in positives:
        theysaid = theysaid.replace(' ' + i + ' ', ' !pos! ')

    for i in negatives:
        theysaid = theysaid.replace(' ' + i + ' ', ' !neg! ')
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
            'i am', 'im'], [
            "i'm", "im"]]
    for i in contractions:
        theysaid = theysaid.replace(i[1], i[0])
    # conjunctions_a=[' is ',' are ',' isnt ',' arent ',' were ',' werent ',' can ',' cant ', ' do ', ' dont ',
    # ' will ',' wont ']
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
    conv_f2 = []
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
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'dictlist is {}'.format(dictlist))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'thisfunction returned {}'.format(str(list(thisfunction(dictlist, '/'.join(conv))))))
    idk = False
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'choices temp is now {}'.format(choices_temp))
    for i in range(2):
        if None in choices_temp:
            choices_temp.remove(None)
    if choices_temp:
        resp = random.choice(choices_temp) ###
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'selecting {} from {}'.format(resp, choices_temp))
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
        idk = True
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
                     think(inspect.getframeinfo(inspect.currentframe()).lineno,'exec_string is {}     MAY GOD HAVE MERCY ON OUR SOULS FOR WRITING LINE {}'.format(exec_string,inspect.getframeinfo(inspect.currentframe()).lineno))
                     exec(exec_string)
                     conv_memory[phrase]={}

        conv = []
        og_conv = []

        think(inspect.getframeinfo(inspect.currentframe()).lineno,'1: ' + str(os.listdir()))
        os.chdir(path)
        think(inspect.getframeinfo(inspect.currentframe()).lineno,'2: ' + str(os.listdir()))
       
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
                real_resp = real_resp.replace(i, latestname)
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
        real_resp = real_resp.replace(i.tag, random.choice(i.responses))
    real_resp = real_resp.strip()
    og_conv.append(real_resp)
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'og_conv: {}'.format(og_conv))
    think(inspect.getframeinfo(inspect.currentframe()).lineno,'saying {}'.format(real_resp))
    say(real_resp)
    if gpt:
        client.beta.threads.messages.create(thread_id=thread.id, role="assistant",content=real_resp)
        
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
                     
    txtblb = textblob.TextBlob(resp)
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
