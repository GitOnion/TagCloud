myCommonWords = []
myWordCounts = {}

def init (ignoreWords):
  file = open(ignoreWords, 'r')
  myCommonWords = file.read().split()
  file.close()

