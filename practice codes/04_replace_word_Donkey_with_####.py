# file contains a word "Donkey" multiple times. You need to replace this word with #### by updating the same file.

#first make a file and write word donkey to replace

word = "Donkey"

with open("problem.txt" , "r") as f:
    content= f.read()


contentNew= content.replace( word , "####")


with open("problem.txt", "w") as f:
    f.write(contentNew)