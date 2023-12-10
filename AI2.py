"""
Script: Omnipotent Lillypad AI2
Version: 1.3.5
Name: James Pinder (https://github.com/3NiGMa404)
Date: 2023-12-10
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
import commands
import os
import psutil
import euc_dist
import warnings

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
if not os.path.exists('Memory'):
    os.makedirs('Memory')
if not os.path.isfile('thoughts.txt'):
    x = open('thoughts.txt', 'w+')
    x.close()
if not os.path.exists('Info'):
    os.makedirs('Info')
print('done')
bar.update(11)
os.system('cls')
print('\nloading speech...')


def think(string, statedatetime=True):
    c = open('thoughts.txt', 'a+')
    if statedatetime:
        c.write('\n' + str(datetime.datetime.now()) + ': ' + string)
    else:
        c.write('\n' + string)
    c.close()


think('\nNEW SESSION\n\n', statedatetime=False)


def say(text):
    from inout import ret
    ret(text)


def add_noun(name, Class, data=''):
    if not os.path.exists('Info/' + Class):
        os.makedirs('Info/' + Class)
    if os.path.isfile('Info/' + Class + '/' + name +
                      '.txt'):  # Finish adding classes here
        openinfo = open('Info/' + Class + '/' + name + '.txt', 'a')
    else:
        openinfo = open('Info/' + Class + '/' + name + '.txt', 'w+')
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
think(st + '({},{})'.format(mood[0], mood[1]))


def getinput():
    from inout import git
    return git()


mynames = ['omnipotent']
os.system('cls')
talkingto = input('who are you? ')
with open('takephoto.txt','w+') as w:
    w.write(talkingto)
gend = 'unknown'
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
think("{}'s gender is {}".format(talkingto, gend))
conv = []

neutral = ['maybe', 'maybe, maybe not']


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
            think('Chose "' + saying + '" from ' + str(can_u_p.responses))
            return saying
        else:
            saying = random.choice(can_u_n.responses)
            think('Chose "' + saying + '" from ' + str(can_u_n.responses))
            return saying
    if convo[0].startswith('cant you '):
        if convo[0].replace('cant you ', '') in things_i_can_do:
            saying = random.choice(cant_u_p.responses)
            think('Chose "' + saying + '" from ' + str(cant_u_p.responses))
            return saying
        else:
            saying = random.choice(cant_u_n.responses)
            think('Chose "' + saying + '" from ' + str(cant_u_n.responses))
            return saying
    if convo[0].startswith('are you '):
        if convo[0].replace('are you ', '') in things_i_am:
            saying = random.choice(are_u_p.responses)
            think('Chose "' + saying + '" from ' + str(are_u_p.responses))
            return saying
        else:
            saying = random.choice(are_u_n.responses)
            think('Chose "' + saying + '" from ' + str(are_u_n.responses))
            return saying
    if convo[0].startswith('arent you '):
        if convo[0].replace('arent you ', '') in things_i_am:
            saying = random.choice(arent_u_p.responses)
            think('Chose "' + saying + '" from ' + str(arent_u_p.responses))
            return saying
        else:
            saying = random.choice(arent_u_n.responses)
            think('Chose "' + saying + '" from ' + str(arent_u_n.responses))
            return saying
    for i in range(len(convo)):
        if os.path.exists('Memory/' + str('/'.join(conv[i:len(convo)]))):
            think('Memory/' + str('/'.join(conv[i:len(convo)])) + ' exists')
            answers = os.listdir('Memory/' + '/'.join(convo[i:len(convo)]))
            if len(answers) > 0:
                think(
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
                think('chose ' + saying + ' from ' + str(answers))
                return saying

        # Check for all of the sets' patterns
        think('checking for recognized patterns...')
        count = 0
        choices = []

        for i in all_resp:
            for h in i.beginnings:
                j = h.replace(',', '')
                if convo[-1].startswith(j) or convo[-1].endswith(j.strip()):
                    think('{} startswith {} ({})'.format(convo[-1], j, i))
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
                            think('{}:{}'.format(i.tag, i.responses))
                            choices.extend(i.responses)

        if len(choices) > 1:
            saying = random.choice(choices)
            think('chose ' + saying + ' from ' + str(choices))
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
    if 18 < hour < 21:
        current_time_word = 'evening'
    if hour > 20:
        current_time_word = 'night'
    time_words.remove(current_time_word)

    resp = None
    global conv, latestname, latestfemale, latestmale, latestpronoun, latestname, mood
    think('getting input...')
    theysaid = str(
        getinput().lower().replace(
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
            ''))
    og_theysaid = theysaid
    txtblb = textblob.TextBlob(theysaid)
    mood[0] = (mood[0] * 0.95) + (txtblb.sentiment.polarity * 0.05)
    mood[1] = (mood[1] * 0.95) + (txtblb.sentiment.subjectivity * 0.05)
    think('input before preprocessing: {}'.format(theysaid))

    theysaid = theysaid.replace(talkingto, '!speaker!')
    if theysaid == 'exit':
        think('Saving and exiting...')
        raise SystemExit('Saving and exiting')
    if theysaid == 'reset':
        import reset
        raise SystemExit('Saving and exiting')
    for command in commands.commands:
        if theysaid in command.inp:
            command.func()
            say(random.choice(command.responses))
            input('Press RETURN to exit')
            raise SystemExit('Saving and exiting')
    choices_temp = []
    if theysaid == 'what is your name' or theysaid == 'whats your name' or theysaid == 'what is ur name' or theysaid == 'whats ur name' or theysaid == 'what are you called' or theysaid == 'what are u called':
        choices_temp.append(
            ['my name is !speaker!', 'i am called !speaker!', 'call me !speaker!'])
    think('theysaid is {}'.format(theysaid))
    opinionated = {
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
        'dont mind': 0.1,
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
        0.1: 'dont mind'}
    opiniated_reversed_neg = {-0.95: 'despise', -0.85: 'really hate', -0.75: 'hate', -0.5: 'really dislike', -
    0.5: 'really dont like', -0.4: 'dislike', -0.3: 'dont like', -0.1: 'am not fond of'}
    for i in list(opinionated.keys()):
        if theysaid.startswith('i ' + i) and not resp:
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
                newopinion = opinion + (random.gauss(0.05, 0.01) * min(
                    max([2 * mood[0] * opinionated[i] + random.gauss(0, 0.2), -1]), 1))
                with open('Info/Opinions/' + theysaid.replace('i ' + i + ' ', '') + '.txt', 'w+') as opopinion:
                    opopinion.write(str(newopinion))
                opinion = newopinion
            except BaseException:
                with open('Info/Opinions/' + theysaid.replace('i ' + i + ' ', '') + '.txt', 'w+') as opopinion:
                    opinion = min(
                        max([2 * mood[0] * opinionated[i] + random.gauss(0, 0.2), -1]), 1)
                    opopinion.write(str(opinion))
            
            if opinion > 0:
                for cur in opiniated_reversed_pos:
                    if opinion > cur:
                        
                        howmuchilikeit = opiniated_reversed_pos[cur]
                        if howmuchilikeit == i and random.randint(1, 3) == 3:
                            resp = random.choice(
                                ['as do i', 'same', 'same here', 'agreed'])
                        if not resp:
                            if inflect.singular_noun(
                                    theysaid.replace('i ' + i + ' ', '')):
                                resp = random.choice(
                                    [random.choice(['i ', 'well i ']) + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''),
                                     random.choice(['i ', 'well i ']) + howmuchilikeit + ' them'])
                            else:
                                resp = random.choice(
                                    [random.choice(['i ', 'well i ']) + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''), random.choice(['i ', 'well i ']) + howmuchilikeit + ' it'])
            if opinion < 0:
                for cur in opiniated_reversed_neg:
                    if opinion < cur:
                        howmuchilikeit = opiniated_reversed_neg[cur]
                        if howmuchilikeit == i and random.randint(1, 3) == 3:
                            resp = random.choice(
                                ['same', 'same here', 'agreed'])
                        if not resp:
                            if inflect.singular_noun(
                                    theysaid.replace('i ' + i + ' ', '')):
                                resp = random.choice(
                                    [random.choice(['i ', 'well i ']) + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''),
                                     random.choice(['i ', 'well i ']) + howmuchilikeit + ' them'])
                            else:
                                resp = random.choice(
                                    [random.choice(['i ', 'well i ']) + howmuchilikeit + ' ' + theysaid.replace(
                                        'i ' + i + ' ', ''), random.choice(['i ', 'well i ']) + howmuchilikeit + ' it'])
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

    if theysaid.startswith('how are you') or theysaid.startswith('how are u'):
        think('Said how are you')
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
            think('Choices temp is now {}'.format(choices_temp))
    if theysaid.startswith('you are ') or theysaid.startswith('are you '):
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
                        '')).sentiment.polarity > 0:
                resp = random.choice(['!pos!, i am', '!pos!', 'i am'])
                add_to_me = open('Me.txt', 'a')
                add_to_me.write(theysaid.replace('you are ', ''))
                add_to_me.close()
            else:
                resp = random.choice(['!neg!, i am', '!neg!', 'i am not'])
    think('checking if {} starts with i'.format(theysaid))
    if len(theysaid) > 1 and theysaid.startswith('i ') and 'VB' in pyinflect.getAllInflections(
            theysaid.split(' ')[1]) and not theysaid.split(' ')[1] in ['do', 'can', 'will', 'would', 'could', 'should','am']:
        think('ok this is interesting')
        add_noun(talkingto, 'PERSON', makethird(theysaid, gend == 'male'))
        think(makethird(theysaid, gend == 'male'))
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
                '') in things_i_can_do:
                resp = random.choice(
                    ['i can', 'why not', 'why not, i can', 'really, i can'])
            else:
                resp = random.choice(
                    ['same', 'nor can i', "i can't either", "i also can't"])
        if theysaid.startswith('i am '):
            if theysaid.replace('i am ', '') in things_i_am:
                resp = random.choice(
                    ['same', 'as am i', 'so am i', theysaid + ' too'])            #YOU WERE HALFWAY THROUGH THIS LAST TIME
            else:                                                                    #Checking if the ai is things that people are
                resp = random.choice(
                    ["yeah, i am not", "really, i am not", "are you, i am not", 'cool'])
        if theysaid.startswith('i am not'):
            if theysaid.replace('i am not', '') in things_i_am:
                resp = random.choice(
                    ['same', 'nor am i', 'i am also not', theysaid + ' either'])            #YOU WERE HALFWAY THROUGH THIS LAST TIME
            else:                                                                    #Checking if the ai is things that people are
                resp = random.choice(
                    ["yeah, i am", "really, i am", "are you, i am", 'cool'])
    if theysaid.startswith('tell me about '):
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
            think(str(e))
            if theysaid.replace('tell me about ', '') in male:
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

    if theysaid.startswith('is '):
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
            if j in theysaid and not j in positives and not j in negatives:
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
    think('input after preprocessing: {}'.format(theysaid))
    og_conv = list(conv)
    og_conv.append(og_theysaid)
    conv.append(theysaid)
    think('conv:{}'.format(conv))
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
                dictlist.append([value, key])
    for i in conv_f2:
        conv_f3.extend(i.split(' '))
    for conv_version in thisfunction(dictlist, '/'.join(conv)):
        choices_temp.append(find_response(conv))
    think('thisfunction returned {}'.format(str(list(thisfunction(dictlist, '/'.join(conv))))))
    idk = False
    think('choices temp is now {}'.format(choices_temp))
    for i in range(2):
        if None in choices_temp:
            choices_temp.remove(None)
    if choices_temp:
        resp = random.choice(choices_temp) ###
        think('selecting {} from {}'.format(resp, choices_temp))
    if resp == None:
        if theysaid.startswith('why ') and len(theysaid.split(' ')) > 2:
            resp = random.choice(
                ["im not sure", "i dont know", "just because", "how should i know"])
        if theysaid.startswith('what ') or theysaid.startswith(
                'who ') or theysaid.startswith('where ') or theysaid.startswith('how '):
            resp = random.choice(["im not sure",
                                  "i dont know",
                                  "i don't know, " + theysaid,
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
            if not os.path.exists('Memory/' + '/'.join(conv[i:len(conv)])):
                os.makedirs('Memory/' + '/'.join(conv[i:len(conv)]))

        conv = []
        og_conv = []

        think('1: ' + str(os.listdir()))
        os.chdir(path)
        think('2: ' + str(os.listdir()))
        for i in os.listdir('Memory/'):
            if len(os.listdir('Memory/' + str(i))) == 0:
                resp = str(i)
                think('cleared and spoke')
                break
    if resp == None:
        resp = theysaid
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
    think('og_conv: {}'.format(og_conv))
    think('saying {}'.format(real_resp))
    say(real_resp)

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

    think('ogconv2: {}\nconv2: {}'.format(og_conv2, conv2))
    dictlist = []
    for key, value in replacements.items():  # Make sure this checks both theysaid and pretheysaid to find the correct dictionary value that contains both sides of it
        for _ in range(''.join(conv2).count(value)):
            if ''.join(conv2).count(key) == ''.join(conv2).count(value):
                dictlist.append([value, key])
    for i in dictlist:
        for j in range(len(conv)):
            if i[1] in conv[j]:
                conv[j].replace(i[1], i[0])
    think('thisfunc ' + str(list(thisfunction(dictlist, '/'.join(og_conv)))))
    think('dictlist={}'.format(dictlist))

    for current_conv in list(thisfunction(dictlist, '/'.join(og_conv))):
        curr_split_conv = current_conv.split('/')
        for i in range(len(curr_split_conv)):
            if not os.path.exists(
                    'Memory/' + '/'.join(curr_split_conv[i:len(curr_split_conv)])):
                os.makedirs('Memory/' +
                            '/'.join(curr_split_conv[i:len(curr_split_conv)]))
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
        think(traceback.format_exc())

'''
   © Copyright 2023 James Pinder

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
