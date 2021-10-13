class InstructionParser:
    def __init__(self):
        self.parameter = None
        self.rovername = None
        self.command = None
        self.values = None

    def parse_instruntion(self, instruction):
        self.__init__()
        parsed_data = instruction.strip().split(":")
        if len(parsed_data) < 2:  # Check if Line has Parameter and Values.
            return None, None, None, None

        if parsed_data[0] == "Plateau":
            self.parameter = parsed_data[0]
            self.values = parsed_data[1].split(" ")
        else: # Landing / Instructions
            self.parameter = parsed_data[0]
            received_params = parsed_data[0].split(" ")
            self.rovername = received_params[0]
            self.command = received_params[1]
            self.values = parsed_data[1].split(" ")
        return self.parameter, self.rovername, self.command, self.values
