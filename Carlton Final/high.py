def update_score(score):
    f = open('highscore.txt','r')
    num = int(f.read())
    f.close()
    if score > num:
        f = open('highscore.txt','w')
        f.write(str(score))
        f.close()
        return "You beat the highscore "+str(num)+" with a score of "+str(score)
    else:
        return "Your score "+str(score)+ " didn't beat the highscore, "+str(num)

    
