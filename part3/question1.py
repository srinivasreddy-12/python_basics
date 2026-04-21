#given a list of tuples with info(name,subject)
info = [
    ("srinu","maths"),
    ("vasu","science"),
    ("ravi","social"),
    ("vasu","maths"),
    ("ravi","science"),
    ("srinu","social"),
]
#1)list all unique course
unique_courses = set()
for course in info:
    unique_courses.add(course[1])
print(unique_courses)

#2)list students enrolled in maths
for name,course in info:
    if(course == "maths"):
        print(name)

#3)create dictionary (students,set of courses)
d = {}
for name,course in info:
    if(d.get(name) == None):
        d.update({name:set()})
        d[name].add(course)
    else:
        d[name].add(course)
print(d)