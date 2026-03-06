# List of bad words to be consered.

words = ["Donkey" ,"laila" , "bad"]

with open("problem.txt" , "r") as f:
    content= f.read()

for word in words:
    content= content.replace( word , "#" * len(word))


with open("problem.txt", "w") as f:
    f.write(content)