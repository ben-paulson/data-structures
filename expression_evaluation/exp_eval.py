"""Evaluation of postfix expressions, conversion
of infix and prefix expressions to postfix expressions.
Author: Ben Paulson
"""

from stack_array import StackArray


class PostfixFormatException(Exception):
    pass


def check_postfix_format(tokens):
    """Verify that the format of the postfix expression is correct
    Argument:
        tokens (list): A list of strings of the tokens in the
                       postfix expression to be evaluated
    Raises:
        PostfixFormatException: If the format is incorrect. This may include
                                invalid tokens, too many operands, or too few
                                operands.
    """
    operator_options = "+-*/^"
    num_operands = 0
    num_operators = 0
    for token in tokens:        # Allow negatives
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            num_operands += 1
        elif token in operator_options:
            num_operators += 1
        else:
            raise PostfixFormatException("Invalid token")
    # Expected number of operands: num_operators + 1
    if num_operands < num_operators + 1:
        raise PostfixFormatException("Insufficient operands")
    if num_operands > num_operators + 1:
        raise PostfixFormatException("Too many operands")


def postfix_eval(input_str):
    """Evaluate a postfix (RPN) expression
    Arguments:
        input_str (str): The expression to evaluate, in string form,
                         with tokens separated by a single space
    Returns:
        int: The value of the postfix expression
    Raises:
        ValueError: if any divisor in the expression is zero
    """
    stack = StackArray()
    tokens = input_str.split(' ')
    check_postfix_format(tokens)
    for token in tokens:        # Handle negative numbers
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                stack.push(val2 + val1)
            elif token == '-':
                stack.push(val2 - val1)
            elif token == '*':
                stack.push(val2 * val1)
            elif token == '/':
                if val1 == 0:
                    raise ValueError("Cannot divide by zero")
                stack.push(val2 / val1)
            elif token == '^':
                stack.push(val2 ** val1)
    return stack.pop()


def infix_to_postfix(input_str):
    """Convert infix expressions to postfix expressions
    Arguments:
        input_str (str): The infix expression to convert, in string form,
                         with tokens separated by a single space
    Returns:
        str: The converted postfix expression
    """
    # format: {operator: (precedence, associativity)}
    operator_info = {'+': (0, 'left'),
                     '-': (0, 'left'),
                     '*': (1, 'left'),
                     '/': (1, 'left'),
                     '^': (2, 'right')}
    stack = StackArray()
    tokens = input_str.split(' ')
    postfix = ''
    for token in tokens:        # Handle negative numbers
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            postfix += ' ' + token
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while stack.peek() != '(':
                postfix += ' ' + stack.pop()
            stack.pop() # pop opening parenthesis
        else:
            next_operator = None if stack.is_empty() else stack.peek()
            if next_operator in operator_info:
                # Get precedence and associativity of this and next operator
                next_precedence = operator_info[next_operator][0]
                next_associativity = operator_info[next_operator][1]
                token_precedence = operator_info[token][0]
                token_associativity = operator_info[token][1]
                # Determine if next should be popped first or left alone
                pop_next = ((token_associativity == 'left' and
                           token_precedence <= next_precedence) or
                           (token_associativity == 'right' and
                           token_precedence < next_precedence))
                if pop_next:
                    postfix += ' ' + stack.pop()
            stack.push(token)
    while not stack.is_empty():
        postfix += ' ' + stack.pop()
    return postfix.strip() # Remove initial space added with first item


def prefix_to_postfix(input_str):
    """Convert prefix (PN) expressions to postfix (RPN) expressions
    Arguments:
        input_str (str): The prefix expression to convert, in string form,
                         with tokens separated by a single space
    Returns:
        str: The converted postfix expression
    """
    stack = StackArray()
    tokens = input_str.split(' ')[::-1] # reverse order, read right to left
    for token in tokens:        # Handle negative numbers
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(token)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(' '.join([op1, op2, token]))
    return stack.pop()
