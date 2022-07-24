import math


# compare the odds if there is any profit. input from per, prints 
j=[['Liverpool - Crystal Palace', ['12.25', '6', 1.25], ['12.25', '6', 1.25], ['1.19', '6', 13.0], ['1.19', '6', 14.0], ['1.19', '12.25', 6.2], ['1.19', '12.25', 6.8], [13.0, 6.2, '1.19'], [13.0, 6.2, 1.25], [1.25, 6.2, '12.25'], [1.25, 6.2, 14.0], [1.25, 13.0, '6'], [1.25, 13.0, 6.8], [14.0, 6.8, '1.19'], [14.0, 6.8, 1.25], [1.25, 6.8, '12.25'], [1.25, 6.8, 13.0], [1.25, 14.0, '6'], [1.25, 14.0, 6.2]]]

def win(a,b,c):

    
    a=float(a)
    b=float(b)
    c=float(c)
    s=(1/a)*100+(1/b)*100+(1/c)*100
    s=s/100
    #print(s)
    if s < 100:

        
        profit=(100/(s))-100
       # print(f'profit is possible and the profit is {profit}%')
        if profit >=5:
            ask=(100*(1/a))/s
            bsk=(100*(1/b))/s
            csk=(100*(1/c))/s
            
            #print(f'Stake is away team {round(ask,2)}%, home team {round(csk,2)}%, draw {round(bsk,2)}%')
            return {"home":round(csk,2),"away":round(ask,2),"draw":round(bsk,2),"profit":round(profit,2)}
        return 'Low profit'
    else:
       # print((f'Not possible'))
        
        return 'Not possible'

#res= win(a,d,h)

def stake(a,b,c,d,sk):
    return {"home":round(a*sk/100,2),"away":round(b*sk/100,2),"draw":round(c*sk/100,2),"profit":round(d*sk/100,2)}

#print(stake(res["home"],res["away"],res["draw"],res["profit"],100))

def po(j):
    t=[]
    for j1 in j:
        
        for i in range(1,len(j1)):
            #print(j1)
            if win(j1[i][0],j1[i][1],j1[i][2])=='Not possible' or win(j1[i][0],j1[i][1],j1[i][2])=='Low profit':
                pass
                #print('forget it')
            else:
                res=win(j1[i][0],j1[i][1],j1[i][2])
                t.append(stake(res["home"],res["away"],res["draw"],res["profit"],100),j1[i],j1[0])
                #print(win(j1[i][0],j1[i][1],j1[i][2]),j1[i],j1[0])
    return t
#po(j)
