import csv              # importing of modules
import os
from time import sleep as z
import pandas as p 


def viewI():                                       # Definition of 
    file.seek(0)                                   # six functions
    id = input('Enter the id : ')
    print()
    for rec in r:
        if rec[0]==id:
            print('The record is as follows :')
            print('ID -',id,'\nName -',rec[1],'\nHeight -',rec[2]+' cm',\
                  '\nWeight -',rec[3]+' kg','\nBMI -',rec[4],\
                  '\nWeight Category -',rec[5],'\nregion -',rec[6]+' Delhi')                                       
            break
    else:
        print('Nothing got matching to this id !!!')

def viewN():
    file.seek(0)
    n = input('Enter your name :').capitalize()
    c = 1
    print('\nRecord(s) pertaining to given name is/are as follows :\n')
    for rec in r:
        if rec[1]==n:
            print('No.',str(c),"record by name - '"+n+"' is as under :\n")
            print('ID -',rec[0],'\nName -',rec[1],'\nHeight -',rec[2]+' cm',\
                  '\nWeight -',rec[3]+' kg','\nBMI -',rec[4],\
                  '\nWeight Category -',rec[5],'\nregion -',rec[6]+' Delhi\n')
            c+=1
    if c==1:
        print('###Null###')

def viewAll():
    file.seek(0)
    loc1 = input('Which region in Delhi you want to check \
(Enter - South/North/East/West) :').upper()
    if loc1 not in['SOUTH','NORTH','WEST','EAST']:
        print('You have entered wrong input for the region. Please try again !!!')
        return
    print('\nRecord(s) pertaining to the given region is/are as follows :\n')
    c = 0
    l = [['ID','NAME','HEIGHT','WEIGHT','BMI','WT CAT.','REGION']]
    for rec in r:
        if rec[6]==loc1:
            c+=1
            l+=[rec]
    f = open('viewA.csv','w+',newline = '')
    w = csv.writer(f)
    w.writerows(l)
    f.close()
    r1 = p.read_csv('viewA.csv')
    print(r1)
    print('\nAs shown above, there is/are',c,'records in',loc1,'Delhi.')
    os.remove('viewA.csv')
                 
def add():
    i = input('Enter your id : ')
    for rec in r:
        if rec[0]==i:
            print('\nA record is already placed for that id. Please try again!!')
            break
    else:
        n = input('Enter your name : ')
        h = int(input('Enter your height (cm): '))
        we = int(input('Enter your weight (kg):'))
        bmi = round(we/((h/100)**2),2)
        loc = input('In which region in Delhi do you live in \
(Enter - South/North/East/West)? :').upper()
        if bmi < 18.5:
            ct = 'Underwt.'
        elif bmi >= 18.5 and bmi < 25:
            ct = 'Normal'
        elif bmi >= 25 and bmi < 30:
            ct = 'Overwt.'
        else:
            ct = 'Obese'
        l = [i,n,str(h),str(we),str(bmi),ct,loc]
        file.seek(0,2)
        w.writerow(l)
        file.flush()
        print('YOUR RECORD HAS BEEN ADDED TO THE DATABASE!!')
    
def update():
    id = input('Enter id :')
    l = []
    file.seek(0)
    for i in r:
        l.append(i)
    for j in l:
        if j[0]==id:
            a = int(input('''What do you want to change :
Enter 1 for name / 2 for height / 3 for weight / 4 for bmi / 5 for region :'''))
            if a == 1:
                name1 = input('\nEnter your new name :')
                l[(l.index(j))][a] = name1
            elif a == 2:
                he = float(input('\nEnter your new height in cm :'))
                l[(l.index(j))][2] = str(he)
                he = he/100
                we = float(l[(l.index(j))][3])
                bmi = round(we/(he**2),2)
                if bmi < 18.5:
                    ct = 'Underwt.'
                elif bmi >= 18.5 and bmi < 25:
                    ct = 'Normal'
                elif bmi >= 25 and bmi < 30:
                    ct = 'Overwt.'
                else:
                    ct = 'Obese'
                l[(l.index(j))][4] = str(bmi)
                l[(l.index(j))][5] = ct
            elif a == 3:
                we = float(input('\nEnter your new weight in kg :'))
                he = float(l[(l.index(j))][2])
                he = he/100                
                bmi = round(we/(he**2),2)
                if bmi < 18.5:
                    ct = 'Underwt.'
                elif bmi >= 18.5 and bmi < 25:
                    ct = 'Normal'
                elif bmi >= 25 and bmi < 30:
                    ct = 'Overwt.'
                else:
                    ct = 'Obese'
                l[(l.index(j))][4] = str(bmi)
                l[(l.index(j))][3] = str(we)
                l[(l.index(j))][5] = ct
                
            elif a == 4:
                we = float(input('\nEnter your new weight in kg :'))
                he = float(input('Enter your new height in cm :'))
                l[(l.index(j))][2] = str(he)
                he = he/100
                bmi = round(we/(he**2),2)
                if bmi < 18.5:
                    ct = 'Underwt.'
                elif bmi >= 18.5 and bmi < 25:
                    ct = 'Normal'
                elif bmi >= 25 and bmi < 30:
                    ct = 'Overwt.'
                else:
                    ct = 'Obese'
                l[(l.index(j))][a] = str(bmi)
                l[(l.index(j))][3] = str(we)
                l[(l.index(j))][5] = ct
            elif a == 5:
                loc = input('In which region in Delhi do you live in \
(Enter South/North/East/West)? :').upper()
                l[(l.index(j))][a+1] = loc
            print()
            print('Updated record is as follows :')                            
            print('Id -',l[l.index(j)][0],'\nName -',l[l.index(j)][1],\
                  '\nHeight -',l[l.index(j)][2]+' cm',\
                  '\nWeight -',l[l.index(j)][3]+' kg',\
                  '\nBMI -',l[l.index(j)][4],\
                  '\nWeight Category -',l[l.index(j)][5],\
                  '\nRegion -',l[l.index(j)][6])
            break
    if j[0]!=id:
        print('\nRecord for this id is not present in the database!!! TRY AGAIN.')
    file.close()
    f1 = open('h.csv','w+',newline = '')                 # use of os module
    w1 = csv.writer(f1)                                  # to update csv file
    r1 = csv.reader(f1)
    w1.writerows(l)
    f1.close()
    os.remove('health.csv')
    os.rename('h.csv','health.csv')
    
def end():
    print('\n                     Chosen function ended !!!')
    input('                     Press enter to continue :')
    print('\n'*20)   

print('''       ~~Welcome to the HEALTH DATABASE SYSTEM with COVID-RISK CHECK~~
                      - DEVESH RAICHANDANI    XII - B
                          **ADARSH PUBLIC SCHOOL**
                          
                              ___OBJECTIVE___ :
                    
        Health Database System keeps your health related parameters safe,
        secure and easily accessible in a python automated CSV database.
            You can also use corona risk-check for self-assessment.''')
a = True
spacer=1
while a == True:
    
    print('''
                       FUNCTION DESCRIPTION       CODE NUMBER
                    
                      View your record by id           1
                          
                     View your record by name          2
                         
                    View all records in an area        3
                        
                        Update your record             4
                            
                         Add a new record              5
                             
                        Corona Risk-Check              6
                            
                     Exit the database program         7 '''
          )   # Menu and Description

                                       
    file = open('health.csv','r+',newline = '')
    w = csv.writer(file)
    r = csv.reader(file)
    if spacer == 2:
        print('\n'*12)
    spacer=2
    code = input('\nEnter code number for applying corresponding function : ')
    print()
    if code == '1':
        print('---Viewing a Record by ID---\n')
        viewI()
        end()
    elif code == '2':
        print('---Viewing a Record by name---\n')
        viewN()
        end()
    elif code == '3':
        print('---Viewing all records in an area---\n')
        viewAll()
        end()
    elif code == '4':
        print('---Updating a Record---\n')
        update()
        end()
    elif code == '5':
        print('---Adding a Record---\n')
        add()
        end()
    elif code == '6':
        print('---Covid-19 Risk Check---\n')
        count = 0
        print('''          The information provided by you will be used for monitoring
               and management of the current health crisis and
                   research in the fight against covid-19.\n''')
        p = input('''Are you experiencing any of the following :
1. cough
2. fever
3. difficulty in breathing
4. loss of senses of smell and taste
Enter y for yes OR any letter for no : ''')
        q = input('''\nHave you ever had :
1. Diabetes
2. Hypertension
3. Lung disease
4. Kidney Disorder
Enter y for yes OR any letter for no : ''')
        r = input('''\nHave you travelled internationally in the last 28-45 days?
Enter y for yes OR any letter for no : ''')
        s = input('''\nHave you recently been in contact with \
a person who has tested positive for covid-19 ?
Enter y for yes OR any letter for no : ''')
        print()

        if p == 'y' or p =='Y':
            count += 1
        if q == 'y' or q == 'Y':
            count += 1
        if r == 'y' or r == 'Y':
            count += 1
        if s == 'y' or s == 'Y':
            count +=1
        if count == 0:
            print('You are safe!! Be at home and maintain \
a safe distance from anyone\nwho is sneezing or coughing.')
        if count == 1:
            print('You have mild risk of developing covid-19. \
Be at home for a few\ndays and if you feel sick, visit \
nearby healthcare professional.')
        if count == 2:
            print('Moderate risk of covid-19. Visit or call a\
medical professional if feeling sick.')
        if count == 3 or count == 4:
            print('You are at a high risk of covid-19. \
Visit or call a\nmedical professional at your earliest convenience.')
        end()    
    elif code == '7':
        a = False
        print('Thanks for accessing Health Database with Covid-19 \
Risk Check!!!\n\t\t\t     -*-*-*-')
        z(2)
    else:
        print('You have mistakenly entered a wrong code. Please try again!!!')
        z(2)
        






