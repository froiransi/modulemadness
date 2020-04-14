class Module: #object module from the network
    # Variables
    input = ""
    output = ""
    preInput = ""

    # Constructor
    def __init__(self, name, operation):
        # Variables
        self.name = name
        self.operation = operation
        self.connection = []

    # Operations
    def echo(self):  # concat itself
        self.output = f"{self.input}{self.input}"

    def reverse(self):  # reverse the string
        self.output = self.input[::-1]

    def delay(self):  # concat previous input
        if (self.preInput != ""):
            self.output = self.preInput
        else:
            self.output = "hello"

    def noop(self):  # return unchanged
        self.output = self.input

    def out (self, input): #method to process final output
        self.input = input
        if len(self.connection) != 0: #if my entry depends on anothers module output
            for i in range(0, len(self.connection)):
                self.connection[i].out(self.input) #recursive call until I find first module of the network
                self.input = self.connection[i].output #summing outputs
        if self.operation == "echo":
            self.echo()
        elif self.operation == "reverse":
            self.reverse()
        elif self.operation == "delay":
            self.delay()
        else:
            self.noop()
        self.preInput = self.input #updating previous input