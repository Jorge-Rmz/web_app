FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Lee un archivo de texto y retorna una lista de to-do """
    with open(filepath, 'r') as file_l:
        todos_local = file_l.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Escribe una lista de to-do en un archivo txt """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
