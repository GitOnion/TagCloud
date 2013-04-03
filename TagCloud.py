myCommonWords = []
myWordCounts = {}

def init (ignoreWords):
  file = open(ignoreWords, 'r')
  myCommonWords = file.read().split()
  file.close()

def countWords (input):
  file = open(input, 'r')
  for word in file.read().split():
    word = removePuncuation(word.lower())
    if isTaggableWord(word):
      myWordCounts[word] = myWordCounts.get(word, 0) + 1
  file.close()

def printWords (outputFile, numSizes):
  global myTagWords
  file = open(outputFile, 'w')
  result = startPage(numSizes)
  for word,size in sorted(myTagWords):
    result += formatWord(word, size)
  result += endPage()
  file.write(result)
  file.close()

if __name__ == "__main__":
  inputFile = sys.argv[1] if len(sys.argv) > 1 else 'speech.txt'
  countWords(inputFile)
