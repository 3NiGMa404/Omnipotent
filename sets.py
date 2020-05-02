positives=['yes','yep','for sure','affirmative','definitely',"i'm afraid so",'i think so']
negatives=['no','nope','nah','definitely not',"i don't think so","i'm afraid not",'nae']

class yesnoset:
    def __init__(self,responses,beginnings,tag,savenoun=False):
       self.beginnings=beginnings
       self.responses=responses
       self.tag=tag
       self.savenoun=savenoun

do_you_p=yesnoset(['i do','yeah, i do']+positives,["do you "],"!do_you_p!")
do_you_n=yesnoset(["nah, i don't",'i do not']+negatives,["do you "],"!do_you_n!")
do_i_p=yesnoset(['you do','i think you do']+positives,["do i "],"!do_i_p!")
dont_i_p=yesnoset(['you do','i think you do']+positives,["don't i ,dont i "],"!dont_i_p!")
dont_i_n=yesnoset(["you don't","i don't you do"]+negatives,["don't i ,dont i "],"!dont_i_n!")
dont_u_p=yesnoset(['i do','i think i do']+positives,["don't you ,dont you "],"!dont_u_p!")
dont_u_n=yesnoset(["i don't",'i do not',"i don't think i do"]+negatives,["don't you ,dont you "],"!dont_u_n!")
do_i_n=yesnoset(["you don't","i don't think you do"]+negatives,["do i "],"!do_i_n!")
things_i_can_do=['talk','read','speak','understand me','understand']
can_i_p=yesnoset(['you can!','yes, you can','i think you can']+positives,['can i '],"!can_i_p!")
can_i_n=yesnoset(["you can't","nah, you can't","i don't think you can"]+negatives,['can i '],"!can_i_n!")
can_u_p=yesnoset(['yes, i can','i can','i think i can']+positives,['can you '],"!can_u_p!")
can_u_n=yesnoset(["no i can't",'i can not',"i don't think i can"]+negatives,['can you '],"!can_u_n!")
will_i_p=yesnoset(['yes you will','you will','i think you will']+positives,['will i '],"!will_i_p!")
will_i_n=yesnoset(["i don't think you will",'no you will not','you will not']+negatives,['will i '],"!will_i_n!")
will_u_p=yesnoset(['yes i will','i will','i think i will']+positives,['will you '],"!will_u_p!")
will_u_n=yesnoset(["i don't think i will",'no i will not','i will not',"i won't"]+negatives,['will you '],"!will_u_n!")
wont_i_p=yesnoset(['you will','i think you will']+positives,["wont i ","won't i "],"!wont_i_p!")
wont_i_n=yesnoset(["i don't think you will","you won't"]+negatives,["wont i ","won't i "],"!wont_i_n!")
wont_u_p=yesnoset(['i will','i think i will']+positives,["wont you ","won't you "],"!wont_u_p!")
wont_u_n=yesnoset(["i don't think i will","i won't"]+negatives,["wont you ","won't you "],"!wont_u_n!")
would_i_p=yesnoset(['you would','i think you would','yeah, you would']+positives,["would i "],"!would_i_p!")
would_i_n=yesnoset(["you wouldn't", "i don't think you would","nah, you wouldn't"]+negatives,["would i "],"!would_i_n!")
would_u_p=yesnoset(['i would','i think i would','yeah, i would']+positives,["would you "],"!would_u_p!")
would_u_n=yesnoset(["i wouldn't", "i don't think i would","nah, i wouldn't"]+negatives,["would you "],"!would_u_n!")
wouldnt_i_p=yesnoset(['you would','i think you would']+positives,["wouldnt i ","wouldn't i "],"!wouldnt_i_p!")
wouldnt_i_n=yesnoset(["you wouldn't", "i don't think you would","nah, you wouldn't"]+negatives,["wouldnt i ","wouldn't i "],"!wouldnt_i_n!")
wouldnt_u_p=yesnoset(['i would','i think i would']+positives,["wouldnt you ","wouldn't you "],"!wouldnt_u_p!")
wouldnt_u_n=yesnoset(["i wouldn't", "i don't think i would","i would not"]+negatives,["wouldnt you ","wouldn't you "],"!wouldnt_u_n!")
could_i_p=yesnoset(['you could','i think you could','yeah, you could']+positives,["could i "],"!could_i_p!")
could_i_n=yesnoset(["you couldn't", "i don't think you could","nah, you couldn't"]+negatives,["could i "],"!could_i_n!")
could_u_p=yesnoset(['i could','i think i could','yeah, i could']+positives,["could you "],"!could_u_p!")
could_u_n=yesnoset(["i couldn't", "i don't think i could","nah, i couldn't"]+negatives,["could you "],"!could_u_n!")
couldnt_i_p=yesnoset(['you could','i think you could']+positives,["couldnt i ","couldn't i "],"!couldnt_i_p!")
couldnt_i_n=yesnoset(["you couldn't", "i don't think you could","nah, you couldn't"]+negatives,["couldnt i ","couldn't i "],"!couldnt_i_n!")
couldnt_u_p=yesnoset(['i could','i think i could']+positives,["couldnt you ","couldn't you "],"!couldnt_u_p!")
couldnt_u_n=yesnoset(["i couldn't", "i don't think i could","i could not"]+negatives,["couldnt you ","couldn't you "],"!couldnt_u_n!")
should_i_p=yesnoset(['you should','i think you should','yeah, you should']+positives,["should i "],"!should_i_p!")
should_i_n=yesnoset(["you shouldn't", "i don't think you should","nah, you shouldn't"]+negatives,["should i "],"!should_i_n!")
should_u_p=yesnoset(['i should','i think i should','yeah, i should']+positives,["should you "],"!should_u_p!")
should_u_n=yesnoset(["i shouldn't", "i don't think i should","nah, i shouldn't"]+negatives,["should you "],"!should_u_n!")
shouldnt_i_p=yesnoset(['you should','i think you should']+positives,["shouldnt i ","shouldn't i "],"!shouldnt_i_p!")
shouldnt_i_n=yesnoset(["you shouldn't", "i don't think you should","nah, you shouldn't"]+negatives,["shouldnt i ","shouldn't i "],"!shouldnt_i_n!")
shouldnt_u_p=yesnoset(['i should','i think i should']+positives,["shouldnt you ","shouldn't you "],"!shouldnt_u_p!")
shouldnt_u_n=yesnoset(["i shouldn't", "i don't think i should","i should not"]+negatives,["shouldnt you ","shouldn't you "],"!shouldnt_u_n!")
was_i_p=yesnoset(['yes, you were','you were','i think you were']+positives,["was i "],"!was_i_p!")
was_i_n=yesnoset(["nah, you weren't","you weren't","i don't think you were"]+negatives,["was i "],"!was_i_n!")
were_u_p=yesnoset(['i was','yeah, i was']+positives,["were you "],"!were_u_p!")
were_u_n=yesnoset(["i wasn't", "nah, i wasn't"]+negatives,["were you "],"!were_u_n!")
are_u_p=yesnoset(['i am','yeah, i am','i think i am']+positives,["are you "],"!are_u_p!")
are_u_n=yesnoset(['i am not',"nah, i'm not","i don't think i am"]+negatives,["are you "],"!are_u_n!")
arent_u_p=yesnoset(['i am','i think i am']+positives,["arent you ","aren't you "],"!arent_u_p!")
arent_u_n=yesnoset(['i am not',"i don't think i am"]+negatives,["arent you ","aren't you "],"!arent_u_n!")
cant_u_p=yesnoset(['i can','i think i can']+positives,['cant you ',"can't you "],'!cant_u_p!')
cant_u_n=yesnoset(['i can not','i dont think i can']+negatives,['cant you ',"can't you "],'!cant_u_p!')
cant_i_p=yesnoset(['you can!','i think you can']+positives,['cant i ',"can't i "],'!cant_i_p!')
cant_i_n=yesnoset(['you can not!',"no, you can't","i don't think you can"]+negatives,['cant i ',"can't i "],'!cant_i_n!')

i_will_n=yesnoset(['i wont','i wont'],['i will '],'!i_will_n!')
i_will_p=yesnoset(['same','so will i'],['i will '],'!i_will_p!')
i_will_q=yesnoset(['are you sure','why though'],['i will '],'!i_will_q!')

i_wont_n=yesnoset(['same','nor will i'],['i wont ',"i won't"],'!i_wont_n!')
i_wont_p=yesnoset(['really, i will','i will'],['i wont ',"i won't"],'!i_wont_p!')
i_wont_q=yesnoset(['are you sure','why not'],['i wont ',"i won't"],'!i_will_q!')

i_dont_n=yesnoset(['same','nor do i'],['i dont ',"i don't"],'!i_dont_n!')
i_dont_p=yesnoset(['really, i do','i do'],['i dont ',"i don't"],'!i_dont_p!')
i_dont_q=yesnoset(['are you sure','why not'],['i dont ',"i don't"],'!i_dont_q!')

i_would_n=yesnoset(["i wouldn't",'really, i would not'],['i would '],'!i_would_n!')
i_would_p=yesnoset(['same','so would i'],['i would '],'!i_would_p!')
i_would_q=yesnoset(['are you sure','why though'],['i would '],'!i_would_q!')

i_wouldnt_p=yesnoset(["i would",'really, i would'],['i wouldnt ',"i wouldn't"],'!i_would_n!')
i_wouldnt_n=yesnoset(['same','nor would i'],['i wouldnt ',"i wouldn't"],'!i_would_p!')
i_wouldnt_q=yesnoset(['are you sure','why not'],['i wouldnt ',"i wouldn't"],'!i_would_q!')

i_could_n=yesnoset(["i couldn't",'really, i could not'],['i could '],'!i_could_n!')
i_could_p=yesnoset(['same','so could i'],['i could '],'!i_could_p!')
i_could_q=yesnoset(['are you sure','why though'],['i could '],'!i_could_q!')

i_couldnt_p=yesnoset(["i could",'really, i could'],['i couldnt ',"i couldn't"],'!i_could_n!')
i_couldnt_n=yesnoset(['same','nor could i'],['i couldnt ',"i couldn't"],'!i_could_p!')
i_couldnt_q=yesnoset(['are you sure','why not'],['i couldnt ',"i couldn't"],'!i_could_q!')

i_should_n=yesnoset(["i shouldn't",'really, i should not'],['i should '],'!i_should_n!')
i_should_p=yesnoset(['same','so should i'],['i should '],'!i_should_p!')
i_should_q=yesnoset(['are you sure','why though'],['i should '],'!i_should_q!')

i_shouldnt_p=yesnoset(["i should",'really, i should'],['i shouldnt ',"i shouldn't"],'!i_should_n!')
i_shouldnt_n=yesnoset(['same','nor should i'],['i shouldnt ',"i shouldn't"],'!i_should_p!')
i_shouldnt_q=yesnoset(['are you sure','why not'],['i shouldnt ',"i shouldn't"],'!i_should_q!')
#New
i_think_p=yesnoset(['i agree','same','i think so too','agreed'],["i think "],'!i_think_p!')
i_think_n=yesnoset(['i disagree',"i don't think so","i don't",'disagree'],["i think "],'!i_think_n!')
i_think_q=yesnoset(['why do you think that',"why"],["i think "],'!i_think_q!')
##Noun
dont_noun_p=yesnoset(['they do','i think they do']+positives,["don't ,dont "],"!dont_noun_p!",True)
dont_noun_n=yesnoset(["they don't","i don't think they do"]+negatives,["dont ","don't "],"!dont_noun_n!",True)
arent_noun_p=yesnoset(['they are','i think they are']+positives,["arent ","aren't "],"!arent_noun_p!",True)
arent_noun_n=yesnoset(['they are not',"i don't think they are"]+negatives,["arent ","aren't "],"!arent_noun_n!",True)
are_noun_p=yesnoset(['they are','i think they are','yes, they are']+positives,["are "],"!are_noun_p!",True)
are_noun_n=yesnoset(['they are not',"i don't think they are","nah, they're not"]+negatives,["are "],"!are_noun_n!",True)
do_noun_p=yesnoset(['they do','i think they do','yeah, they do']+positives,['do '],"!do_noun_p!",True)
do_noun_n=yesnoset(["they don't",'they do not',"i don't think they do"]+negatives,['do '],"!do_noun_n!",True)
is_noun_p=yesnoset(['it is','yes, it is','yeah, it is']+positives,['is '],"!is_noun_p!",True)
is_noun_n=yesnoset(["it isn't",'no, it is not',"nah, it isn't"]+negatives,['is '],"!is_noun_n!",True)
isnt_noun_p=yesnoset(['it is','yes, it is','yeah, it is'],['isnt ',"isn't"],"!isnt_noun_p!",True)
isnt_noun_n=yesnoset(["it isn't",'no, it is not',"nah, it isn't"],['isnt ',"isn't"],"!isnt_noun_n!",True)
can_noun_p=yesnoset(['they can','yes, they can']+positives,['can '],'!can_noun_p!',True)
can_noun_n=yesnoset(['they cannot',"no, they can't"]+negatives,['can '],'!can_noun_n!',True)               #Replace it with they if plural and vice versa, if savenoun=True
cant_noun_p=yesnoset(['they can','yes, they can'],['cant ',"can't "],'!cant_noun_p!',True)
cant_noun_n=yesnoset(['they cannot',"no, they can't"],['cant ',"can't "],'!cant_noun_n!',True)
was_noun_p=yesnoset(['yes, it was','it was','i think it was']+positives,["was "],"!was_noun_p!",True)
was_noun_n=yesnoset(["no, it wasn't","it wasn't","i don't think it was"]+negatives,["was "],"!was_noun_n!",True)
wasnt_noun_p=yesnoset(['yes, it was','it was','i think it was'],["wasnt ","wasn't"],"!wasnt_noun_p!",True)
wasnt_noun_n=yesnoset(["no, it wasn't","it wasn't","i don't think it was"],["wasnt ","wasn't"],"!wasnt_noun_n!",True)
will_noun_p=yesnoset(['yes it will','it will','i think it will']+positives,['will '],"!will_noun_p!",True)
will_noun_n=yesnoset(['no it will not',"it won't","i don't think it will"]+negatives,['will '],"!will_noun_n!",True)
wont_noun_p=yesnoset(['yes it will','it will','i think it will'],["wont ","won't "],"!wont_noun_p!",True)
wont_noun_n=yesnoset(['no it will not',"it won't","i don't think it will"],["wont ","won't "],"!wont_noun_n!",True)
would_noun_p=yesnoset(['they would','i think they would','yeah, they would']+positives,["would "],"!would_noun_p!",True)
would_noun_n=yesnoset(["they wouldn't", "i don't think they would","nah, they wouldn't"]+negatives,["would "],"!would_noun_n!",True)
wouldnt_noun_p=yesnoset(['they would','i think they would','yeah, they would'],["wouldnt ","wouldn't "],"!wouldnt_noun_p!",True)
wouldnt_noun_n=yesnoset(["they wouldn't", "i don't think they would","nah, they wouldn't"],["wouldnt ","wouldn't "],"!wouldnt_noun_n!",True)
could_noun_p=yesnoset(['they could','i think they could','yeah, they could']+positives,["could "],"!could_noun_p!",True)
could_noun_n=yesnoset(["they couldn't", "i don't think they could","nah, they couldn't"]+negatives,["could "],"!could_noun_n!",True)
couldnt_noun_p=yesnoset(['they could','i think they could','yeah, they could'],["couldnt ","couldn't "],"!couldnt_noun_p!",True)
couldnt_noun_n=yesnoset(["they couldn't", "i don't think they could","nah, they couldn't"],["couldnt ","couldn't "],"!couldnt_noun_n!",True)
should_noun_p=yesnoset(['they should','i think they should','yeah, they should']+positives,["should "],"!should_noun_p!",True)
should_noun_n=yesnoset(["they shouldn't", "i don't think they should","nah, they shouldn't"]+negatives,["should "],"!should_noun_n!",True)
shouldnt_noun_p=yesnoset(['they should','i think they should','yeah, they should'],["shouldnt ","shouldn't "],"!shouldnt_noun_p!",True)
shouldnt_noun_n=yesnoset(["they shouldn't", "i don't think they should","nah, they shouldn't"],["shouldnt ","shouldn't "],"!shouldnt_noun_n!",True)
were_noun_p=yesnoset(['they were','i think they were','yeah, they were']+positives,["were "],"!were_noun_p!",True)
were_noun_n=yesnoset(["they weren't", "i don't think they were","nah, they weren't"]+negatives,["were "],"!were_noun_n!",True)
werent_noun_p=yesnoset(['they were','i think they were','yeah, they were'],["werent ","weren't "],"!werent_noun_p!",True)
werent_noun_n=yesnoset(["they weren't", "i don't think they were","nah, they weren't"],["werent ","weren't "],"!werent_noun_n!",True)

#Me
me=open('Me.txt','r')
me_r=me.read()
me.close()
things_i_am=me_r.split('\n')
all_resp=[do_you_p,do_you_n,do_i_p,dont_i_p,dont_i_n,dont_u_p,dont_u_n,do_i_n,can_i_p,can_i_n,can_u_p,can_u_n,will_i_p,will_i_n,will_u_p,will_u_n,wont_i_p,wont_i_n,wont_u_p,wont_u_n,would_i_p,would_i_n,would_u_p,would_u_n,wouldnt_i_p,wouldnt_i_n,wouldnt_u_p,wouldnt_u_n,could_i_p,could_i_n,could_u_p,could_u_n,couldnt_i_p,couldnt_i_n,couldnt_u_p,couldnt_u_n,should_i_p,should_i_n,should_u_p,should_u_n,shouldnt_i_p,shouldnt_i_n,shouldnt_u_p,shouldnt_u_n,was_i_p,was_i_n,were_u_p,were_u_n,are_u_p,are_u_n,arent_u_p,arent_u_n,cant_u_p,cant_u_n,cant_i_p,cant_i_n,dont_noun_p,dont_noun_n,arent_noun_p,arent_noun_n,are_noun_p,are_noun_n,do_noun_p,do_noun_n,is_noun_p,is_noun_n,isnt_noun_p,isnt_noun_n,can_noun_p,can_noun_n,cant_noun_p,cant_noun_n,was_noun_p,was_noun_n,wasnt_noun_p,wasnt_noun_n,will_noun_p,will_noun_n,wont_noun_p,wont_noun_n,would_noun_p,would_noun_n,wouldnt_noun_p,wouldnt_noun_n,could_noun_p,could_noun_n,couldnt_noun_p,couldnt_noun_n,should_noun_p,should_noun_n,shouldnt_noun_p,shouldnt_noun_n,were_noun_p,were_noun_n,werent_noun_p,werent_noun_n,i_will_n,i_will_p,i_will_q,i_wont_n,i_wont_p,i_wont_q,i_dont_n,i_dont_p,i_dont_q,i_would_n,i_would_p,i_would_q,i_wouldnt_p,i_wouldnt_n,i_wouldnt_q,i_could_n,i_could_p,i_could_q,i_couldnt_p,i_couldnt_n,i_couldnt_q,i_should_n,i_should_p,i_should_q,i_shouldnt_p,i_shouldnt_n,i_shouldnt_q,i_think_p,i_think_n,i_think_q]

