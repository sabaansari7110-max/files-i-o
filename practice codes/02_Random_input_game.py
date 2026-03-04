import random

def game():
    print("you are playing the game....")
    score= random.randint(1, 100)

    
    print(f"yourscore: {score}")
   
    try:
        with open("myfile" , "r") as f:
            data= f.read.strip()
            if data == "":
                hiscore= 0
           
            else:
                hiscore= int(data)
    except(FileNotFoundError, ValueError):
        hiscore= 0

    if score > hiscore:
        print("NEW HIGH SCORE")
        with open("myfile.txt", "w") as f:
             f.write(str(score))
        
    else:
        print("BETTER LUCk NEXT TIME")

            
game()

    
