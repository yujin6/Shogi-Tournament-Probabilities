# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 06:07:28 2020

@author: Yujin
"""

def odd(match, elo):
    return 1 / (pow(10, ((elo[match[1]] - elo[match[0]])/400)) + 1)

def odds(pattern, elo):
    prob = 1
    for match in pattern:
        prob = prob * odd(match, elo)
    return prob

def calculate(player, elo):
    pattern = [(0, 1), (2, 3), (0, 2)]
    prob = odds(pattern, elo)
    pattern = [(0, 1), (3, 2), (0, 3)]
    prob = prob + odds(pattern, elo)
    total = prob
    print(player[0] + " " + str(prob * 100) + "%")
    pattern = [(1, 0), (2, 3), (1, 2)]
    prob = odds(pattern, elo)
    pattern = [(1, 0), (3, 2), (1, 3)]
    prob = prob + odds(pattern, elo)
    total += prob
    print(player[1] + " " + str(prob * 100) + "%")
    pattern = [(0, 1), (2, 3), (2, 0)]
    prob = odds(pattern, elo)
    pattern = [(1, 0), (2, 3), (2, 1)]
    prob = prob + odds(pattern, elo)
    total += prob
    print(player[2] + " " + str(prob * 100) + "%")
    pattern = [(0, 1), (3, 2), (3, 0)]
    prob = odds(pattern, elo)
    pattern = [(1, 0), (3, 2), (3, 1)]
    prob = prob + odds(pattern, elo)
    total += prob
    print(player[3] + " " + str(prob * 100) + "%")
    print(total)

def main():
    player = ["永瀬拓矢 二冠", "山崎隆之 八段", "佐藤天彦 九段", "藤井聡太 七段"]
    elo = [1925, 1732, 1768, 1944] # 4/10
    calculate(player, elo)

if __name__ == '__main__':
    main()