term = ''
termList = []
termDef = []
number = -1
while(term != 'Stop'):
    print('Please Enter a term, "Stop", or "File"')
    term = input().capitalize()
    if term == 'Stop': break
    if term == 'File':
        print('Please enter the file name:')
        f = open(input(), 'r')
        line = f.readline()
        while (line):
            termList.append(line[6:-1 ])
            line = f.readline()
            termDef.append(line[12:-1])
            line = f.readline()
        continue
    termList.append(term)
    print('Please enter the definition for: ' + term)
    termDef.append(input())
print('Study Session begun')
print('---------------------')
while(True):
    print('Please enter the term number or "Stop":')
    term = input()
    if term.capitalize() == "Stop": break
    for i in term.split(' '):
        if i.isnumeric():
            if int(i) > len(termList) or int(i) < 1:
                print("There is no term: " + i)
                print('Please try again')
                break
            print('Term '+ i + ': ' + termList[int(i)-1])
            input()
            print(termList[int(i)-1] + ', Definition: ' + termDef[int(i)-1])
            break
print('Program Ended')