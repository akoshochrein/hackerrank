# Enter your code here. Read input from STDIN. Print output to STDOUT

days = int(raw_input().strip())


total_people_liked = 0
people_reached_on_day = 5
for _ in xrange(days):
    people_who_liked = people_reached_on_day / 2
    total_people_liked += people_who_liked
    people_reached_on_day = people_who_liked * 3

print total_people_liked
