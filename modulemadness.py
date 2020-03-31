
#Variables

modules = {} #dictionary of modules
connections = [] #array of connections
read = True #while loop condition
max_output = 0 #max_lenght output string
previous_input = "hello"

#Methods

def echo(str): #concat itself
    return f"{str} {str}"

def reverse(str): #reverse the string
    str = str[::-1] 
    return f"{str}"

def delay(str): #concat previous input
    return f"{previous_input} {str}"

def noop(str): #return unchanged
    return f"{str}"

def process_entry(str): #method that process the entry
    current_input = str
    count = 0 #counter of times we have summed several entries to the same module
    for node in connections:
        module1 = node[0]
        operation1 = modules[module1]["operation"]
        if len(modules[module1]["connections"]) > 1 and count == 0: #if there is more than one connection to the same node then sum them
            rep_conections = modules[module1]["connections"] #array of the connections of this module
            count = count + 1
            for rep in rep_conections:
                current_input = eval(operation1)(current_input) #evaluate first operation
                previous_input = current_input #save last input
                current_input = eval(modules[rep]["operation"])(current_input) #evaluate second operation
                previous_input = current_input #save last input
        module2 = node[1]
        operation2 = modules[module2]["operation"]
        current_input = eval(operation1)(current_input)
        previous_input = current_input
        current_input = eval(operation2)(current_input)
        previous_input = current_input

    return current_input #return last output string

while read: #loop to read entry
    entry = input()
    entry_splitted = entry.split()
    if entry_splitted[0] == "module": #saving the modules
        modules[entry_splitted[1]] = {
            "operation": entry_splitted[2],
            "connections": [], #array of connections to this module
        }
    elif entry_splitted[0] == "connect":
        modules[entry_splitted[1]]["connections"].append((entry_splitted[2]))
        connections.append((entry_splitted[1], entry_splitted[2])) #array of connections to keep the order of entry
    else:
        max_output = 16 * (len(entry_splitted) - 1) #max_lenght of the output string
        read = False #after reading all the modules and connections go to the next loop to read the strings to process

print (process_entry(" ".join(entry_splitted[1:]))) #first call to the process method

while True: #loop to read N process entries
    entry = input()
    entry_splitted = entry.split()
    print (process_entry(" ".join(entry_splitted[1:]))) #remove the word process before procesing the string

