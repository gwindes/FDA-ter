import random

from HTMLParser import HTMLParser
import requests
import re, string

class Translator(HTMLParser):
  api = "http://thesaurus.com/browse/"
  wordList = []
  pattern = re.compile('[\W]+')
  complexity = 2 #controls the complexity of the picked words from the api min=1 max=4?

  def __init__(self, parent=None):
    HTMLParser.__init__(self)

  def translate(self, text):
    text = self.pattern.sub(" ", text)
    text = text.split(" ")
    print "text = %s" % text
    translated = ""
    for word in text:
      translated += self.getWord(word) + " "
    translated = translated.rstrip()
    translated += "."

    return translated.capitalize()

  def getWord(self, src):
    if len(src) < 3:
      return src

    self.wordList = []
    self.parse(src)
    if len(self.wordList) > 0:
      maxRand = len(self.wordList)-1
      rand = random.randint(0, maxRand)
      return self.wordList[rand]
    else:
      return src

  def parse(self, src):
    r = requests.get(self.api + src)
    print "url = %s" % r.url
    data = r.content.split("\n")
    for line in data:
      self.feed(line)

  def handle_starttag(self, tag, attrs):
    for attr in attrs:
      if attr[0] == "class" and attr[1] == "common-word" and int(attrs[4][1]) >= 2:
        word = attrs[0][1].replace(self.api, "")
        complexity = int(attrs[4][1])
        print "word = %s \t complexity = %d" % (word, complexity)
        self.wordList.append(word)