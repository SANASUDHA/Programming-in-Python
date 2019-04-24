# Sorting numbers from a text file

fh=open('input.txt')
lines = [line.split(' ') for line in fh]
output = open("output.txt", 'w')
for line in sorted(lines[0]):
    output.write(' '.join(line))
output.close()
