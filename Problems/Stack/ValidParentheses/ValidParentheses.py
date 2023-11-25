

def isValid(s):
    characters = {
            '(': ')',
            '{': '}',
            '[': ']'
    }
    stack = []
    for bracket in s:
        if bracket in characters:
            stack.append(bracket)
        else:
            if not stack or characters[stack.pop()] != bracket:
                return False
    return len(stack) == 0