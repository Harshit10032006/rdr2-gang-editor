import pandas as pdd 
import numpy as np



names = [
    'Dutch','Arthur','Hosea','Micah','John','Bill','Javier','Charles','Lenny','Sean',
    'Sadie','Uncle','Tilly','Mary-Beth','Karen','Molly','Pearson','Susan','Jack','Kieran'
]

roles = [
    'Leader','Right-Hand Man','Strategist','Enforcer','Outlaw','Gunman','Gunman','Tracker',
    'Gunman','Gunman','Shooter','Camper ','Cook Helper','Woman','Women','Women',
    'Quartermaster','Camp Manager','Child','Scout'
]


ages = [
    44, 36, 55, 39, 27, 40, 35, 32, 19, 28,
    28, 60, 25, 22, 23, 30, 45, 50, 12, 21]

Bounties = [
    280, 798, 323, 345, 150, 200, 180, 220, 289, 210,
    120, 50, 90, 80, 75, 100, 190, 250, 10, 70]


Threat_levels = [
    'Extreme','Very Low','Medium','Low','Medium','High','Medium','High','Very Low','Low',
    'Medium','Very Low','Low','Low','Low','Medium','High','Extreme','Very Low','Medium']

Status = [
    'Alive','Alive','Dead','Alive','Alive','Alive','Alive','Alive','Dead','Alive',
    'Alive','Dead','Alive','Alive','Alive','Alive','Alive','Alive','Alive','Alive']


Locations = [
    'Saint Denis','BlackWater','Saint Denis','Saint Denis','Valentine','Valentine','Rhodes','Rhodes','Saint Denis','Saint Denis',
    'Annesburg','Saint Denis','Valentine','Rhodes','Rhodes','Valentine','Saint Denis','Saint Denis','Saint Denis','Annesburg']


try:
     RDR=pdd.read_csv("RDR.csv")
except FileNotFoundError:
     RDR = pdd.DataFrame({
    'Name': names,
    'Age': ages,
    'Role': roles,
    'Bounty$$': Bounties,
    'Threat Level': Threat_levels,
    'Status': Status,
    'Last Seen': Locations})

def reduce_bounty(Name, amount):
    if Name in RDR['Name'].values :
        
        curr = RDR.loc[RDR['Name']==Name,"Bounty$$"].values[0]
        if curr < amount:
            RDR.loc[RDR['Name']==Name,"Bounty$$"]=curr-amount
            print(f"New Bounty is of {Name} is  :->{curr-amount} ")
        else :
             RDR.loc[RDR['Name']==Name,"Bounty$$"]=0
             print("Now Bounty is 0 Thanku!!" )
    else :
        print(f"No Gang Members Named ->{Name} in This Gang maybe in  another Gang")



def update_bounty(Name,new_amt):
    if Name in RDR['Name'].values:
        temp= RDR.loc[RDR['Name']==Name,"Bounty$$"].values[0]
        RDR.loc[RDR['Name']==Name,"Bounty$$"]=new_amt
        if temp  > new_amt:
            print(" WARNING !! bounty Updated but its Less Than Before")
        else :
            print("Bounty Successfully Increased")
    else :
        print(f"No One Name ->{Name} is this Gang")

def change_reqirement(value) :
    RDR["Required"]=np.where(RDR["Bounty$$"] > value,"Dead or Alive", "Alive")
    print(" !!!!!!Amount Changes Succssfully !!!!!!!")


def add_members(Name , ages,roles , Bounty ,Threat_levels,Locations,Status ):
    new_mem = pdd.DataFrame({'Name': [Name],
    'Age': [ages],
    'Role': [roles],
    'Bounty$$': [Bounty],
    'Threat Level': [Threat_levels],
    'Status': [Status],
    'Last Seen': [Locations]})
    global RDR
    if roles !="Leader" :
         RDR = pdd.concat([RDR ,new_mem])
         print("New Member added : ")
    else :
         print("Error Old Leader  is Alive Right now ")
    RDR.to_csv("RDR.csv")


def remove_members(Name , Status):
    global RDR
    if Status == "Leader":
            if Name in RDR["Name"].values:
               RDR = RDR.drop(RDR[RDR['Name']==Name].index)
               print("Leader Removed New Leader Missing !!!!")
            else :
                 print(f"No member Named {Name} in Gang ")

    else :
        if Name in RDR["Name"].values:
               RDR = RDR.drop(RDR[RDR['Name']==Name].index)
               print("Member Removed  !!!!")
        else :
                print(f"No member Named {Name} in Gang ")

    RDR.to_csv("RDR.csv")
        
     
     

while True:
    choose = input("Type the Choice \n 1 ) FOR Reduce Bounty   \n 2 ) For Update Bounty  \n 3 ) Change requirement for Dead / Dead or Alive   \n4) For Exit   \n 5) For Display changes   \n 6 ) Adding New Members  \n 7) Remove Members \n Choice -> " )

    
    if choose == "1" :
           
           n=input("Type Name of the Member : ")
           v= int(input("Type the amount : "))
           reduce_bounty(n,v)
    elif  choose == "2":
           
           n=input("Type Name of the Member : ")
           v= int(input("Type the new amount : "))
           update_bounty(n,v)
    elif choose == "3" :
           
            v= int(input("Type the  max amount  for Dead or Alive : "))
            change_reqirement(v)
            
    elif choose == "4" :
            print(f"{"!"*10} System Closed {"!"*10}")
            break

    elif choose == "5" :
        print(RDR)
    
    elif choose == "6":
         name=input("Type the New member Name : ")
         age=int(input("Type the age of the New member : " ))
         rolesi = input("Type the role of the New Member : ")
         Bounty = int(input("Type the Bounty of the New Member : "))
         Threat_levels = input("Type the threat_level : ")
         
         Locations = input("Type the  last seen location : ")
         add_members(name , age , rolesi , Bounty , Threat_levels,Locations,Status='Alive')
    
    elif choose == "7":
         n=input("Name of the Member :")
         v=input("Role of the Member ")
         remove_members(n,v)
         


                   
    else :
        print("No option Found Try again")
        
                  
                             
