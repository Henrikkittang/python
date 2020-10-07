import requests


class Element:
    def __init__(self, html_string):
        self.text = html_string

    def __repr__(self):
        return self.text

    def get(self, elem_prop):
        prop_idx = self.text.find(elem_prop)

        start_idx = self.text.find('"', prop_idx) + 1
        end_idx = self.text.find('"', start_idx)
 
        return self.text[start_idx:end_idx].split(' ')

    def tagType(self):
        start_idx = self.text.find('<', 0) + 1
        end_idx = self.text.find(' ', 0)

        return self.text[start_idx:end_idx]
 

class html_parser():
    def __init__(self, url):
        self.html = requests.get(url).text
        self.html = ' '.join(self.html.split())

    def find_elements(self, tag):
        start_tag = '<' + tag
        end_tag = '</' + tag + '>'

        html_elements = []
        string = self.html
        while string.find(start_tag) != -1:
            start_idx = string.find(start_tag)
            end_idx = string.find(end_tag, start_idx+len(start_tag))

            html_element = Element( string[start_idx:end_idx+len(end_tag)] )
            html_elements.append(html_element)
            string = string[end_idx:len(string)]  

        return html_elements
    
parser = html_parser('https://www.gettyimages.no/')
a = parser.find_elements('a')

for i in a:
    ye = i.tagType()
    print(ye)


