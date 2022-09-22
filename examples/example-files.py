import urllib.request
import os

if not os.path.exists("hamlet.txt"):
    urllib.request.urlretrieve("https://gutenberg.org/cache/epub/1524/pg1524.txt", "hamlet.txt")

with open('hamlet.txt', 'r') as handle:
    # readlines reads every line of a file into a giant list!
    lines = handle.readlines()

print(lines[0])
print(lines[1])
print(lines[2])

speakers = [
    line.split(' ')[0]
    for line in lines
    if line.count(' ') > 0
]

speakers = [x for x in speakers if x.upper() == x]

import collections
c = collections.Counter(speakers)
print(c.most_common(10))
