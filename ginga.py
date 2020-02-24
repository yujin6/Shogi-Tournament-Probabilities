# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:00:44 2020

@author: Yujin
"""

import unicodedata

def odd(match, elo):
    return 1 / (pow(10, ((elo[match[1]] - elo[match[0]])/400)) + 1)

def left(digit, msg):
    for c in msg:
        digit -= 2 if unicodedata.east_asian_width(c) in ('F', 'W', 'A') else 1
    return(msg + ' '*digit)

def calculate(player, elo):
    solo = [0, 0, 0, 0, 0, 0, 0]
    num_m = len(player) - 1 # number of matches
    for patterns in range(pow(2, num_m)):
        p = [] # patterns of wins and loses in each match
        for match in range(num_m): p.append((patterns // pow(2, match)) % 2)
        winner = 0
        prob = 1
        for i in range(num_m):
            prob *= odd((i + 1, winner),elo) if p[i] else odd((winner, i + 1),elo)
            if p[i]: winner = i + 1
        solo[winner] += prob
    for i in range(len(player)):
        print(left(18, player[i]) + str(solo[i] * 100) + "% ")

def main():
    player = ["出口若武　四段", "藤井聡太　七段", "中村　修　九段", "森内俊之　九段", "郷田真隆　九段", "稲葉　陽　八段", "羽生善治　九段"]
    elo = [1577, 1921, 1500, 1599, 1747, 1774, 1827]
    calculate(player, elo)

if __name__ == '__main__':
    main()