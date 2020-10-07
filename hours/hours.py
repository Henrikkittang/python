import json


def getTime(interval):
    hours = interval.split(':')
    point = float(hours[0])
    point += float(hours[1]) * 0.0167
    return point

def parseString(string):
    string.join(string.split())
    intervals = string.split('-')
    time1 = getTime(intervals[0])
    time2 = getTime(intervals[1])
    return (time1, time2)

def readJsonFile(filename):
    with open(filename + '.json', 'r', encoding="UTF-8") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    return data

def writeTextFile(filename, content):
    with open(filename + '.txt', 'a+', encoding="UTF-8") as textFile:
        textFile.write(content + '\n')
        textFile.close()

def emptyTextFile(filename):
    with open(filename + '.txt', 'w') as textFile:
        textFile.write('')    
        textFile.close()

emptyTextFile('hours')
file = readJsonFile('hours')

totalWage = 0
totalHours = 0

for time in file['hours']:
    interval = parseString(time['timeStart'] + "-" + time['timeEnd'])
    hours = round(interval[1] - interval[0], 3)
    if time.get('bonus'):
        wage = hours * (file['hourlyWage'] + time['bonus'])
        bonus = ' inkludert bonus'
    elif time.get('holiday'):
        wage = hours * (file['hourlyWage'] * 1.4)
        bonus = ' helligdag'
    else:
        wage = hours * file['hourlyWage']
        bonus = ''

    wage = round(wage, 2)
    totalWage += wage
    totalHours += hours

    content =  'Dato: ' + time['date'] + ', '
    content += 'Tidspunkt: ' + time['timeStart'] + "-" + time['timeEnd'] + ', '
    content += 'Antall timer: ' + str(hours) + ', '
    content += 'Lønn: ' + str(wage) + 'kr' + bonus

    writeTextFile('hours', content)

writeTextFile('hours', '')

for time in file['extra']:
    content =  'Dato: ' + time['date'] + ', '
    content += 'Beskrivelse: ' + time['desricption'] + ', '
    content += 'Antall timer: ' + str(time['lengthInHours']) + ', '
    content += 'Lønn: ' + str(time['lengthInHours'] * file['hourlyWage']) + 'kr'

    totalWage += time['lengthInHours'] * file['hourlyWage']
    totalHours += time['lengthInHours']

    writeTextFile('hours', content)

writeTextFile('hours', '')
totalHours = round(totalHours, 2)
totalWage = round(totalWage, 2)

content = 'Totalt antall timer: ' + str(totalHours) + ', '
content += 'Total lønn: ' + str(totalWage) + 'kr' + ' medregnet bonus og helligdager'
writeTextFile('hours', content)








