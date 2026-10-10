import shlex

def handle_add(args):
    print(f"Викликано Add. Аргументи: {args}")

def handle_show(args):
    print(f"Викликано Show. Аргументи: {args}")

def handle_find(args):
    print(f"Викликано Find. Аргументи: {args}")

def handle_delete(args):
    print(f"Викликано Delete. Аргументи: {args}")

def main():
    print("Команди:\n" \
    "Add\n" \
    "Show\n" \
    "Find\n" \
    "Delete\n")
    
    while True:
        user_input = input(">> ").strip()
        
        if not user_input:
            continue
            
        try:
            parts = shlex.split(user_input)
        except ValueError:
            print("Помилка! Незакриті лапки!")
            continue
            
        if not parts:
            continue
            
        command = parts[0].lower()
        args = parts[1:]
        
        match command:
            case "exit" | "quit":
                print("Робота завершена")
                break

            case "add":
                handle_add(args)

            case "show":
                handle_show(args)

            case "find":
                handle_find(args)

            case "delete":
                handle_delete(args)

            case _:
                print(f"Невідома команда: '{command}'")

if __name__ == "__main__":
    main()