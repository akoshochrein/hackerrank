no_tests = int(raw_input().strip())

def deletions_until_alternating(word):
    counter = 0
    for i in xrange(len(word)-1):
        if word[i] == word[i+1]:
            counter += 1
    return counter

for _ in xrange(no_tests):
    word = raw_input().strip()
    print deletions_until_alternating(word)
