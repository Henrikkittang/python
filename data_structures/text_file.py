
class Text_manager(object):
    def __init__(self, file):
        self.file = file
        with open(file, "r") as f:
            self.content = f.read().split("\n")
            f.close()

    def __repr__(self):
        """Returns the content of the file as one string, to the print function"""
        temp_content = ""
        for i in self.content:
            temp_content += "'" + i + "', "
        return temp_content

    def append(self, data):
        """Adds the data to the end of the file"""
        data = str(data)
        self.content.append(data)
        try:
            self.content.remove("")
        except:
            pass
        with open(self.file, "w") as f:
            temp_cont = ""
            for i in self.content:
                temp_cont += i + "\n"
            f.write(temp_cont)
            f.close()

    def remove(self, data):
        """Removes a specific data. Note: if data = 'dog', it will NOT remove dog from 'Hello dog' """
        data = str(data)
        self.content.remove(data)
        try:
            self.content.remove('')
        except:
            pass
        with open(self.file, "w") as f:
            temp_cont = ""
            for i in self.content:
                temp_cont += i + "\n"
            f.write(temp_cont)
            f.close()

    def remove_last(self):
        if self.content[0] == "":
            self.content.pop()
            self.content.pop()
        else:
            self.content.pop()
        with open(self.file, "w") as f:
            temp_cont = ""
            for i in self.content:
                temp_cont += i + "\n"
            f.write(temp_cont)
            f.close()

    def remove_line(self, line):
        """Removes a specific line, kind of like index"""
        self.content.pop(line-1)
        try:
            self.content.remove('')
        except:
            pass
        with open(self.file, "w") as f:
            temp_cont = ""
            for i in self.content:
                temp_cont += i + "\n"
            f.write(temp_cont)
            f.close()

    def line(self, line):
        """Returns the content of a specific line"""
        return self.content[line - 1]

    def get_line(self, data):
        """"Returns the line number for a piece of data"""
        for idx, i in enumerate(self.content):
            if i == data:
                return idx + 1
        raise ValueError(data)

    def set_line(self, line, value):
        """Replaces a specific line with the new value"""
        self.content[line-1] = value
        with open(self.file, "w") as f:
            temp_cont = ""
            for i in self.content:
                temp_cont += i + "\n"
            f.write(temp_cont)
            f.close()

    def remove_key(self, key):
        """Removes a key-value pair. eks 'Highscore: 100'"""
        for i in self.content:
            try:
                key_val = i.split(": ")
            except:
                continue
            if key_val[0] == key:
                self.content.remove(i)
                with open(self.file, "w") as f:
                    temp_cont = ""
                    for i in self.content:
                        temp_cont += i + "\n"
                    f.write(temp_cont)
                    f.close()
                return
        raise KeyError(key)

    def get_keys(self):
        dicts = []
        for i in self.content:
            try:
                key_val = i.split(": ")
                dicts.append({key_val[0]: key_val[1]})
            except:
                continue
        return dicts

    def get_key(self, key):
        """Returns a value from a key-value pair. eks returns 100 from 'Highscore: 100'"""
        for i in self.content:
            try:
                key_val = i.split(": ")
            except:
                continue
            if key_val[0] == key:
                return key_val[1]
        raise KeyError(key)

    def set_key(self, key, value):
        """Sets a value in a key-value pair. eks sets 100 in 'Highscore: 50' to 'Highscore: 100'"""
        value = str(value)
        for i in self.content:
            try:
                key_val = i.split(": ")
            except:
                continue
            if key_val[0] == key:
                key_val[1] = value
                temp = key_val[0] + ": " + key_val[1]
                idx = self.content.index(i)
                self.content[idx] = temp
                with open(self.file, "w") as f:
                    temp_cont = ""
                    for i in self.content:
                        temp_cont += i + "\n"
                    f.write(temp_cont)
                    f.close()
                return
        raise KeyError(key)

    def get_content(self):
        """Returns the content of the file as a list"""
        temp_content = self.content
        try:
            temp_content.remove('')
        except:
            pass
        return temp_content

    def clear(self):
        """Empties the file"""
        self.content = [""]
        with open(self.file, "w") as f:
            temp_cont = ""
            for i in self.content:
                temp_cont += i + "\n"
            f.write(temp_cont)
            f.close()

