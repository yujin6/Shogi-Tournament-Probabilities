# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 05:18:13 2020

@author: Yujin
"""

import numpy
import unicodedata
from collections import Counter
from itertools import combinations

def odd(match, elo):
    return 1 / (pow(10, ((elo[match[1]] - elo[match[0]])/400)) + 1)

def matched(odds, p):
    return odds

def champion(winners):
    count = Counter(winners)
    most_wins = count.most_common(1)[0][1]
    champ = []
    for c in count:
        if dict(count)[c] == most_wins: champ.append(c)
    champ.sort()
    return champ

def left(digit, msg):
    for c in msg:
        digit -= 2 if unicodedata.east_asian_width(c) in ('F', 'W', 'A') else 1
    return(msg + ' '*digit)

def adjust(player, comb, odds, p, match, result):
    if result == 'W':
        odds[match] = 1 if p[match] else 0
    else:
        odds[match] = 0 if p[match] else 1

def calculate(player, elo):
    solo = []
    tie = []
    playoff = []
    num_p = len(elo) # number of players
    for i in range(num_p):
        solo.append(0)
        tie.append(0)
        playoff.append(0)
    num_m = (num_p * (num_p - 1)) // 2 # number of matches
    comb = list(combinations(list(range(num_p)), 2)) # combination of matches
    print(comb)
    for patterns in range(pow(2, num_m)):
        p = [] # pattens of wins and loses in each match
        for match in range(num_m): p.append((patterns // pow(2, match)) % 2)
        odds = []
        prob = 1
        winners = []
        for i in range(num_m):
            odds.append(odd(comb[i], elo)) if p[i] else odds.append(1 - odd(comb[i], elo))
            winners.append(comb[i][0]) if p[i] else winners.append(comb[i][1])
        # adjust with actual results
        odds = matched(odds, p)
        prob = numpy.prod(odds)
        winners = champion(winners)
        for i in range(num_p):
            if i in winners:
                tie[i] += prob
                if len(winners) == 1: solo[i] += prob
        playoff[len(winners) - 1] += prob
    print("1位の確率: ")
    for i in range(num_p):
        print(left(18, player[i]) + str(solo[i] * 100) + "%, " + str(tie[i] * 100) + "% ")

def main():
    player = ["広瀬章人 八段", "豊島将之 二冠", "羽生善治 九段", "藤井聡太 棋聖", "木村一基 王位", "佐藤天彦 九段", "永瀬拓矢 二冠"]
    elo = [1782.5, 1908.0, 1827.2, 1975.5, 1787.5, 1756.3, 1931.5] # 7/25
    elo = [1770.8, 1887.2, 1819.5, 1986.3, 1788.4, 1774.2, 1945.5] # 8/26
    calculate(player, elo)

if __name__ == '__main__':
    main()