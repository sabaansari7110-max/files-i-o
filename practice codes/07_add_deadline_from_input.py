# Deadline tracking example (mini project)

task= input("enter task: ")
deadline= input("enter deadline (DD-MM-YYYY): ")


with open("problem.txt" , "a") as f:
    f.write(f"\n{task} | {deadline}\n")