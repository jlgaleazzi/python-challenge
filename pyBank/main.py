# main file for pyBank
# dependencies
import os
import csv
# define file path

file_path = os.path.join('Resources','budget_data.csv')
# read file with csv reader

with open(file_path, newline='') as file:
    data = csv.reader(file,delimiter=',')
    #skip header
    next(data)
    #define var for totalProfitsl
    total_profits = 0
    #max_increase
    max_increase = 0
    max_increase_month =''
    #min_increase
    min_increase = 0
    min_increase_month =''
    # diference
    diference = 0
    #total diference for avg
    total_diference = 0
    # rows
    profits_list = []
    rows = 0
    count = 0

    for row in data:
        rows += 1
        total_profits += int(row[1])
        profits_list.append(row[1])
        if profits_list[count-1]:
            # calculate diference
            diference = int(row[1]) - int(profits_list[count-1])
            # check to see if it max_increase
            if diference > max_increase: 
                max_increase = diference
                max_increase_month = row[0]
            elif diference < min_increase:
                min_increase = diference
                min_increase_month = row[0]
            
            # add to total difference to calculate the average
            total_diference += diference
          
        count += 1
    avg_inc = total_diference/(rows-1)
    tm = "total Months : " + str(rows) +"\n"
    tp = "total Profit " +  str(total_profits) +"\n"
    ap = "average profit/loss " + str(avg_inc) +"\n"
    gi =  "Greatest Increase in Profits "+ str(max_increase_month) + " : " + str(max_increase) +"\n"
    gd = "Greatest Decrease in Profits "+ str(min_increase_month)+ " : " + str(min_increase) +"\n"
    print(tm) 
    print(tp)
    print(ap)
    print(gi)
    print(gd)
   
       # output to file
    out_file_path = os.path.join('Output','profits.txt')
    if os.path.exists('Output') == False :
        # create output Directory
        os.mkdir('Output')
    out_file = open(out_file_path,'w')
    out_file.write(tm) 
    out_file.write(tp)
    out_file.write(ap)
    out_file.write(gi)
    out_file.write(gd)
    out_file.close()