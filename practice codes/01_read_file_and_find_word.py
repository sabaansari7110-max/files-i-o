# Read the text from a given file "poems.txt" and find out whether it contaions the word "twinkle". 


st= "hello... twinkle twinkle little star.. but stars are cant be little"
f= open("poem.txt" , "a")
f.write(st)

with open("poem.txt" , "r") as f:
 c= f.read()
 if("twinkle"in c):
    print("twinkle is present in content")


 else:
    print("twinkle is not present in content")


f.close()

# First we make a empty "poem.txt" files. Then append the str in it .

f= open("poem.txt")
text= f.read()
print(text)
f.close
# we read a to check whats written in the file