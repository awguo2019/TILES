with open('CollegeMsg.txt') as fin, open('NewCollegeMsg.tsv', 'w') as fout:
#to have data in separate columns from a single column
    for line in fin:
        fout.write(line.replace(' ', '\t'))