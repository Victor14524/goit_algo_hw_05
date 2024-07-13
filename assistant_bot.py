def input_error(func):
    '''
        Decorator: Error handling function
     '''

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return 'User not found.'
        except IndexError:
            return 'Invalid input format.'
        except Exception as e:
            return f'An error occurred: {str(e)}'

    return inner


def parse_input(user_input: str) -> list:
    '''
    Зarsing user input
    :param user_input: string
    :return: list of user input
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: str, contacts: dict) -> str:
    '''
    Adding a contacts into user - phone number dictionary
    :param args: user input string
    :param contacts: dict of users phones
    :return: adding of contacts into dict
    '''
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_username_phone(args: str, contacts: dict) -> str:
    '''
    Change users phone number in dict
    '''
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


@input_error
def show_phone(args: str, contacts: dict) -> tuple:
    '''
        Show users phone number in dict
    '''
    name, phone = args
    return contacts[name]


@input_error
def show_all_contacts(contacts: dict) -> dict:
    '''
        Show all users phone number in dict
    '''
    return "\n".join(f"{key}: {value}" for key, value in sorted(contacts.items()))


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
