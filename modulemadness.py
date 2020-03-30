
#Variables

modules = {}
connections = []
read = True
previous_input = "hello"

#Methods

def echo(str):
    return str+str

def reverse(str):
    str = str[::-1] 
    return str

def delay(str):
    return f"{previous_input} {str}"

def noop(str):
    return str

def process_entry(str):
    entry = str[8:]
    current_input = ""

    for connection in connections:
        module1 = connection[0]
        operation1 = modules[module1]
        module2 = connection[1]
        operation2 = modules[module2]
        current_input = eval(operation1)(entry)
        previous_input = current_input
        current_input = eval(operation2)(current_input)
    return current_input

while read:
    entry = input()
    entry_splitted = entry.split()
    if entry_splitted[0] == 'module':
        modules[entry_splitted[1]] = entry_splitted[2]
    elif entry_splitted[0] == 'connect':
        connections.append((entry_splitted[1],entry_splitted[2]))
    else:
        read = False

print (process_entry(entry))

while True:
    entry = input()
    print (process_entry(entry))

