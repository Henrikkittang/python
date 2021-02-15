

class Selector(object):
    def __init__(self, tag, body):
        self.tag = tag
        self.body = body

    def __repr__(self):
        string = self.tag + '{\n'
        for attr in self.body:
            string += '    ' + attr + ': ' + self.body[attr] + ';\n'
        return string

    def __repr__(self):
        return self.tag + str(self.body)


class Parser(object):
    def __init__(self, content):
        self.content = content
        self.curChar = None
        self.curIdx = 0
        self.selectors = []
        self.advance()

    def advance(self):
        if self.curIdx < len(self.content):
            self.curChar = self.content[self.curIdx]
        else:
            self.curChar = None
        self.curIdx += 1

    def peek(self):
        if self.curTokIdx < len(self.tokens):
            return self.tokens[self.curTokIdx]
        else:
            return None

    def parse(self):
        while self.curChar != None:
            if self.curChar == ' ' and self.curChar == '\n':
                self.advance()
                continue
            # self.removeComment()
            tag = self.makeTag()
            if self.curChar == None: break
            body = self.makeBody()
            
            self.selectors.append( Selector(tag, body) )
        
    def makeTag(self):
        curStr = ''
        print('parser: ' + self.curChar)
        while self.curChar != '{' and self.curChar != None:
            # self.removeComment()
            if self.curChar == '\n':
                self.advance()
                continue
            curStr += self.curChar
            self.advance()

        return curStr
            

    def makeBody(self):
        curStr = ''
        self.advance()
        while self.curChar != '}' and self.curChar != None:
            # self.removeComment()
            if self.curChar == '\n':
                self.advance()
                continue
            curStr += self.curChar
            self.advance()    
        self.advance()
 
        attributes = curStr.split(';')
        if attributes[-1] == '': attributes.pop()
        print(attributes)
        body = {}
        for attr in attributes:
            if attr.isspace(): continue
            key, value = attr.split(':')

            key = key.strip()
            value = value.strip()

            body[key] = value

        return body

    def removeComment(self):
        if self.curChar == '/':
            self.advance()
            while self.curChar != '/': self.advance()
            self.advance()
        
    


            
                        


