def is_balanced(expression):
    # Initialize an empty stack
    stack = []

    # Define a dictionary for matching pairs
    matching_pairs = {')': '(', '}': '{', ']': '['}

    # Traverse through the expression
    for char in expression:
        if char in '({[':
            # Push opening symbols onto the stack
            stack.append(char)
        elif char in ')}]':
            # If the stack is empty or the top element doesn't match the corresponding opening symbol
            if not stack or stack[-1] != matching_pairs[char]:
                return "Not Balanced"
            stack.pop()  # Pop the matching opening symbol

    # Check if the stack is empty (all symbols were matched)
    if not stack:
        return "Balanced"
    else:
        return "Not Balanced"

# Test cases
expression1 = "{[()]}"
expression2 = "{[(])}"

print(f"Expression: {expression1} → {is_balanced(expression1)}")
print(f"Expression: {expression2} → {is_balanced(expression2)}")

