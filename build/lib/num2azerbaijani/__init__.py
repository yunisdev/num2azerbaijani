from .nums import numsDict


def getLadder(num):
    parts = divide_to_parts(str(num))
    result = []
    for part in parts:
        numLadder = [i for i in part]
        nums = []
        for i in range(len(numLadder)):
            if numLadder[i] != "0":
                nums.append(numLadder[i]+"0"*(len(numLadder)-1-i))
        result.append(nums)
    return result


def divide_to_parts(num):
    parts = []
    left = len(num) % 3
    if len(num[:left]) > 0:
        parts.append(num[:left])
    j = 0
    temp = ""
    for i in num[left:]:
        temp += i
        if j % 3 == 2:
            parts.append(temp)
            temp = ""
        j += 1
    return parts


def complect_ladder(ladder):
    result = []
    for i in ladder:
        temp = []
        for j in i:
            t = numsDict.get(j)
            if len(j) == 3 and numsDict.get(j[0]) != 'bir':
                t = numsDict.get(j[0])+" yüz"
            elif len(j) == 3:
                t = 'yüz'
            temp.append(t)
        result.append(" ".join(temp))
    return result


def convert(num):
    try:
        num = int(num)
        cl = complect_ladder(getLadder(num))
        result = ""
        for i in range(len(cl)):
            if (len(cl)-1-i) > 0:
                if not cl[i] == "":
                    if cl[i] == 'bir' and (len(cl)-1-i) == 1:
                        result += numsDict.get('x'*(len(cl)-1-i)) + " "
                    else:
                        result += cl[i] + " " + \
                            numsDict.get('x'*(len(cl)-1-i)) + " "
            else:
                result += cl[i] + " "
        return result
    except ValueError:
        raise ValueError('Please enter valid integer')
