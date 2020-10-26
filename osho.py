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

def adjust(player, comb, odds, p, result):
    if result[1] == 'W':
        odds[result[0]] = 1 if p[result[0]] else 0
    else:
        odds[result[0]] = 0 if p[result[0]] else 1

def calculate(player, elo, actual):
    solo = []
    tie = []
    playoff = []
    num_p = len(elo) # number of players
    print(" 棋士一覧: ")
    for i in range(num_p):
        print (str(i) + " " + player[i])
        solo.append(0)
        tie.append(0)
        playoff.append(0)
    num_m = (num_p * (num_p - 1)) // 2 # number of matches
    comb = list(combinations(list(range(num_p)), 2)) # combination of matches
    # print(comb)
    print(" 実際の対局結果： ")
    for result in actual:
        print(player[comb[result[0]][0]] + (" 〇 - ● " if result[1] == 'W' else " ● - 〇 ") + player[comb[result[0]][1]])
    for patterns in range(pow(2, num_m)):
        p = [] # pattens of wins and loses in each match
        for match in range(num_m): p.append((patterns // pow(2, match)) % 2)
        odds = []
        prob = 1
        winners = []
        for i in range(num_m):
            odds.append(odd(comb[i], elo)) if p[i] else odds.append(1 - odd(comb[i], elo))
            winners.append(comb[i][0]) if p[i] else winners.append(comb[i][1])
        for result in actual: # adjust with actual results
            adjust(player, comb, odds, p, result)
        odds = matched(odds, p)
        prob = numpy.prod(odds)
        winners = champion(winners)
        for i in range(num_p):
            if i in winners:
                tie[i] += prob
                if len(winners) == 1: solo[i] += prob
        playoff[len(winners) - 1] += prob
    print(" 1位の確率: ")
    for i in range(num_p):
        print(left(18, player[i]) + str(solo[i] * 100) + "%, " + str(tie[i] * 100) + "% ")

def main():
    player = ["広瀬章人 八段", "豊島将之 竜王", "藤井聡太 二冠", "羽生善治 九段", "永瀬拓矢 王座", "木村一基 九段", "佐藤天彦 九段"]
    elo = [1782.5, 1908.0, 1975.5, 1827.2, 1931.5, 1787.5, 1756.3] # 7/25
    elo = [1770.8, 1887.2, 1986.3, 1819.5, 1945.5, 1788.4, 1774.2] # 8/26
    elo = [1772.7, 1911.7, 1969.5, 1835.8, 1933.9, 1761.5, 1777.2] # 9/23
    elo = [1789.8, 1930.5, 1965.3, 1822.5, 1946.2, 1764.8, 1756.3] # 10/5
    elo = [1786.0, 1951.5, 1967.6, 1823.6, 1953.6, 1773.5, 1743.0] # 10/22
    actual = []
    actual.append((0, 'L'))   # 広瀬章人 八段 ● - 〇 豊島将之 竜王
    actual.append((5, 'W'))   # 広瀬章人 八段 〇 - ● 佐藤天彦 九段
    actual.append((6, 'W'))   # 豊島将之 竜王 〇 - ● 藤井聡太 二冠
    actual.append((9, 'W'))   # 豊島将之 竜王 〇 - ● 木村一基 九段
    actual.append((11, 'L'))  # 藤井聡太 二冠 ● - 〇 羽生善治 九段
    actual.append((12, 'L'))  # 藤井聡太 二冠 ● - 〇 永瀬拓矢 王座
    actual.append((17, 'W'))  # 羽生善治 九段 〇 - ● 佐藤天彦 九段
    actual.append((18, 'W'))  # 永瀬拓矢 王座 〇 - ● 木村一基 九段
    actual.append((19, 'W'))  # 永瀬拓矢 王座 〇 - ● 佐藤天彦 九段
    calculate(player, elo, actual)

if __name__ == '__main__':
    main()