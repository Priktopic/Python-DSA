"""
In a nested dictionary, find which books and in which semester is taught by a teacher in a college. Here books are 'name', semester is 'spring2020',etc, 
subjects are 'cs101','cs373',etc.
"""

courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'c': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2021': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'}
                     }
    }
    
def which_book_taught_in_sem(courses, teacher_name, course):
    books=[]
    semester=[]
    """
    Prints all the keys and values of the dictionary. 
    Here the keys are "spring2020","fall2020" and "spring2021" and the remaining are values
    """
    for sem, sub in courses.items():
            
        """
        In "sub" part of the above dict there is another dict that contains keys as subjectnumber and its name along with teacher as the values
        """
        for subject,teacher_details in sub.items():
            if teacher_details['teacher'] == teacher_name: 
                """
                teacher_details['teacher']" prints the name of the teachers from the values of the dictionary "sub"
                If the teacher name matches with the name passed as a parameter, then it adds the "name" part from the values of the same dictionary in an
                empty list "books". Use set to remove duplicacy of the books taught by that teacher.
                """
                
                books.append(teacher_details['name'])
                books = list(set(books)) #remove string duplicacy
                
        if course in sub.keys():
            """
            Checks if the course passed as a parameter is present in the keys of "sub" dictionary. If yes, then it adds the value of "sem", i.e., the key
            of dictionary "courses" in an empty list, "semester".
            """
            semester.append(sem)
            
    return books, semester

books, semester = which_book_taught_in_sem(courses, 'Dave', 'cs101')
print("Dave teaches {0} in semester {1}".format(books, semester)) # We're checking what are the books taught and in which semester by the teacher named 'Dave' 


