# A file name log.txt and find out whether it contaion word "python"

with open("log.txt" , "r") as f:
    content= f.read()


if("python" in content):
    print("yes, python is present")

else:
    print("no, python is not present")