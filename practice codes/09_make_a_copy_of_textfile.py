# Makeing a copy of a text file (this.txt)"problem.txt".

with open("problem.txt") as f:
    content= f.read()


with open("copy_problem.txt" , "w") as f:
    f.write(content)