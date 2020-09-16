def getLadder(num):
    numLadder = [i for i in str(num)]
    nums = []
    for i in range(len(numLadder)):
        nums.append(numLadder[i]+"0"*(len(numLadder)-1-i))
    return nums

def convert(num):
    ladders = getLadder(num)
    