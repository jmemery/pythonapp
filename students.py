students = [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }

def all_students(arr):
    for x in students:
        print x['first_name'], x['last_name']

def all_u(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(person['first_name']) + len(person['last_name'])
            print "{} - {} {} - {}".format(counter, person['first_name'], person['last_name'], length)

all_students(students)
all_u(users)
