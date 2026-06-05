import json

courses = '{"name" : "Rahul", "languages" : ["Java", "Python"]}'

#loads method parses json string and then in returns dictionary
#loads will take string as input
#load will take file object as input
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)

print(dict_courses["name"])
print(dict_courses["languages"])
print(dict_courses["languages"][1])

list_languages = dict_courses["languages"]
print(type(list_languages))
print(list_languages[0])



##****** Parse content present in Json file
with open('Courses1.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))
#price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
        #print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] ==  45

with open('Courses2.json') as fi:
    data2 =  json.load(fi)
    assert data == data2


