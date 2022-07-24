
#v=[[{'match': 'Crystal Palace - Arsenal', 'odds': ['3.5', '2.08', '3.6']}, {'match': 'Fulham - Liverpool', 'odds': ['9.4', '1.32', '5.6']}, {'match': 'Leeds - Wolves', 'odds': ['2.27', '3.25', '3.4']}, {'match': 'Bournemouth - Aston Villa', 'odds': ['3.3', '2.22', '3.45']}, {'match': 'Tottenham - Southampton', 'odds': ['1.38', '7.8', '5.2']}, {'match': 'Newcastle - Nottingham Forest', 'odds': ['1.67', '5', '3.7']}, {'match': 'Everton - Chelsea', 'odds': ['5', '1.68', '4']}, {'match': 'Manchester United - Brighton', 'odds': ['1.53', '6.3', '4.35']}, {'match': 'Leicester - Brentford', 'odds': ['2', '3.6', '3.75']}, {'match': 'West Ham - Manchester City', 'odds': ['8.1', '1.37', '5.25']}, {'match': 'Aston Villa - Everton', 'odds': ['2.06', '3.5', '3.2']}, {'match': 'Wolves - Fulham', 'odds': ['2.14', '3.35', '3.2']}, {'match': 'Manchester City - Bournemouth', 'odds': ['1.1', '21', '7.9']}, {'match': 'Brighton - Newcastle', 'odds': ['2.35', '2.98', '3.15']}, {'match': 'Southampton - Leeds', 'odds': ['2.2', '3.1', '3.25']}, {'match': 'Arsenal - Leicester', 'odds': ['1.62', '4.9', '3.85']}, {'match': 'Brentford - Manchester United', 'odds': ['3.4', '2.1', '3.25']}, {'match': 'Nottingham Forest - West Ham', 'odds': ['3.15', '2.18', '3.25']}, {'match': 'Chelsea - Tottenham', 'odds': ['2.12', '3.35', '3.25']}, {'match': 'Liverpool - Crystal Palace', 'odds': ['1.19', '12.25', '6']}], [{'match': 'Crystal Palace - Arsenal', 'odds': [3.55, 2.1, 3.6]}, {'match': 'Fulham - Liverpool', 'odds': [9.2, 1.34, 5.5]}, {'match': 'Bournemouth - Aston Villa', 'odds': [3.3, 2.25, 3.45]}, {'match': 'Leeds - Wolves', 'odds': [2.3, 3.25, 3.4]}, {'match': 'Newcastle - Nottingham Forest', 'odds': [1.7, 5.25, 3.85]}, {'match': 'Tottenham - Southampton', 'odds': [1.4, 7.7, 5.25]}, {'match': 'Everton - Chelsea', 'odds': [5.0, 1.7, 4.0]}, {'match': 'Leicester - Brentford', 'odds': [2.05, 3.6, 3.75]}, {'match': 'Manchester United - Brighton', 'odds': [1.55, 6.2, 4.25]}, {'match': 'West Ham - Manchester City', 'odds': [8.0, 1.4, 5.25]}, {'match': 'Aston Villa - Everton', 'odds': [2.1, 3.7, 3.4]}, {'match': 'Arsenal - Leicester', 'odds': [1.65, 5.25, 4.25]}, {'match': 'Brighton - Newcastle', 'odds': [2.4, 3.15, 3.3]}, {'match': 'Manchester City - Bournemouth', 'odds': [1.11, 25.0, 9.2]}, {'match': 'Southampton - Leeds', 'odds': [2.25, 3.3, 3.45]}, {'match': 'Wolves - Fulham', 'odds': [2.2, 3.55, 3.35]}, {'match': 'Brentford - Manchester United', 'odds': [3.6, 2.15, 3.45]}, {'match': 'Nottingham Forest - West Ham', 'odds': [3.35, 2.25, 3.45]}, {'match': 'Chelsea - Tottenham', 'odds': [2.15, 3.55, 3.45]}, {'match': 'Liverpool - Crystal Palace', 'odds': [1.25, 13.0, 6.2]}], [{'match': 'Crystal Palace - Arsenal', 'odds': [3.65, 2.15, 3.55]}, {'match': 'Fulham - Liverpool', 'odds': [9.8, 1.33, 6.0]}, {'match': 'Tottenham - Southampton', 'odds': [1.42, 8.0, 5.2]}, {'match': 'Newcastle - Nottingham Forest', 'odds': [1.68, 5.6, 4.0]}, {'match': 'Bournemouth - Aston Villa', 'odds': [3.4, 2.27, 3.55]}, {'match': 'Leeds - Wolves', 'odds': [2.33, 3.3, 3.45]}, {'match': 'Everton - Chelsea', 'odds': [5.0, 1.76, 3.95]}, {'match': 'Leicester - Brentford', 'odds': [2.07, 3.7, 3.75]}, {'match': 'Manchester United - Brighton', 'odds': [1.58, 6.4, 4.3]}, {'match': 'West Ham - Manchester City', 'odds': [8.6, 1.39, 5.4]}, {'match': 'Aston Villa - Everton', 'odds': [2.08, 3.85, 3.55]}, {'match': 'Arsenal - Leicester', 'odds': [1.65, 5.4, 4.3]}, {'match': 'Brighton - Newcastle', 'odds': [2.45, 3.15, 3.35]}, {'match': 'Southampton - Leeds', 'odds': [2.22, 3.5, 3.5]}, {'match': 'Manchester City - Bournemouth', 'odds': [1.13, 28.0, 10.0]}, {'match': 'Wolves - Fulham', 'odds': [2.14, 3.8, 3.45]}, {'match': 'Brentford - Manchester United', 'odds': [3.8, 2.12, 3.5]}, {'match': 'Nottingham Forest - West Ham', 'odds': [3.55, 2.2, 3.55]}, {'match': 'Chelsea - Tottenham', 'odds': [2.13, 3.75, 3.55]}, {'match': 'Liverpool - Crystal Palace', 'odds': [1.25, 14.0, 6.8]}]]
#arrang all the odds for a particular match. output to per(), input from games()

def match(v):
    
    a=[]
    for i in v[0]:
        
        for j in v[1]:
            for k in v[2]:
                if i['match']== j['match'] and k['match']== j['match']:
                #if i[0]== j[0] and k[0]== j[0]:
                    a.append({'match':i['match'],'all odds':[i['odds'],j['odds'],k['odds']]})
                    
    #print(a)
    return a
                
            
#match(v)

