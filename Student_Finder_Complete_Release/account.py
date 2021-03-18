from database import Prompt
import time
import random

class HashMap:
    result_var = None
    def __init__(self, array_size=None):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]
        

    def hash(self, key, collisions=0):
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        definer = random.randint(1, 100)
        return hash_code + collisions + definer 

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def setter(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value != None:
            self.result_var = True 
            print("""
            \nYou might need to switch the class name as the database already has a class similar like that. 
            If you need more help, you can refer to the .md file on the Github page of this project.\n
            """)
        else:
            
            self.result_var = None
            if current_array_value == None:
                self.array[array_index] = [key, value]
                return 

            if current_array_value[0] == key:
                self.array[array_index] = [key, value]
                return 
            
            number_collisions = 1
            while current_array_value[0] != key:
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]


                if new_array_value == None:
                    self.array[new_array_index] = [key, value]
                    return

                if new_array_value[0] == key:
                    self.array[new_array_index] = [key, value]
                    return 
                number_collisions += 1
                return 

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            return None 

        if current_array_value[0] == key:
            return current_array_value[1]
        
        retrieve_collisions = 1 
        while current_array_value[0] != key:
            new_hash_code = self.hash(self, retrieve_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                return None 

            if new_array_value[0] == key:
                return new_array_value[1]
            
            retrieve_collisions += 1
            return 

    def delete(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            pass
        
        if current_array_value[0] == key:
            self.array[array_index] = None
            return 
        
        del_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, del_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                pass

            if new_array_value[0] == key:
                self.array[new_array_index] = None
                return 
            
            del_collisions += 1
            return 


class Gameplay:
    
    def gameplay(self):
        users = {}
        checker1 = 0
        checker2 = 0
        working = True
        possible_classes = []
        
        print('Hello, please enter your username: ')
        print('If you don\'t have one, please create one by typing /user: ')
        while working:
            
            prompt1 = input()

            if prompt1 == '/user':
                username = input('Please type a username: ')
                password = input('Please type in a password: ')

                users[username] = password 
                print('Great! Now you have an account, you can log in with your credentials!')
                time.sleep(1)

            elif prompt1 == "/quit":
                break 


            else:
                for i in users.keys():
                    if i == prompt1:
                        checker1 += 1
                        prompt2 = input("Please type in your password: ")

                        if prompt2 == "/quit":
                            break

                        for j in users.values():
                            if j == prompt2:
                                checker2 += 1

                                print("Success! You are now logged in to the student database! ")
                                time.sleep(0.5)
                                print('You have 4 options with your database. ')
                                time.sleep(0.5)
                                print('1) You can add a new class to your database by typing /add_class')
                                print('2) You can view your classes by typing /view_classes')
                                print('3) You can remove a class from the database by typing /remove_class')
                                print('4) You can access a class\'s grades by typing /access')
                                class_tracker = 0
                                data = HashMap(class_tracker)
                                



                                real_prompt = True

                                while real_prompt:
                                    print('Please enter a command: ')
                                    decisions = input()
                                    

                                    if decisions == "/add_class":
                                        num_classes = None

                                        while type(num_classes) != int:
                                            
                                            num_classes = input('Please enter the number of classes you have: ')
                                            try:
                                                num_classes = int(num_classes)
                                            except ValueError:
                                                print('Oops, that does not seem to be a valid input!')
                                          
                                        class_tracker += int(num_classes)
                                        data = HashMap(class_tracker)


                                        for i in range(int(num_classes)):
                                            subject = input('Please enter the name of your class: ')

                                            data.setter(subject, Prompt())

                                            if data.result_var == True:
                                                while data.result_var != None:
                                                    subject = input('Please enter the name of your class: ')
                                                    data.setter(subject, Prompt())
                                                pass
                                            else:
                                                possible_classes.append(subject)
                                        
                                        print('Success! ')
                                        time.sleep(1)

                                    if decisions == "/view_classes":
                                        clean_strings = []
                                        for i in data.array:
                                            try:
                                                for j in i:
                                                    if type(j) == str:
                                                        clean_strings.append(j)
                                                    else:
                                                        continue
                                            except TypeError:
                                                continue 
                                        
                                        print('Classes: ')
                                        for i in clean_strings:
                                            print(i)
                                    
                                    if decisions == "/remove_class":
                                        del_class = input('Please enter a class you want to remove: ')

                                        if len(possible_classes) == 0:
                                            print('You have not added a class yet!')
                                        else:
                                            if del_class in possible_classes:
                                                data.delete(del_class)
                                                possible_classes.remove(del_class)
                                            else:
                                                print("That does not seem to be a valid class!")
                                    
                                    if decisions == "/access":
                                        cert_class = input('Please type in a class you would like to access: ')
                                        if not cert_class in possible_classes:
                                            print("That class does not seem to be a valid class")
                                        else:
                                            data.retrieve(cert_class).gameplay()




                                    if decisions == "/quit":
                                        break

                                






                            else:
                                continue 
                        if checker2 == 0:
                            print('Password is incorrect')
                    else:
                        continue 
                if checker1 == 0:
                    print("User not available")

test = Gameplay()
print(test.gameplay())




