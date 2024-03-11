import eel
import json

todo_count = 0

eel.init('web')

def read_data():
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
    return data

def write_data(data):
    with open('data.json', 'w') as file:
        file.write(json.dumps(data))
    return data

@eel.expose
def create_todo(title):
    global todo_count
    
    new_todo = {
        'id': todo_count + 1,
        "title": title
    }

    data = read_data()
    data['todos'].append(new_todo)

    write_data(data)
    todo_count += 1

    return new_todo

eel.start('index.html')
