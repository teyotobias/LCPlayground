# Runtime: 54 ms, faster than 81.06% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 16.2 MB, less than 91.16% of Python3 online submissions for Zigzag Conversion.
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    ret = [''] * numRows
    going_down = False
    currRow = 0
    for char in s:
        ret[currRow] += char
        if currRow == 0 or currRow == (numRows - 1):
            going_down = not going_down
        if going_down:
            currRow += 1
        else:
            currRow -= 1
    return ''.join(ret)
            