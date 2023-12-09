
def canConstruct(ransomNote, magazine):
    letMap = {}
    for i in range(len(magazine)):
        currLet = magazine[i]
        if currLet in letMap:
            letMap[currLet] += 1
        else:
            letMap[currLet] = 1
    for i in range(len(ransomNote)):
        currLet = ransomNote[i]
        if currLet in letMap:
            if letMap[currLet] == 1:
                del letMap[currLet]
            else:
                letMap[currLet] -= 1
        else:
            return False
    return True


