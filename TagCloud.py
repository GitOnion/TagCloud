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

def topWords (numWordsToKeep):
  global myTagWords
  myTagWords = sorted(myTagWords, key=operator.itemgetter(1), reverse=True)[0:numWordsToKeep]

def sizeWords (numSizes):
  global myTagWords
  numWordsPerSize = myTagWords[0][1] / numSizes
  for index,wordCount in enumerate(myTagWords):
    myTagWords[index] = (wordCount[0], wordCount[1] / numWordsPerSize)

def printWords (outputFile, numSizes):
  global myWordCounts
  file = open(outputFile, 'w')
  result = startPage(numSizes)
  for word,size in sorted(myWordCounts):
    result += formatWord(word, size)
  result += endPage()
  file.write(result)
  file.close()

if __name__ == "__main__":
  inputFile = sys.argv[1] if len(sys.argv) > 1 else 'speech.txt'
  countWords(inputFile)
