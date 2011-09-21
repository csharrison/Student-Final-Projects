#the colission program that i am using
def collide(d, x,y,lisst):
    for c in lisst:
        if d == 1 and c.x != x and c.y != y:
            if abs(x + 28 -(c.x+7)) <3 and abs(y+5 -(c.y+14)) < 32 and c.d !=3:
                return True
        if d == 2 and c.x != x and c.y != y:
            if abs(y + 28 -(c.y+7)) <3 and abs(x+5 -(c.x+14)) < 32 and c.d !=4:
                return True
        if d == 3 and c.x != x and c.y != y:
            if abs(x -(c.x+3)) <3 and abs(y+5 -(c.y+14)) < 32 and c.d != 1:
                return True
        if d == 4 and c.x != x and c.y != y:
            if abs(y -(c.y+3)) <3 and abs(x+5 -(c.x+14)) < 32 and c.d !=2:
                return True
