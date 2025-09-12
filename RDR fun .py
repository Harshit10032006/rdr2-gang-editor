import pandas as pd 
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
    28, 60, 25, 22, 23, 30, 45, 50, 12, 21
]

Bounties = [
    280, 798, 323, 345, 150, 200, 180, 220, 289, 210,
    120, 50, 90, 80, 75, 100, 190, 250, 10, 70
]

# Threat based on their Bounties
Threat_levels = [
    'Extreme','Very Low','Medium','Low','Medium','High','Medium','High','Very Low','Low',
    'Medium','Very Low','Low','Low','Low','Medium','High','Extreme','Very Low','Medium'
]
# Alive or Dead
Status = [
    'Alive','Alive','Dead','Alive','Alive','Alive','Alive','Alive','Dead','Alive',
    'Alive','Dead','Alive','Alive','Alive','Alive','Alive','Alive','Alive','Alive'
]

# Last Seen Location
Locations = [
    'Saint Denis','BlackWater','Saint Denis','Saint Denis','Valentine','Valentine','Rhodes','Rhodes','Saint Denis','Saint Denis',
    'Annesburg','Saint Denis','Valentine','Rhodes','Rhodes','Valentine','Saint Denis','Saint Denis','Saint Denis','Annesburg'
]


RDR = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'Role': roles,
    'Bounty$$': Bounties,
    'Threat Level': Threat_levels,
    'Status': Status,
    'Last Seen': Locations
})

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

while True:
    choose = input("Type the Choice \n 1 ) FOR Reduce Bounty \n 2 ) For Update Bounty \n 3 ) Change requirement for Dead / Dead or Alive \n4) For Exit  \n 5) For Display changes " )

    
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
            break

    elif choose == "5" :
        print(RDR)
                   
    else :
        print("No option Found Try again")
    ## ok
        
                  
                             
