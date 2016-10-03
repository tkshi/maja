# -*- coding: utf-8 -*-
import copy


tehai = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0],
]

matched = {
'atama':False,
'ments':0
}

def getTartsu(tehai,index,matched):
    tehai = tehai[:]
    index = index[:]
    matched = copy.deepcopy(matched)
    for row_i in range(0,5):
        index = (row_i,index[1])
        for i in range(0,len(tehai[row_i])):
            index = (index[0],i)
            if tehai[index[0]][index[1]] >= 3:
                tehai[index[0]][index[1]] = tehai[index[0]][index[1]] -3
                matched['ments'] = matched['ments'] + 1
                break
    return [tehai,index,matched]



def getAtama(tehai,index,matched):
    tehai = tehai[:]
    index = index[:]
    matched = copy.deepcopy(matched)
    for row_i in range(0,4):
        index = (row_i,index[1])
        for i in range(0,len(tehai[row_i])):
            index = (index[0],i)
            if tehai[index[0]][index[1]] >= 2:
                tehai[index[0]][index[1]] = tehai[index[0]][index[1]] -2
                matched['atama'] = True
                return [tehai,index,matched]
                break
            else:
                index = (index[0],index[1] + 1)

def getShuntsu(tehai,index,matched):
    tehai = tehai[:]
    index = index[:]
    matched = copy.deepcopy(matched)
    for row_i in range(0,4):
        index = (row_i,index[1])
        for i in range(0,len(tehai[row_i])):
            index = (index[0],i)
            if tehai[index[0]][index[1]] and tehai[index[0]][index[1] + 1] and tehai[index[0]][index[1] + 2]:
                tehai[index[0]][index[1]] = tehai[index[0]][index[1]] -1
                tehai[index[0]][index[1]] = tehai[index[0]][index[1] + 1] -1
                tehai[index[0]][index[1]] = tehai[index[0]][index[1] + 2] -1
                matched['ments'] = matched['ments'] + 1
                break
            else:
                index = (index[0],index[1] + 1)
    return [tehai,index,matched]
