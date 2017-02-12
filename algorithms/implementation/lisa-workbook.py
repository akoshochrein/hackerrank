n, k = map(int, raw_input().strip().split(' '))
t = map(int, raw_input().strip().split(' '))

current_page = 1
specials = 0
pages_per_chapter = []
for problem_count in t:
    pages_for_chapter = problem_count // k + (1 if problem_count % k > 0 else 0)
    for i in xrange(pages_for_chapter):
        if current_page + i in range(i * k + 1, min(i * k + k + 1, problem_count + 1)):
            specials += 1
    current_page += pages_for_chapter

print specials
