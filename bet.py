from NaijaBet_Api.bookmakers import bet9ja, betking, nairabet
from NaijaBet_Api.id import Betid
from trs import match
from permutate import permute , per
from check import po




#get the games for different bookies out to match()
def games():
    b9 = bet9ja.Bet9ja()
    b8 = betking.Betking()
    b7 = nairabet.Nairabet()
    a=b9.get_league()
    b=b8.get_league()
    c=b7.get_league()

    d=[a,b,c]
    f=[]
    for j in d:
        e=[]
        for i in range(len(j)):
            #print(j[i]['match'],j[i]['home'],j[i]['away'],j[i]['draw'])
            e.append({'match':j[i]['match'],'odds':[j[i]['home'],j[i]['away'],j[i]['draw']]})
        f.append(e)
    return f
    
#print(po(per(match(games()))))


#run the checker
def c():
    t=po(per(match(games())))
    if len(t)==0:
        print('no game for now')
    else:
        for i in t:
            print(i)
c()

