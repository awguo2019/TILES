# change the path above to whatever

def convert_tsv(pathname):
    with open(pathname + '.txt') as fin, open(pathname + '.tsv', 'w') as fout:
    #to have data in separate columns from a single column
        for line in fin:
            fout.write(line.replace(' ', '\t'))

convert_tsv('../../CollegeMsg')