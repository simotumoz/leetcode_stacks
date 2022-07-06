# # Given an array of integers temperatures
# # represents the daily temperatures, return an array answer
# # such that answer[i] is the number of days you have to wait
# # after the ith day to get a warmer temperature.
# # If there is no future day for which this is possible,
# # keep answer[i] == 0 instead.
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)  # initialize result array to zeros
    stack = []  # pair : [temp, index]

    for i, t, in enumerate(temperatures):
        while stack and t > stack[-1][0]:  # checking if t > top of the stack
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])  # appending pair temp, index to the stack
    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))
