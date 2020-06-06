# -*- coding: utf-8 -*-
"""
Description
Given a string, you have to find the first n most frequent characters in it.

You have to print these n letters in alphabetically sorted order.

The input will contain two lines, the first line will contain a string and the second line will contain the letter n.

The output should be a list of n most frequent letters in alphabetically sorted order.

Note: If there are two letters with the same frequency, then the alphabetically preceding alphabet should be picked first. (For example, in "aabbccc", if n=2, then output list would have c and a.)

Sample Input:

ddddaacccb

3

Sample Output:

['a', 'c', 'd']


In the above example, the order of frequencies is : d>c>a>b

Here, d,c and a are three most frequent characters which are displayed in alphabetically sorted order.

Execution Time Limit
Default.
"""

string=input()
n=int(input())
import collections
out=[collections.Counter(string).most_common(i+1)[i][0] for i in range(n)]
out.sort()
print(out)


