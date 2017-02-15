s = raw_input().strip()

answer = s
could_reduce = True
while could_reduce:
    could_reduce = False
    for i in xrange(len(answer)-1):
        if answer[i] == answer[i+1]:
            answer = answer[:i] + answer[i+2:]
            could_reduce = True
            break

if answer == '':
    answer = 'Empty String'
print answer
