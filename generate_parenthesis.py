# Given n pairs of parentheses, write a function to
# generate all combinations of well-formed parentheses.
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

def generateParentheses(n: int):
    stack = []
    res = []

    # recursively
    def backtrack(openN, closedN):
        # valid IIF open ==  closed == n
        if openN == closedN == n:
            res.append("".join(stack))
            return
        # only add open p if open < n
        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closedN)
            stack.pop()
        # only add closed p if closed < open
        if closedN < openN:
            stack.append(')')
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generateParentheses(3))
