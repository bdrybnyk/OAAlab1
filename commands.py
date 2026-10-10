def create(name):
    print(f"створюється мн: '{name}'")

def insert(name, x, y):
    print(f"вносимо ({x}, {y}) в '{name}'")

def print_tree(name):
    print(f"дерево для '{name}'")

def contains(name, x, y):
    print(f"шукаєм ({x}, {y}) у '{name}'")

def search_all(name):
    print(f"вивести все з '{set_name}'")

def search_inside(name, x_left, y_bot, x_right, y_top):
    print(f"пошук в '{name}'. "
          f"прямокутник від ({x_left}, {y_bot}) до ({x_right}, {y_top})")

def search_left_of(name, x):
    print(f"пошук зліва в '{set_name}', X < {x}")

def search_nn(name, x, y):
    print(f"пошук нн в '{set_name}', точка: ({x}, {y})")