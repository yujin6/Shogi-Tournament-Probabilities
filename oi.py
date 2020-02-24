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

def matched(odds, p, color):
    # if color == "紅組":
    #    odds[4] = 1 if not p[4] else 0
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

def calculate(player, elo, color):
    solo = [0, 0, 0, 0, 0, 0]
    duo = [0, 0, 0, 0, 0, 0]
    trio = [0, 0, 0, 0, 0, 0]
    quad = [0, 0, 0, 0, 0, 0]
    quin = [0, 0, 0, 0, 0, 0]
    sex = [0, 0, 0, 0, 0, 0]
    tie = [0, 0, 0, 0, 0, 0]
    playoff = [0, 0, 0, 0, 0, 0]
    num_p = len(elo) # number of players
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
        #白組
        odds[10] = 1 if p[10] else 0 # 稲葉陽     八段 〇 - ● 阿部健治郎 七段
        odds[4] = 0 if p[4] else 1   # 羽生善治   九段 ● - 〇 藤井聡太   七段
        odds = matched(odds, p, color)
        prob = numpy.prod(odds)
        winners = champion(winners)
        for i in range(num_p):
            if i in winners:
                tie[i] += prob
                if len(winners) == 1: solo[i] += prob
                if len(winners) == 2: duo[i] += prob
                if len(winners) == 3: trio[i] += prob
                if len(winners) == 4: quad[i] += prob
                if len(winners) == 5: quin[i] += prob
                if len(winners) == 6: sex[i] += prob
        playoff[len(winners) - 1] += prob
    print(color + " 1位の確率: ", end = " ")
    for i in playoff:
        print(str(i * 100), end = "% ")
    print("a")
    for i in range(num_p):
        print(left(18, player[i]) + str(solo[i] * 100) + "% " + str(duo[i] * 100) + "% "  + str(trio[i] * 100) + "% " + str(quad[i] * 100) + "% " + str(quin[i] * 100) + "% " + str(sex[i] * 100) + "% ")

def main():
    color = "紅組"
    player = ["豊島将之   二冠", "永瀬拓矢   二冠", "佐々木大地 五段", "鈴木大介   九段", "佐藤秀司   七段", "本田奎     五段"]
    elo = [1919, 1912, 1825, 1663, 1555, 1704]
    elo = [1916, 1925, 1809, 1661, 1560, 1691]
    calculate(player, elo, color)
    color = "白組"
    player = ["羽生善治   九段", "菅井竜也   七段", "稲葉陽     八段", "上村亘     五段", "阿部健治郎 七段", "藤井聡太   七段"]
    elo = [1819, 1833, 1751, 1526, 1669, 1903]
    elo = [1833, 1846, 1774, 1533, 1667, 1915]
    calculate(player, elo, color)

if __name__ == '__main__':
    main()