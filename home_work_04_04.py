def parse_input(user_input):
    """Function parsing input data"""
    parts = user_input.strip().split()

    if not parts:
        return "", []

    cmd, *args = parts
    return cmd.lower(), args


def add_contact(args, contacts):
    """Function added new contact"""
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Input: add <name> <phone>"


def change_username_phone(args, contacts):
    """Function change contacts"""
    try:
        name, new_phone = args
    except ValueError:
        return "Input: change <name> <new_phone>"

    if name in contacts:
        contacts[name] = new_phone
        return "Contact changed."

    return "Contact not found."


def show_phone(args, contacts):
    """Search contacts by name"""
    if not args:
        return "Input: phone <name>"

    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Contact not found."


def show_all(contacts):
    """Show all contacts with phone"""
    if not contacts:
        return "No contacts saved"

    result_info = []

    for name, phone in contacts.items():
        result_info.append(f"{name}: {phone}")

    return "\n".join(result_info)

def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

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
            print(show_all(contacts))

        elif command == "":
            continue

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()