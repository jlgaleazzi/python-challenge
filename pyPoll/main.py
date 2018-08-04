# main file for pyPoll
import os
import csv

file_path = os.path.join('Resources','election_data.csv')

candidates = []
votes = []
winning_votes = 0
total_votes = 0
results = ''

with open(file_path,newline='') as file:
    data = csv.reader(file,delimiter=',')
    next(data)
    for row in data:
        candidate = row[2]
        if candidate  in candidates:
           idx = candidates.index(candidate)
           votes[idx] = votes[idx] + 1
        else:
            candidates.append(candidate)
            votes.append(1)
        total_votes += 1
# calculate % winner and format results
    for index in range(len(candidates)):
        if votes[index] > winning_votes:
            # store index
            winning_votes = votes[index]
            winning_index = index
        pct = (votes[index]/total_votes)*100
        strpct = '{:05.2f}'.format(pct)
        results += str(candidates[index]) +': '+ strpct + ' % ('+str(votes[index])+')' + '\n'

header = 'Election Results'
line = '--------------------------'
total_votes_str= 'Total Votes: '+str(total_votes) 
winner = 'Winner : '+candidates[winning_index] 
# print output to console     
print (header)
print (line)
print (total_votes_str)
print (line)   
print (results)
print (line)
print (winner)
print (line)
# output to file
out_file_path = os.path.join('Output','results.txt')
if os.path.exists('Output') == False:
    #create dir if it doesnt exists
    os.mkdir('Output')
 # write to file   
out_file = open(out_file_path,'w')
header += '\n'
out_file.write(header)
line += '\n'
out_file.write (line)
total_votes_str += '\n'
out_file.write (total_votes_str)
out_file.write (line)   
out_file.write (results)
out_file.write (line)
winner += '\n'
out_file.write (winner)
out_file.write (line)
out_file.close()
