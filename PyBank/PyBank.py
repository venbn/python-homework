import os
import csv
import numpy as npy

month_count=0
profit_losses=0
total_profit_losses=0
average_change=0
max_profits=0
max_losses=0
losses_month=""
profit_month=""
profit_increase=0
hdr=0
fmp=0
pr=0
plfm=0
pl_lst=[]


bd_csv=("/Users/vbn/Desktop/VenGitRepo/python-homework/PyBank/budget_data.csv")
op=open('/Users/vbn/Desktop/VenGitRepo/python-homework/PyBank/results.txt','w+')

with open(bd_csv,'r') as bd_csv:
    csvreader=csv.reader(bd_csv,delimiter=",")    
    hdr=next(csvreader)
    fr=next(csvreader)
    fmp=int(fr[1])
    month_count+=1
    plfm=int(fr[1])
    
    for line in csvreader:
    
        month_count+=1
        profit_losses=plfm+int(line[1])
        total_profit_losses+=profit_losses
        plfm=0
        
       # Maximum profits and losses
        
        pr=int(line[1])
        pi=int(pr)-int(fmp)
        fmp=pr
        
        pl_lst.append(pi)
        
        if max_losses == 0:
            max_losses=pi
        elif max_losses>pi:
            max_losses=pi
            losses_month=line[0]
        elif max_profits<pi:
            max_profits=pi
            profit_month=line[0]
    
    average_change=round(npy.mean(pl_lst),2)
    
    print(f"Financial Analysis")
    print(f"----------------------------------")
    print(f"Total Months: {month_count}")    
    print(f"Total: ${total_profit_losses}")
    print(f"Average change: ${average_change}")
    print(f"Greatest Increase in profits: {profit_month} (${max_profits})")
    print(f"Greatest Decrease in profits: {losses_month} (${max_losses})")
    
    #write to a file
    
    op.write(f"Financial Analysis\n")
    op.write(f"----------------------------------\n")
    op.write(f"Total Months: {month_count}\n")    
    op.write(f"Total: ${total_profit_losses}\n")
    op.write(f"Average change: ${average_change}\n")
    op.write(f"Greatest Increase in profits: {profit_month} (${max_profits})\n")
    op.write(f"Greatest Decrease in profits: {losses_month} (${max_losses})\n")
    op.close()
