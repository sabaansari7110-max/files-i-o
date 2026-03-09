# Find out whether a file is identical and matches the content of another file.

with open("problem.txt") as f:
    content1= f.read()

with open("copy_problem.txt") as f:
    content2= f.read()

if(content1== content2):
    print("yes, these files id identical")

else:
    print("no, thses files is not identical")