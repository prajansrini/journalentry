#__JOURNAL ENTRY AND TRIAL BALANCE__
import subprocess
import sys

def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
install()

import csv
import os
from tabulate import tabulate
import datetime

#__Functions__
def createfolder(fold):
    cwd=os.getcwd()
    folddir=cwd+"\\"+fold
    os.mkdir(folddir)
    os.chdir(folddir)
    directory=folddir
    return directory

def folfilecheck(cwd,foldche,modfolder):
    modfoldche=foldche.lower()
    if modfoldche in modfolder:
        foldcwd=cwd+"\\"+foldche
        file=os.listdir(foldcwd)
        modfile=[]
        print("The list of Files in the Folder,","'",foldche,"'","is: ")

        for j in file:
            if os.path.isfile(foldcwd+"\\"+j):
                print(j)
                modfile.append(j.lower())
            else:
                pass
        print()
        fileche=input("Enter the file name: ")

        if ".csv" not in fileche.lower():
            fileche=fileche+".csv"
        else:
            pass
        
        if fileche.lower() in modfile:
            filecwd=foldcwd+"\\"+fileche
            return filecwd,fileche
        else:
            print("The File,","'",fileche,"'","doesnt exist in the Folder","'",foldche,"'")
            return None,None
    else:
        print("The Folder,","'",foldche,"'","doesnt exist in the Directory")
        return None,None

def date(inputdate):
    print()
    if "-" in inputdate and inputdate.count('-')==2:
        date,month,year = inputdate.split('-')
    elif "/" in inputdate and inputdate.count('/')==2:
        date,month,year = inputdate.split('/')
    elif "\\" in inputdate and inputdate.count('\\')==2:
        date,month,year = inputdate.split('\\')
    elif "." in inputdate and inputdate.count('.')==2:
        date,month,year = inputdate.split('.')
    else:
        date=month=year=False

    try:
        datein=int(date)
        monthin=int(month)
        yearin=int(year)
        datetime.datetime(yearin,monthin,datein)
        monthdict={1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr",
                   5:"May",6:"Jun",7:"Jul", 8:"Aug",
                   9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
        inputdate=date+"-"+monthdict[monthin]+"-"+year
        dinp=False
        return dinp,inputdate
        
    except ValueError:
        print("Invalid date... Please follow the date format(dd/mm/yyyy)")
        dinp=True
        return dinp,None
    
def debit(writeobj,debcount,totdeb,datecnt):
        debcount+=1
        print()
        debtacc=input("Enter the Debit Account "+str(debcount)+" (Name) : ")
        lowdebtacc=debtacc.lower()
        if "a/c" not in lowdebtacc or "a\c" not in lowdebtacc:
            debtacc=debtacc+" A/c"

        debc=True
        while debc==True:
            try:
                debtcash=float(input("Enter the Debit Cash of Debit Account "+str(debcount)+" (numerical value only): "))
            except ValueError:
                print()
                print("Invalid cash amount...")
                debtcash=None
                debc=True

            if type(debtcash)==float:
                if debtcash<0:
                    print()
                    print("Invalid cash amount...")
                    debc=True
                elif debtcash>=0:
                    debc=False

        totdeb+=debtcash
        moddebcash="Rs. "+str(debtcash)

        if datecnt==0:
            record=[inputdate,debtacc,moddebcash," "]
            datecnt+=1
            return record,totdeb,debcount,datecnt
        else:
            record=[" ",debtacc,moddebcash," "]
            datecnt+=1
            return record,totdeb,debcount,datecnt

def crecashcheck(crecount):
    try:
        credcash=float(input("Enter the Credit Cash of Credit Account "+str(crecount)+" (numerical value only): "))
    except ValueError:
        print()
        print("Invalid cash amount...")
        return True,None

    if type(credcash)==float:
        if credcash<0:
            print()
            print("Invalid cash amount...")
            return True,None
        elif credcash>=0:
            return False,credcash

def narration(trancnt):
    print()
    nar=input("Enter the Narration Line of the Transaction "+str(trancnt)+" : ")
    if "being" not in nar.lower():
        nar="Being "+nar

    if nar[0]!="(" and nar[-1]!=")":
        nar="("+nar+")"
    return nar

def disptable(table,nar):
    minmodtable=""
    modtable=""
    bascnt=0

    lowcnt=table.find("╘")
    higcnt=table.find("╛")
    baslen=higcnt-lowcnt+1
    a=False

    for j in table:
        if j=="├":
            minmodtable+="│"
            a=True
        elif a==True:
            if j=="┼":
                minmodtable+="├"
                a=False
            else:
                j=" "
                minmodtable+=j
        else:
            minmodtable+=j

    for i in minmodtable:
        if i=="╧":
            i="┴"
            modtable+=i
        if i=="╛":
            i="┘"
            modtable+=i
        if i=="╘":
            i="├"
            modtable+=i
            bascnt+=1
        if i=="╛":
            i="┘"
            modtable+=i
        if bascnt>0:
            if i=="═":
                i="─"
                modtable+=i
        else:
            modtable+=i
            
    tot=len(modtable)
    if len(nar)+2>baslen:
        nar=" "+nar+" "
        cover=len(nar)+1-baslen
        modtable=modtable[:tot-1]+"┴"
        modtable=modtable+cover*"─"+"┐"

        nar="│"+nar+"│"

        base="╘"
        for i in range(len(nar)-2):
            base+="═"
        base+="╛"

        restable=modtable+"\n"+nar+"\n"+base
        tottable=""
        for u in restable:
            if u=='█':
                tottable+=" "
            else:
                tottable+=u
        print(tottable)
        
    if len(nar)+2<baslen:
        modtable=modtable[:tot-1]+"┤"

        rem=baslen-len(nar)-1
        rrem=rem//2
        lrem=rem-rrem-1
        nar="│"+" "*lrem+nar+" "*rrem+"│"

        base="╘"
        for i in range(baslen-2):
            base+="═"
        base+="╛"

        restable=modtable+"\n"+nar+"\n"+base
        tottable=""
        for u in restable:
            if u=='█':
                tottable+=" "
            else:
                tottable+=u
        print(tottable)
        
    if len(nar)+2==baslen:
        modtable=modtable[:tot-1]+"┤"

        nar="│"+nar
        rem=baslen-len(nar)-1
        nar=nar+" "*rem+"│"

        base="╘"
        for i in range(baslen-2):
            base+="═"
        base+="╛"

        restable=modtable+"\n"+nar+"\n"+base
        tottable=""
        for u in restable:
            if u=='█':
                tottable+=" "
            else:
                tottable+=u
        print(tottable)

def trialbal(slno):
    par=input("Enter the Ledger Account "+str(slno)+" (Name) : ")
    parlow=par.lower()

    if "a/c" not in parlow or "a\c" not in parlow:
        par+=" A/c"                        

    ent1="y"
    while ent1=="y":
        print()
        print("Is '",par,"' a Debit Account or Credit Account")
        ali=input("Enter 'd' for Debit account or Enter 'c' for Credit account: ")
        ali=ali.lower()
        if ali not in ["d","c"]:
            print("Invalid input")
            ent1="y"
        else:
            ent1="n"

    if ali=="d":
        dcc=True
        while dcc==True:
            print()
            try:
                dcash=float(input("Enter the Debit Cash of Debit Account ' "+par+" ' (numerical value only): "))
            except ValueError:
                print()
                print("Invalid cash amount...")
                dcash=None
                dcc=True

            if type(dcash)==float:
                if dcash<0:
                    print()
                    print("Invalid cash amount...")
                    dcc=True
                elif dcash>=0:
                    dcc=False

    elif ali=="c":
        ccc=True
        while ccc==True:
            print()
            try:
                ccash=float(input("Enter the Credit Cash of Credit Account ' "+par+" ' (numerical value only): "))
            except ValueError:
                print()
                print("Invalid cash amount...")
                ccash=None
                ccc=True

            if type(ccash)==float:
                if ccash<0:
                    print()
                    print("Invalid cash amount...")
                    ccc=True
                elif ccash>=0:
                    ccc=False

    if ali=="d":
        dcashmod="Rs. "+str(dcash)
        slno=str(slno)+"."
        drec=[slno,par,dcashmod," "]
        return dcash,None,drec

    elif ali=="c":
        ccashmod="Rs. "+str(ccash)
        slno=str(slno)+"."
        crec=[slno,par," ",ccashmod]
        return None,ccash,crec

def helpjourn():
    print("""JOURNAL ENTRY:
            Journal Entry is a record of every business transactions in accordance to the specific entity and date.
            It follows double entry system of accounting where every transaction is recorded in Credit and Debit section.
            They are not limited to the buying and selling of goods and services, but include any exchange of monetary value,
            such as interest payments, depreciation, expenses, or payroll.""")
    print()
    print("""Principles:
             ->	'Debit the receiver and Credit the giver'.
                For Personal Accounts (consists of all those accounts which are related to a person, business, firm, etc...),
                The rule is debit the account of the person who receives the benefit and
                credit the account of the person who gives the benefit.

             ->	'Debit what comes in and Credit what goes out'.
                For Real Accounts (consists of all those accounts which are related to assets),
                The rule is debit what comes in and credit what goes out.

             ->	'Debit all expenses and losses and Credit all incomes and gains'.
                For Nominal Accounts (consists of all those accounts which are related to expenses, losses, Income and Gains),
                The rule is debit all expenses and losses and credit all incomes and gains.
            """)
    print()
    print("Example:")
    print("Transactions of SUBBU Sports:")
    print("""
            ╒════════════╤══════════════════════════════════════════════════════╕
            │ Date       │ Transaction                                          │
            ╞════════════╪══════════════════════════════════════════════════════╡
            │ 4-Aug-2022 │ Football sold to Vishnu for Rs. 830                  │
            ├────────────┼──────────────────────────────────────────────────────┤
            │ 4-Aug-2022 │ Ball and Bat sold to Deep and Deepak for Rs. 1050    │
            ├────────────┼──────────────────────────────────────────────────────┤
            │ 5-Aug-2022 │ Paid Rent for September of Rs. 2000                  │
            ├────────────┼──────────────────────────────────────────────────────┤
            │ 6-Aug-2022 │ Basket Ball sold to Keshav for Rs. 1200              │
            ├────────────┼──────────────────────────────────────────────────────┤
            │ 6-Aug-2022 │ Goods Purchased from Peter Sports of worth Rs. 96000 │
            ├────────────┼──────────────────────────────────────────────────────┤
            │ 7-Aug-2022 │ Paid Salaries of Rs. 12000                           │
            ╘════════════╧══════════════════════════════════════════════════════╛
          """)
    print()
    print("Journal Entry: ")
    print("""
            Transaction 1 :
            ╒════════════╤════════════════════╤═══════════╤═══════════╕
            │ Date       │ Particulars        │ Debit     │ Credit    │
            ╞════════════╪════════════════════╪═══════════╪═══════════╡
            │ 4-Aug-2022 │ Cash A/c           │ Rs. 830.0 │           │
            │            ├────────────────────┼───────────┼───────────┤
            │            │      To Vishnu A/c │           │ Rs. 830.0 │
            ├────────────┴────────────────────┴───────────┴───────────┤
            │                  (Being Sold Football)                  │
            ╘═════════════════════════════════════════════════════════╛

            Transaction 2 :
            ╒════════════╤════════════════════╤════════════╤════════════╕
            │ Date       │ Particulars        │ Debit      │ Credit     │
            ╞════════════╪════════════════════╪════════════╪════════════╡
            │ 4-Aug-2022 │ Cash A/c           │ Rs. 1050.0 │            │
            │            ├────────────────────┼────────────┼────────────┤
            │            │      To Deep A/c   │            │ Rs. 1000.0 │
            │            ├────────────────────┼────────────┼────────────┤
            │            │      To Deepak A/c │            │ Rs. 50.0   │
            ├────────────┴────────────────────┴────────────┴────────────┤
            │             (Being sold Cricket Bat and Ball)             │
            ╘═══════════════════════════════════════════════════════════╛

            Transaction 3 :
            ╒════════════╤══════════════════╤════════════╤════════════╕
            │ Date       │ Particulars      │ Debit      │ Credit     │
            ╞════════════╪══════════════════╪════════════╪════════════╡
            │ 5-Aug-2022 │ Rent A/c         │ Rs. 2000.0 │            │
            │            ├──────────────────┼────────────┼────────────┤
            │            │      To Cash A/c │            │ Rs. 2000.0 │
            ├────────────┴──────────────────┴────────────┴────────────┤
            │              (Being paid rent for Sept)                 │
            ╘═════════════════════════════════════════════════════════╛

            Transaction 4 :
            ╒════════════╤════════════════════╤════════════╤════════════╕
            │ Date       │ Particulars        │ Debit      │ Credit     │
            ╞════════════╪════════════════════╪════════════╪════════════╡
            │ 6-Aug-2022 │ Cash A/c           │ Rs. 1200.0 │            │
            │            ├────────────────────┼────────────┼────────────┤
            │            │      To Keshav A/c │            │ Rs. 1200.0 │
            ├────────────┴────────────────────┴────────────┴────────────┤
            │                 (Being sold Basket Ball)                  │
            ╘═══════════════════════════════════════════════════════════╛

            Transaction 5 :
            ╒════════════╤══════════════════╤═════════════╤═════════════╕
            │ Date       │ Particulars      │ Debit       │ Credi       │
            ╞════════════╪══════════════════╪═════════════╪═════════════╡
            │ 6-Aug-2022 │ Peter Sports A/c │ Rs. 96000.0 │             │
            │            ├──────────────────┼─────────────┼─────────────┤
            │            │      To Cash A/c │             │ Rs. 96000.0 │
            ├────────────┴──────────────────┴─────────────┴─────────────┤
            │           (Being Purchased Goods for wholesale)           │
            ╘═══════════════════════════════════════════════════════════╛

            Transaction 6 :
            ╒════════════╤══════════════════╤═════════════╤═════════════╕
            │ Date       │ Particulars      │ Debit       │ Credit      │
            ╞════════════╪══════════════════╪═════════════╪═════════════╡
            │ 7-Aug-2022 │ Salary A/c       │ Rs. 12000.0 │             │
            │            ├──────────────────┼─────────────┼─────────────┤
            │            │      To Cash A/c │             │ Rs. 12000.0 │
            ├────────────┴──────────────────┴─────────────┴─────────────┤
            │                    (Being Salary Paid)                    │
            ╘═══════════════════════════════════════════════════════════╛
          """)

def helptrial():
    print("""TRIAL BALANCE:
             A trial balance is a bookkeeping worksheet in which the balances of all ledgers are compiled into debit
             and credit account such that column totals of each becomes equal.
             A company prepares a trial balance periodically, usually at the end of every financial year.""")
    print()
    print("""Key Notes:
             -> A trial balance is a worksheet with two columns, one for debits and one for credits,
                that ensures a company’s bookkeeping is mathematically correct.
                
             -> The debits and credits include all business transactions for a company over a certain period
                (usually financial year), including the sum of accounts such as assets, expenses,
                liabilities, and revenues.
                
             -> Debits and credits of a trial balance must tally to ensure that there are no mathematical errors,but
                there could still be mistakes or errors in the accounting systems, which are balanced by
                Suspense Account.
                
             -> If the Suspense account is present in the Credit column then it is considered to be a LIABILITY
                If the Suspense account is present in the Debit column then it is considered to be an ASSET""")
    print()
    print("Example:")
    print("Balance Information of CAPS STATIONERY as on 02-Mar-22")
    print("""                       
            ╒══════════════════╤══════════════╕ ╒══════════════════════╤══════════════╕
            │ Particulars      │ Amount       │ │  Particulars         │ Amount       │
            ╞══════════════════╪══════════════╡ ╞══════════════════════╪══════════════╡
            │ Capital          │ Rs. 250000.0 │ │ Purchases            │ Rs. 150000.0 │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Private Equity   │ Rs. 10000.0  │ │ Insurance            │ Rs. 2000.0   │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Bills Receivable │ Rs. 30000.0  │ │ Stock                │ Rs. 20000.0  │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Building Rent    │ Rs. 50000.0  │ │ Employee Salary      │ Rs. 200000.0 │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Furniture        │ Rs. 20000.0  │ │ Building Maintenance │ Rs. 10000.0  │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Phone Charges    │ Rs. 2000.0   │ │ Electricity Bill     │ Rs. 15000.0  │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ General Reserve  │ Rs. 10000.0  │ │ Insurance            │ Rs. 8000.0   │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Bills Payable    │ Rs. 35000.0  │ │ Miscellaneous        │ Rs. 3000.0   │
            ├──────────────────┼──────────────┤ ├──────────────────────┼──────────────┤
            │ Sales            │ Rs. 240000.0 │ │ Taxes                │ Rs. 25000.0  │
            ╘══════════════════╧══════════════╛ ╘══════════════════════╧══════════════╛
          """)
    print()
    print("Trial Balance: ")
    print("""
            CAPS STATIONERY
            Trial Balance as on 02-Mar-22
            ╒══════════╤══════════════════════════╤══════════════╤══════════════╕
            │ Sl.no.   │ Particulars              │ Debit        │ Credit       │
            ╞══════════╪══════════════════════════╪══════════════╪══════════════╡
            │ 1.       │ Capital A/c              │              │ Rs. 250000.0 │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 2.       │ Private Equity A/c       │              │ Rs. 10000.0  │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 3.       │ Bills Receivable A/c     │ Rs. 30000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 4.       │ Building Rent A/c        │ Rs. 50000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 5.       │ Furniture A/c            │ Rs. 20000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 6.       │ Phone Charges A/c        │ Rs. 2000.0   │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 7.       │ General Reserve A/c      │              │ Rs. 10000.0  │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 8.       │ Bills Payable A/c        │              │ Rs. 35000.0  │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 9.       │ Sales A/c                │              │ Rs. 240000.0 │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 10.      │ Purchases A/c            │ Rs. 150000.0 │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 11.      │ Insurance A/c            │ Rs. 2000.0   │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 12.      │ Stock A/c                │ Rs. 20000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 13.      │ Employee Salary A/c      │ Rs. 200000.0 │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 14.      │ Building Maintenance A/c │ Rs. 10000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 15.      │ Electricity Bill A/c     │ Rs. 15000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 16.      │ Insurance A/c            │ Rs. 8000.0   │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 17.      │ Agent Commission A/c     │ Rs. 3000.0   │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 18.      │ Taxes A/c                │ Rs. 25000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │ 19.      │ Suspense A/c             │ Rs. 10000.0  │              │
            ├──────────┼──────────────────────────┼──────────────┼──────────────┤
            │          │ Total                    │ Rs. 545000.0 │ Rs. 545000.0 │
            ╘══════════╧══════════════════════════╧══════════════╧══════════════╛
         """)

#__Main__
headmain="y"
while headmain=="y":
    print()
    print("MAIN MENU")
    print("Enter")
    print("1 For JOURNAL ENTRY")
    print("2 For TRIAL BALANCE")
    print("3 To Exit")
    print()
    chmain=input("Enter your choice: ")

    if chmain=='1':        
        main1="y"
        while main1=="y":
            print()
            print("JOURNAL ENTRY")
            print()
            print("JOURNAL ENTRY MAIN MENU")
            print("Enter")
            print("1 To Create a New Journal Entry file in a New Folder")
            print("2 To Create a New Journal Entry file in an Existing Folder") 
            print("3 To Add a Transaction in an Existing Journal Entry file")
            print("4 To Display a Journal Entry file")
            print("5 For Help")
            print("6 To Go Back")

            print()
            ch=input("Enter your choice: ")
            oldcwd=os.getcwd()
            emp="█"

            if ch=='1':
                print()
                print("GREETINGS !!!")
                print()
                enter="y"
                headcnt=0
                c=True
                while enter=="y":
                    while c==True:
                        foldname=input("Enter the Folder Name to be created: ")
                        try:
                            locate=createfolder(foldname)
                            c=False
                        except FileExistsError:
                            print("Error, File already exists. You need to enter a unique name.")
                            print()
                            c=True

                        if c==False:
                            filename=input("Enter the File Name to be created: ")
                            print()
                            print("Your File Directory is :",locate+"\\"+filename+".csv")
                    
                    if c==False:
                        file=open(filename+".csv","a",newline="",encoding='utf-8')
                        writeobj=csv.writer(file)
                        
                        if headcnt==0:
                            writeobj.writerow(["Date","Particulars","Debit","Credit"])
                            headcnt+=1

                        dinp=True
                        while dinp==True:
                            predate=input("Enter the Date of Transaction(dd/mm/yyyy): ")
                            dinp,inputdate=date(predate)
                        print()
                        print("Entering the Debit Account(s)...")
                        debcheck="y"
                        totdeb=0
                        debcount=0
                        datecnt=0
                        while debcheck=="y":
                            ret,totdeb,debcount,datecnt=debit(writeobj,debcount,totdeb,datecnt)
                            writeobj.writerow(ret)
                            print()
                            debcheck=input("Do you want to Enter another Debit Account(y/n): ")
                            debcheck=debcheck.lower()
                        
                        print()
                        print("All Debit Account(s) is/are Entered Successfully...")
                        print()
                        print("Entering the Credit Account(s)...")

                        crecheck=True
                        totcre=0
                        crecount=0
                        trancnt=0
                        while crecheck==True:
                            crecount+=1
                            print()
                            credacc=input("Enter the Credit Account "+str(crecount)+" (Name): ")
                            crelow=credacc.lower()

                            if crelow[:2]!="to":
                                credacc="To "+ credacc
                            if "a/c" not in crelow or "a\c" not in crelow:
                                credacc=credacc+" A/c"
                            credacc="     "+credacc

                            if crecount==1:
                                balance=totdeb
                                modbalance="Rs. "+str(balance)
                                print("The total amount to be Balanced is:",modbalance)

                            cash=True
                            while cash==True and balance!=0:
                                crec=True
                                while crec==True:
                                    crec,credcash=crecashcheck(crecount)
                                    
                                modcredcash="Rs. "+str(credcash)
                                totcre+=credcash
                                balance=totdeb-totcre
                                if totcre>totdeb:
                                    balance+=credcash
                                    modbalance="Rs. "+str(balance)
                                    print()
                                    print("The amount to be Balanced is:",modbalance)
                                    print("Invalid!!!, Credit is greater than Balance, Please enter a Valid Input")
                                    totcre-=credcash
                                    cash=True
                                    
                                else:
                                    modbalance="Rs. "+str(balance)
                                    print("The amount to be Balanced is:",modbalance)

                                    record=[" ",credacc," ",modcredcash]
                                    writeobj.writerow(record)

                                    cash=False
                            if balance==0:
                                print("The Total Debit and Total Credit for the Transaction is Balanced")
                                print()
                                print("All Credit Account(s) is/are Entered Successfully...")
                                trancnt+=1
                                nar=narration(trancnt)
                                writeobj.writerow([nar])
                                crecheck=False
                                file.close()
                                
                    print()
                    enter=input("Do you want to Enter another Transaction(y/n): ")
                    enter=enter.lower()
                    if enter=="y":
                        c=False

                else:
                    print()
                    print("All your Transactions are Entered...")
                    print("Thankyou")
                    os.chdir(oldcwd)

                print()
                main1=input("Do you want to go to 'JOURNAL ENTRY MAIN MENU'(y/n): ")
                main1=main1.lower()

            elif ch=='2':
                os.chdir(oldcwd)
                cwd=os.getcwd()
                folder=os.listdir(cwd)
                modfolder=[]
                che="y"
                trancnt=0
                while che=="y":
                    print()
                    print("List of Folders in the Directory is/are: ")
                    for i in folder:
                        if os.path.isdir(cwd+"\\"+i):
                            print(i)
                            modfolder.append(i.lower())
                        else:
                            pass
                    print()
                    foldche=input("Enter the Folder Name: ")
                    modfoldche=foldche.lower()
                    
                    if modfoldche in modfolder:
                        loop=True
                    else:
                        print("The Folder isn't present in the Directory...")
                        loop=False
                        print()
                        che=input("Do you want to Enter the Folder Name again(y/n): ")
                        che=che.lower()

                    headcnt=0
                    while loop==True:
                        loc=oldcwd+"\\"+foldche
                        os.chdir(loc)
                        print()
                        modfilelist=[]
                        filelist=os.listdir(loc)
                        print("The list of Files in the Folder","'",foldche,"'", "is: ")
                        for k in filelist:
                            if os.path.isfile(loc+"\\"+k):
                                print(k)
                                k=k.lower()
                                modfilelist.append(k)
                        print()
                        filename=input("Enter the File Name(unique): ")
                        if ".csv" not in filename:
                            filename+=".csv"
                            
                        if filename.lower() in modfilelist:
                            print("The File","'",filename,"'","is already present in the Folder","'",foldche,"'")
                            print("Please Enter Another Name")
                            loop=True
                        else:
                            loop=False

                        if loop==False:
                            w="y"
                            while w=="y":
                                file=open(filename,"a",newline="",encoding='utf-8')
                                writeobj=csv.writer(file)
                                
                                if headcnt==0:
                                    writeobj.writerow(["Date","Particulars","Debit","Credit"])
                                    headcnt+=1

                                dinp=True
                                while dinp==True:
                                    predate=input("Enter the Date of Transaction(dd/mm/yyyy): ")
                                    dinp,inputdate=date(predate)
                                    
                                print()
                                print("Entering the Debit Account(s)...")
                                debcheck="y"
                                totdeb=0
                                debcount=0
                                datecnt=0
                                while debcheck=="y":
                                    ret,totdeb,debcount,datecnt=debit(writeobj,debcount,totdeb,datecnt)
                                    writeobj.writerow(ret)
                                    print()
                                    debcheck=input("Do you want to Enter another Debit Account(y/n): ")
                                    debcheck=debcheck.lower()
                                
                                print()
                                print("All Debit Account(s) is/are Entered Successfully...")
                                print()
                                print("Entering the Credit Account(s)...")

                                crecheck=True
                                totcre=0
                                crecount=0
                                while crecheck==True:
                                    crecount+=1
                                    print()
                                    credacc=input("Enter the Credit Account "+str(crecount)+" (Name): ")
                                    crelow=credacc.lower()

                                    if crelow[:2]!="to":
                                        credacc="To "+ credacc
                                    if "a/c" not in crelow or "a\c" not in crelow:
                                        credacc=credacc+" A/c"
                                    credacc="     "+credacc

                                    if crecount==1:
                                        balance=totdeb
                                        modbalance="Rs. "+str(balance)
                                        print("The total amount to be Balanced is:",modbalance)

                                    cash=True
                                    while cash==True and balance!=0:
                                        crec=True
                                        while crec==True:
                                            crec,credcash=crecashcheck(crecount)
                                        modcredcash="Rs. "+str(credcash)
                                        totcre+=credcash
                                        balance=totdeb-totcre
                                        if totcre>totdeb:
                                            balance+=credcash
                                            modbalance="Rs. "+str(balance)
                                            print()
                                            print("The amount to be Balanced is:",modbalance)
                                            print("Invalid!!!, Credit is greater than Balance, Please enter a Valid Input")
                                            totcre-=credcash
                                            cash=True
                                            
                                        else:
                                            modbalance="Rs. "+str(balance)
                                            print("The amount to be Balanced is:",modbalance)

                                            record=[" ",credacc," ",modcredcash]
                                            writeobj.writerow(record)

                                            cash=False

                                    if balance==0:
                                        print("The Total Debit and Total Credit for the Transaction is Balanced")
                                        print()
                                        print("All Credit Account(s) is/are Entered Successfully...")
                                        trancnt+=1
                                        nar=narration(trancnt)
                                        writeobj.writerow([nar])
                                        crecheck=False
                                        file.close()

                                print()
                                w=input("Do you want to Enter Another Transaction(y/n): ")
                                w=w.lower()                 
                                if w!="y":
                                    print()
                                    print("All your Transactions are Entered...")
                                    print()
                                    che=input("Do you want Create a Another File in a Existing Folder(y/n): ")
                                    che=che.lower()

                else:
                    print()
                    print("Thankyou")
                    os.chdir(oldcwd)
                    print()
                    main1=input("Do you want to go to 'JOURNAL ENTRY MAIN MENU'(y/n): ")
                    main1=main1.lower()
                    
            elif ch=='3':
                os.chdir(oldcwd)
                cwd=os.getcwd()
                folder=os.listdir(cwd)
                modfolder=[]
                get="y"
                while get=="y":
                    print()
                    print("List of Folders in the Directory is/are: ")
                    for i in folder:
                        if os.path.isdir(cwd+"\\"+i):
                            print(i)
                            modfolder.append(i.lower())
                        else:
                            pass
                    print()
                    foldche=input("Enter the Folder Name: ")
                    directory,fileche=folfilecheck(cwd,foldche,modfolder)

                    if directory==None:
                        pass
                    else:
                        add="y"
                        while add=="y":
                            file=open(directory,"a",newline="",encoding='utf-8')
                            writeobj=csv.writer(file)
                            
                            dinp=True
                            while dinp==True:
                                predate=input("Enter the Date of Transaction(dd/mm/yyyy): ")
                                dinp,inputdate=date(predate)
                            print()
                            print("Entering the Debit Account(s)...")
                            debcheck="y"
                            totdeb=0
                            debcount=0
                            datecnt=0

                            while debcheck=="y":
                                ret,totdeb,debcount,datecnt=debit(writeobj,debcount,totdeb,datecnt)
                                writeobj.writerow(ret)

                                debcheck=input("Do you want to Enter another Debit Account(y/n): ")
                                debcheck=debcheck.lower()
                            
                            print()
                            print("All Debit Account(s) is/are Entered Successfully...")
                            print()
                            print("Entering the Credit Account(s)...")

                            crecheck=True
                            totcre=0
                            trancnt=0
                            crecount=0
                            while crecheck==True:
                                print() 
                                crecount+=1
                                credacc=input("Enter the Credit Account "+str(crecount)+" (Name): ")
                                crelow=credacc.lower()

                                if crelow[:2]!="to":
                                    credacc="To "+ credacc
                                if "a/c" not in crelow or "a\c" not in crelow:
                                    credacc=credacc+" A/c"
                                credacc="     "+credacc

                                if crecount==1:
                                    balance=totdeb
                                    modbalance="Rs. "+str(balance)
                                    print("The total amount to be Balanced is:",modbalance)

                                cash=True
                                while cash==True and balance!=0:
                                    crec=True
                                    while crec==True:
                                        crec,credcash=crecashcheck(crecount)
                                    modcredcash="Rs. "+str(credcash)
                                    totcre+=credcash
                                    balance=totdeb-totcre
                                    if totcre>totdeb:
                                        balance+=credcash
                                        modbalance="Rs. "+str(balance)
                                        print()
                                        print("The amount to be Balanced is:",modbalance)
                                        print("Invalid!!!, Credit is greater than Balance, Please enter a Valid Input")
                                        totcre-=credcash
                                        cash=True
                                        
                                    else:
                                        modbalance="Rs. "+str(balance)
                                        print("The amount to be Balanced is:",modbalance)

                                        record=[" ",credacc," ",modcredcash]
                                        writeobj.writerow(record)

                                        cash=False
                                if balance==0:
                                    print("The Total Debit and Total Credit for the Transaction is Balanced")
                                    print()
                                    print("All Credit Account(s) is/are Entered Successfully...")
                                    trancnt+=1
                                    nar=narration(trancnt)
                                    writeobj.writerow([nar])
                                    crecheck=False
                                    file.close()
                                
                            print()
                            add=input("Do you want to Enter another Transaction(y/n): ")
                            add=add.lower()
                            
                            if add!="y":
                                print()
                                print("All your transactions are entered...")
                                print("Thankyou")
                                get=False
                                os.chdir(oldcwd)

                print()
                main1=input("Do you want to go to 'JOURNAL ENTRY MAIN MENU'(y/n): ")
                main1=main1.lower()

            elif ch=='4':
                os.chdir(oldcwd)
                cwd=os.getcwd()
                folder=os.listdir(cwd)
                modfolder=[]
                get="y"
                while get=="y":
                    print()
                    print("List of Folders in the Directory is/are: ")
                    for i in folder:
                        if os.path.isdir(cwd+"\\"+i):
                            print(i)
                            modfolder.append(i.lower())
                        else:
                            pass
                    print()

                    if len(modfolder)==0:
                        print("The Folder is Empty...")
                        print()
                        break

                    foldche=input("Enter the Folder Name: ")
                    
                    try:
                        directory,fileche=folfilecheck(cwd,foldche,modfolder)
                        print()
                        if directory!=None:
                            print("The Directory of the File is : ")
                            print(directory)
                        if directory==None:
                            pass
                        else:
                            print()
                            print("The Data in the File is: ")
                            file=open(directory,"r",newline='\r\n',encoding='utf-8')
                            readobj=csv.reader(file)
                            data=[]
                            headcnt=True
                            for rec in readobj:
                                if len(rec)>1:
                                    if rec[2]==" ":
                                        rec[1]=emp+rec[1][1:]
                                if headcnt==True:
                                    head=rec
                                    headcnt=False
                                else:
                                    data.append(rec)
                            recs=[]
                            transcnt=0
                            for otp in data:
                                if len(otp)==1:
                                    transcnt+=1
                                    table=tabulate(recs,headers=head,tablefmt="fancy_grid")
                                    print("Transaction ",transcnt," :",sep="")
                                    disptable(table,otp[0])
                                    print()
                                    recs=[]
                                else:
                                    recs.append(otp)
                    except:
                        pass

                    get=input("Do you want to Search Again(y/n): ")
                    get=get.lower()

                else:
                    print("Thankyou")
                    print()
                main1=input("Do you want to go to 'JOURNAL ENTRY MAIN MENU'(y/n): ")
                main1=main1.lower()

            elif ch=='5':
                helpjourn()
                main1=input("Do you want to go to 'TRIAL BALANCE MAIN MENU'(y/n): ")
                main1=main1.lower()

            elif ch=='6':
                print()
                print("Thankyou")
                print()
                break

            elif ch not in ['1','2','3','4','5','6']:
                print()
                print("Enter a valid choice")
                main1=input("Do you want to go to 'JOURNAL ENTRY MAIN MENU'(y/n): ") 
                main1=main1.lower() 
        else:
            print()
            print("Thankyou")
            print()

    elif chmain=='2':
        main2="y"
        while main2=="y":
            print()
            print("TRIAL BALANCE")
            print()
            print("TRIAL BALANCE MAIN MENU")
            print("Enter")
            print("1 To Create a New Trial Balance in a New Folder")
            print("2 To Create a Trial Balance in an Existing Folder") 
            print("3 To Display a Trial Balance")
            print("4 For Help")
            print("5 To Go Back")

            print()
            ch=input("Enter your choice: ")
            oldcwd=os.getcwd()

            if ch=='1':
                print()
                print("GREETINGS !!!")
                print()
                
                headcnt=0
                c=True
                while c==True:
                    foldname=input("Enter the Folder Name to be created: ")
                    try:
                        locate=createfolder(foldname)
                        c=False
                    except FileExistsError:
                        print("Error, File already exists. You need to enter a unique name.")
                        print()
                        c=True

                    if c==False:
                        filename=input("Enter the File Name to be created: ")
                        print()
                        print("Your File Directory is :",locate+"\\"+filename+".csv")
                
                if c==False:
                    print()
                    file=open(filename+".csv","a",newline="",encoding='utf-8')
                    writeobj=csv.writer(file)
                    comp=input("Enter Business Name: ")

                    dinp=True
                    while dinp==True:
                        predate=input("Enter the Date(dd/mm/yyyy): ")
                        dinp,inputdate=date(predate)

                    writeobj.writerow([comp])
                    writeobj.writerow([inputdate])
                    writeobj.writerow(["Sl.no.","Particulars","Debit","Credit"])

                    slno=0
                    ent="y"
                    dtot=0
                    ctot=0
                    while ent=="y":
                        slno+=1
                        print()
                        dcash,ccash,rec=trialbal(slno)
                        if dcash!=None:
                            dtot+=dcash
                        if ccash!=None:
                            ctot+=ccash
                        writeobj.writerow(rec)
                        print()
                        ent=input("Do you want to Enter another Account(y/n): ")
                        ent=ent.lower()
                    bal=ctot-dtot
                    slno+=1

                    if bal>0:
                        balmod="Rs. "+str(bal)
                        slno=str(slno)+"."
                        writeobj.writerow([slno,"Suspense A/c",balmod," "])
                        dtot+=bal
                        print()
                        print("Suspense Account of",balmod,"has been created in Debit Balance (Asset).")

                    if bal<0:
                        bal=abs(bal)
                        balmod="Rs. "+str(bal)
                        slno=str(slno)+"."
                        writeobj.writerow([slno,"Suspense A/c"," ",balmod])
                        ctot+=bal
                        print()
                        print("Suspense Account of",balmod,"has been created in Credit Balance (Liability).")

                    ctotmod="Rs. "+str(ctot)
                    dtotmod="Rs. "+str(dtot)
                    writeobj.writerow([" ","Total",dtotmod,ctotmod])
                    file.close()

                print()
                print("The Trial Balance is Entered...")
                os.chdir(oldcwd)
                print()
                main2=input("Do you want to go to 'TRIAL BALANCE MAIN MENU'(y/n): ")
                main2=main2.lower()

            elif ch=='2':
                os.chdir(oldcwd)
                cwd=os.getcwd()
                folder=os.listdir(cwd)
                modfolder=[]
                che="y"
                trancnt=0
                while che=="y":
                    print()
                    print("List of Folders in the Directory is/are: ")
                    for i in folder:
                        if os.path.isdir(cwd+"\\"+i):
                            print(i)
                            modfolder.append(i.lower())
                        else:
                            pass

                    print()
                    foldche=input("Enter the Folder Name: ")
                    modfoldche=foldche.lower()
                    
                    if modfoldche in modfolder:
                        loop=True
                        che="n"
                        
                    else:
                        print("The Folder isn't present in the Directory...")
                        loop=False
                        print()
                        che=input("Do you want to Enter the Folder Name again(y/n): ")
                        che=che.lower()
                        
                while loop==True:
                    loc=oldcwd+"\\"+foldche
                    os.chdir(loc)
                    print()
                    modfilelist=[]
                    filelist=os.listdir(loc)
                    print("The list of Files in the Folder","'",foldche,"'", "is: ")

                    for k in filelist:
                        if os.path.isfile(loc+"\\"+k):
                            print(k)
                            k=k.lower()
                            modfilelist.append(k)
                    print()
                    filename=input("Enter the File Name(unique): ")
                    if ".csv" not in filename:
                        filename+=".csv"
                        
                    if filename.lower() in modfilelist:
                        print("The File","'",filename,"'","is already present in the Folder","'",foldche,"'")
                        print("Please Enter Another Name")
                        loop=True
                    else:
                        loop=False

                    if loop==False:
                        file=open(filename,"a",newline="",encoding='utf-8')
                        writeobj=csv.writer(file)

                        comp=input("Enter Business Name: ")

                        dinp=True
                        while dinp==True:
                            predate=input("Enter the Date(dd/mm/yyyy): ")
                            dinp,inputdate=date(predate)
                            
                        writeobj.writerow([comp])
                        writeobj.writerow([inputdate])
                        writeobj.writerow(["Sl.no.","Particulars","Debit","Credit"])

                        slno=0
                        ent="y"
                        dtot=0
                        ctot=0
                        while ent=="y":
                            slno+=1
                            print()
                            dcash,ccash,rec=trialbal(slno)
                            if dcash!=None:
                                dtot+=dcash
                            if ccash!=None:
                                ctot+=ccash
                            writeobj.writerow(rec)
                            print()
                            ent=input("Do you want to Enter another Account(y/n): ")
                        bal=ctot-dtot
                        slno+=1
                        modslno=str(slno)+"."
                        
                        if bal>0:
                            balmod="Rs. "+str(bal)
                            slno=str(slno)+"."
                            writeobj.writerow([modslno,"Suspense A/c",balmod," "])
                            dtot+=bal
                            print()
                            print("Suspense Account of",balmod,"has been created in Debit Balance (Asset).")

                        if bal<0:
                            bal=abs(bal)
                            balmod="Rs. "+str(bal)
                            slno=str(slno)+"."
                            writeobj.writerow([modslno,"Suspense A/c"," ",balmod])
                            ctot+=bal
                            print()
                            print("Suspense Account of",balmod,"has been created in Credit Balance (Liability).")

                        ctotmod="Rs. "+str(ctot)
                        dtotmod="Rs. "+str(dtot)
                        writeobj.writerow([" ","Total",dtotmod,ctotmod])
                        file.close()
   
                        print()
                        print("The Trial Balance is Entered...")
                        os.chdir(oldcwd)
                        print()

                else:
                    print()
                    main2=input("Do you want to go to 'TRIAL BALANCE MAIN MENU'(y/n): ")
                    main2=main2.lower()
            
            elif ch=='3':
                os.chdir(oldcwd)
                cwd=os.getcwd()
                folder=os.listdir(cwd)
                modfolder=[]
                get="y"
                while get=="y":
                    print()
                    print("List of Folders in the Directory is/are: ")
                    for i in folder:
                        if os.path.isdir(cwd+"\\"+i):
                            print(i)
                            modfolder.append(i.lower())
                        else:
                            pass
                    print()

                    if len(modfolder)==0:
                        print("The Folder is Empty...")
                        print()
                        break

                    foldche=input("Enter the Folder Name: ")
                    try:
                        directory,fileche=folfilecheck(cwd,foldche,modfolder)
                        print()
                        if directory!=None:
                            print("The Directory of the File is : ")
                            print(directory)
                        if directory==None:
                            pass
                        else:
                            print()
                            print("The Data in the File is: ")
                            file=open(directory,"r",newline='\r\n',encoding='utf-8')
                            readobj=csv.reader(file)
                            l=[]
                            head=[]
                            cou=0
                            for i in readobj:
                                if cou>1:
                                    l.append(i)
                                else:
                                    head.append(i[0])
                                cou+=1

                            c=l[0]
                            l.remove(c)
                            print()
                            print(head[0])
                            print("Trial Balance as on",head[1])
                            res=tabulate(l,headers=c,tablefmt="fancy_grid")
                            print(res)
                            print()                    
                    except:
                        pass

                    get=input("Do you want to Search Again(y/n): ")
                    get=get.lower()

                else:
                    print("Thankyou")
                    print()
                main2=input("Do you want to go to 'TRIAL BALANCE MAIN MENU'(y/n): ")
                main2=main2.lower()

            elif ch=='4':
                helpjourn()
                
                main2=input("Do you want to go to 'TRIAL BALANCE MAIN MENU'(y/n): ")
                main2=main2.lower()

            elif ch=='5':
                print()
                print("Thankyou")
                print()
                break

            elif ch not in ['1','2','3','4','5']:
                print()
                print("Enter a valid choice")
                main2=input("Do you want to go to 'TRIAL BALANCE MAIN MENU'(y/n): ") 
                main2=main2.lower() 
        else:
            print()
            print("Thankyou")
            print()

    elif chmain=='3':
        print()
        print("Thankyou")
        print()
        break

    elif chmain not in ['1','2','3']:
        print()
        print("Enter a valid choice")
        headmain=input("Do you want to go to the 'MAIN MENU'(y/n): ") 
        headmain=headmain.lower() 
else:
    print()
    print("Thankyou")
    print()
