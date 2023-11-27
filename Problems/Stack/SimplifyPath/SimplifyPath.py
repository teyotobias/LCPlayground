

def simplifyPath(path):
    curr = ""
    stack = []
    for character in path:
        if character == '/':
            if curr == '..':
                if stack:
                    stack.pop()
            elif curr != "" and curr != ".":
                stack.append(curr)
            curr = ""
        else:
            curr += character

    if curr != "." and curr != "/" and curr != "" and curr != "..":
        stack.append(curr)
    elif curr == ".." and stack:
        stack.pop()
    return "/" + "/".join(stack)