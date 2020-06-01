# Parsing functions for the sidebar items

# stripping the letters from the sidebar items
# converting to int and make a list
def stripper(x):
    data = [0, 0, 0, 0, 0, 0]
    for i in x.split():
        if 'S' in str(i):
            data[0] = int(i.strip('S'))

        elif 'W' in str(i):
            data[1] = int(i.strip('W'))

        elif 'C' in str(i):
            data[2] = int(i.strip('C'))

        elif 'F' in str(i):
            data[3] = int(i.strip('F'))

        elif 'J' in str(i):
            data[4] = int(i.strip('J'))

        elif 'N' in str(i):
            data[5] = int(i.strip('N'))
    return data

# attaching the letters back to the list and deleting unchanged items
def destripper(data):
    strmsgs = [str(x) for x in data]

    if strmsgs[0] != '0' and not '-' in strmsgs[0]:
        strmsgs[0] = f'+{strmsgs[0]}S'
    else:
        strmsgs[0] = '0'

    if strmsgs[1] != '0' and not '-' in strmsgs[1]:
        strmsgs[1] = f'+{strmsgs[1]}W'
    else:
        strmsgs[1] = '0'

    if strmsgs[2] != '0' and not '-' in strmsgs[2]:
        strmsgs[2] = f'+{strmsgs[2]}C'
    else:
        strmsgs[2] = '0'

    if strmsgs[3] != '0' and not '-' in strmsgs[3]:
        strmsgs[3] = f'+{strmsgs[3]}F'
    else:
        strmsgs[3] = '0'

    if strmsgs[4] != '0' and not '-' in strmsgs[4]:
        strmsgs[4] = f'+{strmsgs[4]}J'
    else:
        strmsgs[4] = '0'

    if strmsgs[5] != '0' and not '-' in strmsgs[5]:
        strmsgs[5] = f'{strmsgs[5]}N'
    else:
        strmsgs[5] = '0'

    for i in range((len(strmsgs)-1), -1, -1):
        if strmsgs[i] == '0':
            strmsgs.pop(i)

    return strmsgs
