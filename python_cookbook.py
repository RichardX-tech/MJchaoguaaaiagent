# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 31/8/2025
# @Author  : xmj-ANAN
# @Github  : https://github.com/RichardX-tech
# @CSDN    : https://blog.csdn.net/weixin_44568751?type=blog
# @Software: PyCharm
# @File    : python_cookbook.py
p =(4,5)
x, y = p
print(x)
print(y)
print("--------------")

data = ['ACME', 50 ,91.1, (2025, 9, 1)]
name, shares,price, data = data
print(name, data)
print("--------------")

data = ['ACME', 50 ,91.1, (2025, 9, 1)]
name, shares, price, (year, mon, day) = data
print(name, year, mon, day)
print("--------------")

'''
tips:
如果元素不匹配，则得到一个错误❌提示
e.g.:
>>> p = (4,5)
>>> x, y, z = p
Traceback(most recent call list):
    File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpacl
'''

# 只要对象是可迭代的，就可以执行分解操作。包括字符串string、文件file、迭代器、生成器。
s='hello'
a, b, c, d, e = s
print(a, b, e)
print("--------------")

# 当做分解时，想要丢掉某些特定值
data = ['ACME', 50, 91.1, (2025, 9, 1)]
_, shares, price, _=data
print(shares)
print(price)
print("--------------")

# 1.2 从任意长度的可迭代对象中分解元素
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)

user_record = ('dave', 'anonymous7h2yhy@snapmail.cc', '789-555-1234', '666-555-1234')
name,email, *phone_numbers = user_record
print(name)
print(email)
print(phone_numbers)
print("--------------")

*tailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(tailing)
print(current)
tailing_avg = sum(tailing) / len(tailing)
print(tailing_avg)
print("--------------")
# 利用*表达式分解可迭代对象使得开发者能够轻松的使用这些模式，而不必在可迭代对象中做复杂花哨的操作才能得到相关的元素。
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print("--------------")

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print("--------------")

record = ('ACME', 50, 123.45, (3, 9, 2025))
name, *_, (*_, year) = record
print(name)
print(year)
print("--------------")

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)
print("--------------")

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
print("--------------")

# 1.3 保存最后N个元素（保存有限的历史记录是collections.deque的完美应用场景。）
from collections import deque
def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# # example use on a file
# if __name__ = '__main__':
#     with open(somefile.txt) as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-'*20)






