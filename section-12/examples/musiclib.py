class Reader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.result_map = {}
        self.read_file_content()

    def read_file_content(self):
        file = open(self.filepath, "r")
        line = file.readline()

        values = line.split("/")
        self.result_map["performer"] = values[0]
        self.result_map["album"] = values[1]
        
        trackinfo = values[2].split("-")
        self.result_map["track"] = trackinfo[0].strip()
        self.result_map["title"] = trackinfo[1].strip()[:-1]

    def get_value(self, key):
        return self.result_map[key]
