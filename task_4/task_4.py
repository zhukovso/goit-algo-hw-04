
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"A contact with the name '{name}' already exists!"
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"The contact with the name '{name}' does NOT exist!"
    
def show_phone(name, contacts):
    return contacts.get(name)

def show_all(contacts):
    return_str = ""
    #max_name_len = len(max(contacts.keys(), key=len))
    for k, v in contacts.items():
        return_str += f"{k:>15}: {v:<15}\n"
    return return_str
    #return '\n'.join(map('\t'.join, contacts.items()))

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        try:
            command, *args = parse_input(user_input)
            #print(f"command: {command}, args: {args}")


            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")

            #> add [ім'я] [номер телефону]
            elif command == "add":
                print(add_contact(args, contacts))

            #> change [ім'я] [новий номер телефону]
            elif command == "change":
                print(change_contact(args, contacts))

            #> phone [ім'я]
            elif command == "phone":
                print(show_phone(args[0], contacts))

            #> all
            elif command == "all":
                print(show_all(contacts))

            else:
                print("Invalid command.")
        except ValueError as e:
            print(f'Invalid command.')
        except UnboundLocalError as e:
            print(f'Invalid command.')

if __name__ == "__main__":
    main()