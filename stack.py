# Implement a function is_balanced(expression) that takes a string 
# containing parentheses, curly braces, and square brackets,and determines whether 
# the expression is balanced. 

# An expression is considered balanced if each opening bracket has a corresponding closing 
# bracket in the correct order.

# sample input = 

# expression1 = "([]{})"
# expression2 = "([)]"
# print(is_balanced(expression1))  # Output: True
# print(is_balanced(expression2))  # Output: False

def is_balanced(str):
    stack = []  #  empty stack to keep track of opening brackets
    
    #a mapping of opening brackets to their corresponding closing brackets
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    
    # Iterating through each character in the expression
    for char in str:
        # If the character is an opening bracket, pushing it onto the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing bracket
        elif char in ')}]':
            # Check if the stack is empty or if the top of the stack does not match
            # the expected opening bracket for the current closing bracket
            if not stack or stack.pop() != bracket_mapping[char]:
                return False  # Expression is not balanced
    
    # If the stack is empty at the end, the expression is balanced
    return not stack

print(is_balanced("([]{})") ) # Output: True
print(is_balanced("([)]")) 
