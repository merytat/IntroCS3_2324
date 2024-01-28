word = input("Enter a word")
middleIndex = len(word)//2
initialIndex = middleIndex-1
endingIndex = middleIndex+2
middle = word[initialIndex:endingIndex]

middle = word[((len(word)//2)-1):((len(word)//2)+2)]
print("Middle Letters: ", middle)