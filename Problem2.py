# Problems 2 : Remove all the continuous character
# Time Complexity: O(n),Each character is pushed at most once and popped at most once Rebuilding the result adds at most n characters in total. Reverse and join are O(n).
# Space Complexity: O(n), Worst case (no removals, like "abcd"): both stacks hold n items and result also holds up to n characters.
# Approach:
# Use two stacks that always stay the same size.
#   stack     -> stores the characters
#   num_stack -> stores how many times that character repeats in a row
# For each new character: If it matches the top character, add 1 to the top count. If the count reaches k, remove that group (pop both stacks). Otherwise, save the updated count back.
# If it is different (or the stack is empty), start a new group with count 1.
# When a group is removed, the older group below becomes the top,
# so the next character can join it. This handles chain removals.
# At the end, rebuild the string from what is left in the stacks.


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []      # characters of the groups that are still alive
        num_stack = []  # num_stack[i] = run length of stack[i]

        for char in s:  # look at each character once, left to right
            if stack and stack[-1] == char:  # stack not empty AND same as top character
                freq = num_stack.pop()  # take out the current run length of the top group
                freq += 1               # one more copy of this character
                if freq == k:           # the group reached size k
                    stack.pop()         # delete the group (count is already popped)
                else:                   # group is still smaller than k
                    num_stack.append(freq)  # put the updated count back
            else:  # stack is empty OR top character is different
                stack.append(char)      # start a new group with this character
                num_stack.append(1)     # its run length is 1

        result = []  # will hold the final characters (built backwards)

        while stack:  # repeat until every group is used
            char = stack.pop()         # top character (last group)
            count = num_stack.pop()    # its run length
            for i in range(count):     # write the character 'count' times
                result.append(char)

        return "".join(result[::-1])  # reverse (we built it backwards), then join into a string