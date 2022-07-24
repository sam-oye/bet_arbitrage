


#odds=[{'match': 'Crystal Palace - Arsenal', 'all odds': [['3.5', '2.08', '3.6'], [3.55, 2.1, 3.6], [3.65, 2.15, 3.55]]}, {'match': 'Fulham - Liverpool', 'all odds': [['9.4', '1.32', '5.6'], [9.2, 1.34, 5.5], [9.8, 1.33, 6.0]]}, {'match': 'Leeds - Wolves', 'all odds': [['2.27', '3.25', '3.4'], [2.3, 3.25, 3.4], [2.33, 3.3, 3.45]]}, {'match': 'Bournemouth - Aston Villa', 'all odds': [['3.3', '2.22', '3.45'], [3.3, 2.25, 3.45], [3.4, 2.27, 3.55]]}, {'match': 'Tottenham - Southampton', 'all odds': [['1.38', '7.8', '5.2'], [1.4, 7.7, 5.25], [1.42, 8.0, 5.2]]}, {'match': 'Newcastle - Nottingham Forest', 'all odds': [['1.67', '5', '3.7'], [1.7, 5.25, 3.85], [1.68, 5.6, 4.0]]}, {'match': 'Everton - Chelsea', 'all odds': [['5', '1.68', '4'], [5.0, 1.7, 4.0], [5.0, 1.76, 3.95]]}, {'match': 'Manchester United - Brighton', 'all odds': [['1.53', '6.3', '4.35'], [1.55, 6.2, 4.25], [1.58, 6.4, 4.3]]}, {'match': 'Leicester - Brentford', 'all odds': [['2', '3.6', '3.75'], [2.05, 3.6, 3.75], [2.07, 3.7, 3.75]]}, {'match': 'West Ham - Manchester City', 'all odds': [['8.1', '1.37', '5.25'], [8.0, 1.4, 5.25], [8.6, 1.39, 5.4]]}, {'match': 'Aston Villa - Everton', 'all odds': [['2.06', '3.5', '3.2'], [2.1, 3.7, 3.4], [2.08, 3.85, 3.55]]}, {'match': 'Wolves - Fulham', 'all odds': [['2.14', '3.35', '3.2'], [2.2, 3.55, 3.35], [2.14, 3.8, 3.45]]}, {'match': 'Manchester City - Bournemouth', 'all odds': [['1.1', '21', '7.9'], [1.11, 25.0, 9.2], [1.13, 28.0, 10.0]]}, {'match': 'Brighton - Newcastle', 'all odds': [['2.35', '2.98', '3.15'], [2.4, 3.15, 3.3], [2.45, 3.15, 3.35]]}, {'match': 'Southampton - Leeds', 'all odds': [['2.2', '3.1', '3.25'], [2.25, 3.3, 3.45], [2.22, 3.5, 3.5]]}, {'match': 'Arsenal - Leicester', 'all odds': [['1.62', '4.9', '3.85'], [1.65, 5.25, 4.25], [1.65, 5.4, 4.3]]}, {'match': 'Brentford - Manchester United', 'all odds': [['3.4', '2.1', '3.25'], [3.6, 2.15, 3.45], [3.8, 2.12, 3.5]]}, {'match': 'Nottingham Forest - West Ham', 'all odds': [['3.15', '2.18', '3.25'], [3.35, 2.25, 3.45], [3.55, 2.2, 3.55]]}, {'match': 'Chelsea - Tottenham', 'all odds': [['2.12', '3.35', '3.25'], [2.15, 3.55, 3.45], [2.13, 3.75, 3.55]]}, {'match': 'Liverpool - Crystal Palace', 'all odds': [['1.19', '12.25', '6'], [1.25, 13.0, 6.2], [1.25, 14.0, 6.8]]}]
#arrange the home, away and draw games for three different bookies,
#input from match(). output to po()

def permute(x,y,z,w):


    
    a =[1,2,3]
    b=[4,5,6]
    c=[7,8,9]
    
    e=0
    f=[w]
    for i in range(3):
        d=[]
        g=[]
        for j in range(3):
            
            if a[i]!=a[j]:
                d.append(x[j])
                g.append(x[j])
        
       
        for m in range(1):
            d.append(y[e])
            f.append(d)
            #print(d)
            g.append(z[e])
            f.append(g)
            
            #print(g)
            e+=1
    e=0
    for i in range(3):
        d=[]
        g=[]
        for j in range(3):
            
            if b[i]!=b[j]:
                d.append(y[j])
                g.append(y[j])
        
       
        for m in range(1):
            d.append(x[e])
            f.append(d)
            #print(d)
            g.append(z[e])
            f.append(g)
            
            #print(g)
            e+=1

    e=0
    for i in range(3):
        d=[]
        g=[]
        for j in range(3):
            
            if c[i]!=c[j]:
                d.append(z[j])
                g.append(z[j])
        
       
        for m in range(1):
            d.append(x[e])
            f.append(d)
            #print(d)
            g.append(y[e])
            f.append(g)
            
            #print(g)
            e+=1


            
    #print(f)
    return f
       
#print(permute(a,b,c))

def per(odds):
    p=[]
    for i in odds:
        p.append(permute(i['all odds'][0],i['all odds'][1],i['all odds'][2],i['match']))
    
    return p
