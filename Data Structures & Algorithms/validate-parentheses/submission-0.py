class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(",  "]" : "[", "}" : "{"} # pairs as a hash map
        for c in s: # go through characters as c
            if c in closeToOpen: #if its a closing parenthesis. stack[-1] means axcesinccessing the last item added to it
                if stack and stack[-1] == closeToOpen[c]: #if its the same as current position
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) #send current parenthesis to stack if its's an opening one
        return True if not stack else False #return true if it's empty

        