import time 

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self):
        student = []  

        possible_numbers = []
        for m in self.children:
            possible_numbers.append(m.value[0])
        
        
        student_identity = input('Please enter their student number: ' )

        if not student_identity in possible_numbers:
            student_name = input('Please enter the student\'s name:' )
            grade = input('Please enter their grade: ') 

            identity = TreeNode([student_identity, student_name, grade])

            self.children.append(identity)
        else:
            print('That ID is already in the database')

    def remove_child(self):
        student_re = input('Please enter their student number: ')
        student_index = None
        
        checker = []
        for i in self.children:
            if student_re == i.value[0]:
                checker.append(student_re)
            else:
                pass
        if len(checker) == 0:
            print('That ID is not valid ')
        
        else:
            for j in self.children:
                if student_re == j.value[0]:
                    student_index = student_re
                    continue 
        
        self.children = [k for k in self.children if k.value[0] != student_index]

    
    def traverse(self):
        node = self
        student = input('Please enter student ID: ')

        descriptions = ['Student ID', 'Name', 'Mark']
        descriptions_index = 0
        checker = []
        for i in node.children:
            if student == i.value[0]:
                checker.append(i)

        if len(checker) >= 1:

            while len(node.children) > 0:
                for l in range(len(node.children)):
                    if student == node.children[l].value[0]:
                        for i in node.children[l].value:
                            print('{}: '.format(descriptions[descriptions_index]) + i)
                            
                            if descriptions_index == 2:
                                descriptions_index = 0
                            else:
                                descriptions_index += 1
                        #print(node.children[0].value)
                        node.children = node.children[0].children 
                        break
                    else:
                        continue
                        #node.value = node.children[0].value
                    
        else:
            print('That ID seems to be invalid')
            
        
    def edit(self):
        node = [self]
        student = input('Please enter a student ID: ')

        while len(node) > 0:
            current_node = node.pop()
            if current_node.value[0] == student:
                grade_updated = input('Please enter a new grade: ')
                current_node.value = [current_node.value[0], current_node.value[1], grade_updated]
                return 
                break 
            node += current_node.children 
                                                         

    
class Prompt:
    def gameplay(self):
        
        print('Welcome to your student database! ')
        database = TreeNode('Students: ')
        if len(database.children) == 0:
            num_students = input('Please enter the amount of students you have in your class: ')
            
            for i in range(int(num_students)):
                database.add_child()

                time.sleep(0.5)
        else:
            pass

        print('-----------------------------------------------------------------------')
        print('You can now do 3 actions: ')
        print('You can view your database using /traverse')
        print('You can remove a student using /remove')
        print('You can edit a student\'s mark using /edit')
        print('You can also add a new student using /add')
        print('You can also quit using /quit')
        print('-----------------------------------------------------------------------')
        playing = True 
        while playing:
            user = input()

            if user == '/traverse':
                database.traverse()

            elif user == "/remove":
                database.remove_child()
                print(database.children)

            elif user == "/edit":
                database.edit()

            elif user == "/add":
                database.add_child()

            elif user == "/quit":
                break
            
            else:
                print('That command is not valid ')

        

test = Prompt()
#print(test.gameplay())

