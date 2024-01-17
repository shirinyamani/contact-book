import collections

class Contactbook:
    def __init__(self):
        self.contact = collections.defaultdict(dict) #name:contact

    def read(self):
        for name, info in self.contact.items():
            print(f'name: {name}')
            print(f'phone: {info["phone"]}')
            print(f'email: {info["email"]}')
            print("-" * 50)


    def write(self, name, phone, email=None):
        if name in self.contact:
            print("Contact already exists!")
            return
        
        self.contact[name]["phone"] = phone
        self.contact[name]["email"] = email
        

    def update(self, name, phone=None, email=None):
        if name in self.contact:
            if phone:
                self.contact[name]['phone'] = phone

            if email:
                self.contact[name]['email'] = email
            print('COntact updated succesfully!')

        else: print("you dont have such contact!")

    def delete(self,name):
        if name not in self.contact:
            print("You dont have this contact!")
        else: 
            del self.contact[name]
            print(f'Contact {name} deleted!')

            


if __name__ == "__main__":
    book = Contactbook()
while True:
    print('Welcome to phonebook app...')
    print('1----> Add contact')
    print('2 -----> delete contact')
    print('3 -----> View Contact')
    print('4 -------> Edit COntact')
    print('5 for quit')

    user_choice = input('Enter your choice')
   

    if user_choice == "5":
        break

    elif user_choice == '1':
        name = input('Enter name')
        phone = input('Enter phone number')
        email = input('Enter email')

        book.write(name, phone, email)

    elif user_choice =='2':
        name = input('Enter name')
        book.delete(name)

    elif user_choice == '3':
        book.read()
        

    elif user_choice == '4':
        name = input('Enter name')
        phone = input('Enter phone number')
        email = input('Enter email')

        book.update(name, phone, email)

        