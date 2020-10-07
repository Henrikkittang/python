import os
import json
from git.repo.base import Repo

#dir, mkdir, gitClone, 


class Variable:
    def __init__(self):
        self.file = 'store.json'
            
    def resolveVars(self, args):
        for idx, variableName in enumerate(args, 0):
            if '$' in variableName:
                try:
                    with open(self.file, 'r') as file:
                        data = json.load(file)
                        value = data['variables'][variableName]
                        file.close()
                    args[idx] = value
                except KeyError:
                    print('variable' + "'" +  variableName + "'" + 'not found') 
                    return NULL
        return args

    def createVar(self, args):
        illegalChars = './'
        if args[0] in illegalChars or args[1] in illegalChars:
            print('Illegal character')
            return

        with open(self.file, 'r') as file:
            data = json.load(file)
            file.close()
        
        data['variables']['$' +  args[0]] = args[1]

        with open(self.file, 'w') as file:
            json.dump(data, file)
            file.close()

    def listVars(self, args):
        with open(self.file, 'r') as file:
            variables = json.load(file)['variables']
            for key in variables:
                print(key + ': ' + variables[key])
            file.close()

    def deleteVar(self, args):
        with open(self.file, 'r') as file:
            data = json.load(file)
            file.close()
    
        if data['variables'].pop('$' + args[0], None):
            with open(self.file, 'w') as file:
                json.dump(data, file)
                file.close()
        else:
            print('Key ' + "'" + args[0] + "'" + ' not found')
       

class Parser:
    def __init__(self):
        self.curDir = 'C:/Users/Henrik'
        self.variable = Variable()
        self.commands = {
            'nvar': self.variable.createVar,
            'lvar': self.variable.listVars,
            'dvar': self.variable.deleteVar,
            'raw': self.raw,
            'cd..': self.cdDD,
            'cd': self.cd,
            'dir': self.dirr,
            'mkdir': self.mkdir,
            'help': self.helpp,     
            'gclone': self.gclone
        }

    def parse(self, line):
        tokens = line.split(' ')
        command = tokens[0]
        args = self.variable.resolveVars(tokens[1:])

        try:
            self.commands[command](args)
        except KeyError:
            print('Command ' + "'" + command + "'" + ' not found')

    def raw(self, args):
        args = ' '.join(args)
        os.system(args)

    def cdDD(self, args):
        if self.curDir != 'C:':
            path = self.curDir.split('/')
            path.pop()
            self.curDir = '/'.join(path)

    def cd(self, args):
        path = args[0].split('/')
        starPath = self.curDir
        for p in path:
            folders = os.listdir(self.curDir)
            flag = False
            for folder in folders:
                if p == folder:
                    flag = True
                    break
            if flag:
                self.curDir += '/' + p
            else:
                self.curDir = starPath
                print('Path not found')
                break

    def dirr(self, args):
        for i in os.listdir(self.curDir):
            print(i)

    def mkdir(self, args):
        path = self.curDir + '/' + args[0]
        os.mkdir(path)

    def helpp(self, args):
        for key in self.commands:
            print(key)

    def gclone(self, args):
        Repo.clone_from(args[0], args[1])


parser = Parser()
while True:
    inputText = input(parser.curDir + '> ')
    
    if inputText == 'exit':
        exit()

    parser.parse(inputText)




