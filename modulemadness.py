import Module

# Variables
modules = []
read = True
entry = ""
entry_splitted = []
module = Module
out = ""
out_splitted = []
result = ""

# Main

while read:  # loop to read entry
    entry = input()
    entry_splitted = entry.split(" ")

    if entry_splitted[0] == "module":  # saving the modules
        module = Module.Module(entry_splitted[1],entry_splitted[2])
        modules.append(module)

    elif entry_splitted[0] == "connect":

        for x in range (0, len(modules)): #search in the array modules

            if (modules[x].name == entry_splitted[2]): #if I find the second module of this connection

                for t in range (0,len(modules)): #search in array modules

                    if modules[t].name == entry_splitted[1]: #if I find the first module of this connection
                        modules[x].connection.append(modules[t]) #saving first module in second module connection list

    elif entry_splitted[0] == "process":

        for y in range (1, len(entry_splitted)):
            modules[len(modules)-1].out(entry_splitted[y]) #process string on the last defined module
            out += modules[len(modules) - 1].output + " " #concat outputs

        #Start empty the network
        modules[len(modules) - 1].out("")
        out += modules[len(modules) - 1].output #we ensure that we have printed all the processed strings
        for w in range(0, len(modules)):
            modules[w].out("")
        #End empty the network

        if len(out.split(" ")) > (16*(len(entry_splitted)-1)): #max_output lenght
            out_splitted = out.split(" ")

            for v in range (len(out_splitted)-1, (16*len(entry_splitted))):
                result += out_splitted[v]

        else:
            result = out
        print(result) #Printed final output
        result = ""
        out = ""
        out_splitted = []

    else:
        read = False