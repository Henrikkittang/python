import cssparser

class CSSCompression(object):
    def __init__(self, filename):
        self.filename = filename

    def compressFile(self):
        content = self._readFile()
        cssp = cssparser.Parser(content)
        cssp.parse()

        newContent = ''
        for selector in cssp.selectors:
            newContent += selector.tag + '{'
            for counter, attr in enumerate(selector.body):
                newContent += attr + ':' + selector.body[attr]
                if counter < len(selector.body)-1: newContent += ';'
            newContent += '}'
        print(newContent)
        self._writeNewFile(newContent)

    def _writeNewFile(self, content):
        newFilename = self.filename[:-3] + 'min.css'
        with open(newFilename, 'w') as f:
            f.write(content)
            f.close()
        
    def _readFile(self):
        content = ''
        with open(self.filename, 'r') as f:
            content = f.read()
            f.close()
        
        return content

    
