words="Many Many Happy Returns ."
word_split=words.split(" ")
word_count = {}
for word in word_split:
    word_count[word]=word_count.get(word,0) + 1
print(word_count)

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Traversing in 2D array row by row:")
for row in arr:
    for element in row:
        print(element,end=" ")
    print()