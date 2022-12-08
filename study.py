term = ''
termList = []
termDef = []
number = -1
while(term != 'Stop'):
    print('Please Enter a term or "Stop"')
    term = input().capitalize()
    if term == 'Stop': break
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