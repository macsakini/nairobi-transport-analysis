import string
import re
class Preprocess():
    def __init__(self, string):
        self.string = string

    def lowercase(self):
        return self.string.lower()

    def remove_punctuations(self):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
        q = re.sub(r'[^\w\s]', '', self.lowercase())
        return q.replace(" ", "")
        

    def check_slash(self):
        pass

    def check_match_percentage(self):
        pass

    def call(self):
        return self.remove_punctuations()

print(Preprocess("I am am MAN").call())