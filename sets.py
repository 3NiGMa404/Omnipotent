positives=['yes','yep','for sure','affirmative','definitely',"i'm afraid so",'i think so']
negatives=['no','nope','nah','definitely not',"i don't think so","i'm afraid not",'nae']

class yesnoset:
    def __init__(self,responses,beginnings,tag,savenoun=False):
       self.beginnings=beginnings
       self.responses=responses
       self.tag=tag
       self.savenoun=savenoun

do_you_p=yesnoset(['i do','yeah, i do']+positives,["do you "],"!do_you_p!"'!do_u_p!')
do_you_n=yesnoset(["nah, i don't",'i do not']+negatives,["do you "],"!do_you_n!"'!do_u_n!')
do_i_p=yesnoset(['you do','i think you do']+positives,["do i "],"!do_i_p!"'!do_i_p!')
dont_i_p=yesnoset(['you do','i think you do']+positives,["don't i ,dont i "],"!dont_i_p!"'!dont_i_p!')
dont_i_n=yesnoset(["you don't","i don't you do"]+negatives,["don't i ,dont i "],"!dont_i_n!"'!dont_i_n!')
dont_u_p=yesnoset(['i do','i think i do']+positives,["don't you ,dont you "],"!dont_u_p!"'!dont_u_p!')
dont_u_n=yesnoset(["i don't",'i do not',"i don't think i do"]+negatives,["don't you ,dont you "],"!dont_u_n!"'!dont_u_n!')
do_i_n=yesnoset(["you don't","i don't think you do"]+negatives,["do i "],"!do_i_n!"'!do_i_n!')
things_i_can_do=['talk','read','speak','understand me','understand']                                                 #Finish this!
can_i_p=yesnoset(['you can!','yes, you can','i think you can']+positives,['can i '],"!can_i_p!"'!can_i_p!')
can_i_n=yesnoset(["you can't","nah, you can't","i don't think you can"]+negatives,['can i '],"!can_i_n!"'!can_i_n!')             #maybe add these to another file then "from thatfile import *"
can_u_p=yesnoset(['yes, i can','i can','i think i can']+positives,['can you '],"!can_u_p!"'!can_u_p!')
can_u_n=yesnoset(["no i can't",'i can not',"i don't think i can"]+negatives,['can you '],"!can_u_n!"'!can_u_n!')
will_i_p=yesnoset(['yes you will','you will','i think you will']+positives,['will i '],"!will_i_p!"'!will_i_p!')
will_i_n=yesnoset(["i don't think you will",'no you will not','you will not']+negatives,['will i '],"!will_i_n!"'!will_i_n!')
will_u_p=yesnoset(['yes i will','i will','i think i will']+positives,['will you '],"!will_u_p!"'!will_u_p!')
will_u_n=yesnoset(["i don't think i will",'no i will not','i will not',"i won't"]+negatives,['will you '],"!will_u_n!"'!will_u_n!')

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
me=open('Me.txt','r')
me_r=me.read()
me.close()
things_i_am=me_r.split('\n')
arent_u_p=yesnoset(['i am','i think i am']+positives,["arent you ","aren't you "],"!arent_u_p!")
arent_u_n=yesnoset(['i am not',"i don't think i am"]+negatives,["arent you ","aren't you "],"!arent_u_n!")

cant_u_p=yesnoset(['i can','i think i can']+positives,['cant you ',"can't you "],'!cant_u_p!')
cant_u_n=yesnoset(['i can not','i dont think i can']+negatives,['cant you ',"can't you "],'!cant_u_p!')
cant_i_p=yesnoset(['you can!','i think you can']+positives,['cant i ',"can't i "],'!cant_i_p!')
cant_i_n=yesnoset(['you can not!',"yes, you can't","i don't think you can"]+negatives,['cant i ',"can't i "],'!cant_i_n!')
dont_noun_p=yesnoset(['they do','i think they do']+positives,["don't ,dont "],"!dont_noun_p!"'!dont_noun_p!',True)
dont_noun_n=yesnoset(["they don't","i don't think they do"]+negatives,["dont ","don't "],"!dont_noun_n!"'!dont_noun_n!',True)
arent_noun_p=yesnoset(['they are','i think they are']+positives,["arent ","aren't "],"!arent_noun_p!",True)
arent_noun_n=yesnoset(['they are not',"i don't think they are"]+negatives,["arent ","aren't "],"!arent_noun_n!",True)
are_noun_p=yesnoset(['they are','i think they are','yes, they are']+positives,["are "],"!are_noun_p!",True)
are_noun_n=yesnoset(['they are not',"i don't think they are","nah, they're not"]+negatives,["are "],"!are_noun_n!",True)
do_noun_p=yesnoset(['they do','i think they do','yeah, they do']+positives,['do '],"!do_noun_p!"'!do_noun_p!',True) #Do noun p
do_noun_n=yesnoset(["they don't",'they do not',"i don't think they do"]+negatives,['do '],"!do_noun_n!"'!do_noun_n!',True)


all_resp=[do_you_p,do_you_n,do_i_p,dont_i_p,dont_i_n,dont_u_p,dont_u_n,do_i_n,can_i_p,can_i_n,can_u_p,can_u_n,will_i_p,will_i_n,will_u_p,will_u_n,wont_i_p,wont_i_n,wont_u_p,wont_u_n,would_i_p,would_i_n,would_u_p,would_u_n,wouldnt_i_p,wouldnt_i_n,wouldnt_u_p,wouldnt_u_n,could_i_p,could_i_n,could_u_p,could_u_n,couldnt_i_p,couldnt_i_n,couldnt_u_p,couldnt_u_n,should_i_p,should_i_n,should_u_p,should_u_n,shouldnt_i_p,shouldnt_i_n,shouldnt_u_p,shouldnt_u_n,was_i_p,was_i_n,were_u_p,were_u_n,are_u_p,are_u_n,arent_u_p,arent_u_n,cant_u_p,cant_u_n,cant_i_p,cant_i_n,dont_noun_p,dont_noun_n,arent_noun_p,arent_noun_n,are_noun_p,are_noun_n,do_noun_p,do_noun_n]
