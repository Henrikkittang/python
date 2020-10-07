NUMBERS = '0123456789'

class Token:
    def __init__(self, typ, value=None):
        self.type = typ
        self.value = value

    def __repr__(self):
        if(self.value):
            return self.type + ': ' + str(self.value)
        else:
            return self.type


class Lexer:
    def __init__(self, text):
        self.rawText = text
        self.index = -1
        self.curChar = None

    def next(self):
        self.index += 1
        try: return self.rawText[self.index]
        except: return None 
    
    def makeTokens(self):
        tokens = []
        self.curChar = self.next()

        while(self.curChar != None):
            if self.curChar in NUMBERS:
                newTok = self.makeNumber()
                tokens.append(newTok)
            if self.curChar == '+':
                newTok = Token('ADD')
            elif self.curChar == '-':
                newTok = Token('SUB')
            elif self.curChar == '*':
                newTok = Token('MUL')
            elif self.curChar == '/':
                newTok = Token('DIV')
            elif self.curChar == '(':
                newTok = Token('LPAR')
            elif self.curChar == ')':
                newTok = Token('RPAR')
            else:
                self.curChar = self.next()
                continue
            self.curChar = self.next()
            tokens.append(newTok)
        return tokens

    def makeNumber(self):
        curNum = ''
        while(str(self.curChar) in NUMBERS):
            curNum += self.curChar
            self.curChar = self.next()
        return Token('NUM', int(curNum))


class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.operation = op
        self.right = right
    
    def __repr__(self):
        return f'({self.left}, {self.operation}, {self.right})'


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = -1
        self.curTok = None

    def next(self):
        self.index += 1
        try: self.curTok = self.tokens[self.index]
        except: self.curTok = None
        return self.curTok

    def parse(self):
        self.curTok = self.next()
        return self.func(self.curTok)

    def func(self, tok):
        left = NumberNode(tok.value)
        op = self.next()
        if op != None: 
            print(op)           
            if op.type in ('ADD', 'SUB', 'MUL', 'DIV'):
                right = NumberNode(self.func(self.next()))
                return BinOpNode(left, op, right)
        else:
            return left                    

def main():
    with open('source.txt', 'r') as f:
        data = f.read()
        f.close()

    lexer = Lexer(data)
    tokens = lexer.makeTokens()

    parser = Parser(tokens)
    res = parser.parse()
    print(res)

main()






