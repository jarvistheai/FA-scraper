# Storing and pulling function for added memory

import os

def storedata(*args):
    with open('memory.txt', 'w') as file:
        for i in args:
            file.write(f'{i}\n')

def getdata():
    with open('memory.txt', 'r') as file:
        data = []
        for line in file:
            data.append(line.strip())
        return data
