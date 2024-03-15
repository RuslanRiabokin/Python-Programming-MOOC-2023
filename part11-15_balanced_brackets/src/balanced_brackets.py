def balanced_brackets(my_string: str):
    def is_valid_bracket(char):
        return char in '()[]'

    def is_matching_pair(opening, closing):
        return (opening == '(' and closing == ')') or (opening == '[' and closing == ']')

    def is_balanced_helper(sub_string):
        stack = []
        for char in sub_string:
            if not is_valid_bracket(char):
                continue
            if char in '([':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not is_matching_pair(top, char):
                    return False
        return not stack

    # Call is_balanced_helper recursively on each substring
    def balanced_brackets_recursive(my_string):
        if len(my_string) == 0:
            return True
        for i in range(len(my_string)):
            if is_valid_bracket(my_string[i]):
                if is_balanced_helper(my_string[:i+1]) and balanced_brackets_recursive(my_string[i+1:]):
                    return True
        return False

    return balanced_brackets_recursive(my_string)