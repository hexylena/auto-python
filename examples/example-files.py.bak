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
# Get the unique options
unique_speakers = set(speakers)
counts = [
    (s, speakers.count(s))
    for s in
    unique_speakers
]
counts = sorted(counts, key=lambda x: -x[1])

print(counts[0:10])
