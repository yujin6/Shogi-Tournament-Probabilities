# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:51:09 2020

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
    loser = [0, 0, 0]
    num_m = len(player) // 2 # number of matches
    for patterns in range(pow(2, num_m)):
        p = [] # patterns of wins and loses in each match
        for match in range(num_m): p.append((patterns // pow(2, match)) % 2)
        prob = 1
        for i in range(num_m):
            prob *= odd((2 * i, 2 * i + 1),elo) if p[i] else odd((2 * i + 1, 2 * i),elo)
        if p[2] == 0:
            loser[2] += prob
        elif p[1] == 0:
            loser[1] += prob
        elif p[0] == 0:
            loser[0] += prob
        else:
            loser[2] += prob
    for i in range(len(loser)):
        print(left(18, player[2 * i]) + str(loser[i] * 100) + "% ")

def main():
    player = ["佐藤天彦 九段", "稲葉陽　 八段", "糸谷哲郎 八段", "久保利明 九段", "木村一基 王位", "広瀬章人 八段"]
    elo = [1754, 1789, 1741, 1765, 1781, 1833]
    calculate(player, elo)

if __name__ == '__main__':
    main()