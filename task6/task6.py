with open('library.py') as file:
    reader = file.readlines()
    for n, i in enumerate(reader):
        if i[0:3] == 'def':
            if reader[n - 1][0] != '#':
                index1 = i.find(' ')
                index2 = i.find('(')
                print(i[index1:index2])
