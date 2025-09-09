def add(filename, description):
    with open(filename, 'w') as f:
        f.write(description + '\n')
    id = sum(1 for _ in open(filename))
    return id


def modify(filename, id, description):
    lines = []
    update = False
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('', 1)
            current_id, _ = parts
            if current_id == id:
                line = f"{current_id} {description}\n"
                update = True
            lines.append(line)
        if update:
            with open(filename, 'w') as f:
                f.writelines(lines)
            print(f" id numero  {id} est modifié avec succès.")
        else:
            print(f"ERROR, id numero  {id} pas trouvé!!")


def rm(filename, id):
    lines = []
    # exist = False
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('', 1)
            current_id = parts[0]
            if current_id == id:
                found = True
                continue
            lines.append(line)
    if found:
        with open(filename, 'w'):
            f.writelines(lines)
            print(f" ID numero  {id} a été supprimé avec succès ! .")


def show(filename):
    tasks = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(" ", 1)
            id, description = parts
            tasks.append((int(id)), description)
    tasks.sort(key=lambda x: x[0])
    for id, description in tasks:
        print(f'{id}  {description}')
