
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    count_apples = 0
    count_oranges = 0
  
    for apple in apples:
        final_position_apple = apple + a
        if s <= final_position_apple <= t:
            count_apples += 1
    
    for orange in oranges:
        final_position_orange = orange + b
        if s <= final_position_orange <= t:
            count_oranges += 1

    print(count_apples)
    print(count_oranges)

s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]

countApplesAndOranges(s, t, a, b, apples, oranges)
