"""
CS3B, Assignment #2, RPN Calculator 
Andre Chen
Using knowledge of Stack to implement RPN Calculator utilizing infix notation(left to right easier for
computer to understand)
"""

import numpy 

class MyStack:
    # Constants
    MAX_CAPACITY = 100000
    DEFAULT_CAPACITY = 10

    # Initializer method
    def __init__(self, default_item, capacity=DEFAULT_CAPACITY):
        # If the capacity is bad, fail right away
        if not self.validate_capacity(capacity):
            raise ValueError("Capacity " + str(capacity) + " is invalid")
        self._capacity = capacity
        self._default_item = default_item

        # Make room in the stack and make sure it's empty to begin with
        self.clear()

    def clear(self):
        # Allocate storage the storage and initialize top of stack
        self._stack = numpy.full(self._capacity, self._default_item, dtype=type(self._default_item))
        self._top_of_stack = 0

    @classmethod
    def validate_capacity(cls, capacity):
        return 0 <= capacity <= cls.MAX_CAPACITY

    def push(self, item_to_push):
        if self.is_full():
            raise OverflowError("Push failed - capacity reached")
        
        #since numpy enforces types, checks are no longer needed
        #thus we have commented out the old type checking
        #elif type(item_to_push) != type(self._default_item):
            #raise TypeError("Push failed - wrong type for item")

        self._stack[self._top_of_stack] = item_to_push
        self._top_of_stack += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop failed - stack is empty")

        self._top_of_stack -= 1
        return self._stack[self._top_of_stack]

    def is_empty(self):
        return self._top_of_stack == 0

    def is_full(self):
        return self._top_of_stack == self._capacity

    def get_capacity(self):
        return self._capacity


        #i wonder if i can use self._stack and self._top_of_stack here since its not apart of 
        #'client code' per se
    def __str__(self):
        return f'MyStack(self.stack ={self._stack}, self.top_of_stack={self._top_of_stack})'
    

class RpnCalculator:
#class constants for our operators
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    FLOOR_DIVIDE = "//"

    @staticmethod
    #rpn_expression: a str of a single RPN expression to be evaluated, such as "2 3 +".
    def eval(rpn_expression):
        tokens = RpnCalculator.parse(rpn_expression)
        return RpnCalculator.eval_tokens(tokens)

    @staticmethod
    def parse(rpn_expression):
        return rpn_expression.split()
    
    @staticmethod
    #takes in a param "tokens": a list of str, e.g. ["2", "3", "+" ] that represents a parsed RPN expression
    def eval_tokens(tokens):
        capacity = len(tokens) *2 #little some overhead
        stack = MyStack(default_item = 0, capacity = capacity, dtype = int)

        '''
profs note: please use int() to figure out if a token (which can use any valid Python integer notation, 
        e.g. "1", "-1", "1_000") is an integer or not (remember, int() throws ValueError if a string is not a number), 
        not any of the str methods such as str.isdigit() (which doesn't work on negative numbers). 
        Please try to figure out the algorithm to evaluate the RPN expression using a stack.
        '''

        #ahh
        for token in tokens:
            try:
                stack.push(int(token))
            except ValueError:
                if token in (RpnCalculator.ADD, RpnCalculator.SUBTRACT, RpnCalculator.MULTIPLY, RpnCalculator.FLOOR_DIVIDE):
                    if stack.is_empty():
                        raise ValueError("Not enough operands for operation")
                    
                    operand2 = stack.pop()
                    
                    if stack.is_empty():
                        raise ValueError("INot enough operands for operation")
                    
                    operand1 = stack.pop()

                    if token == RpnCalculator.ADD:
                        result = operand1 + operand2
                    elif token == RpnCalculator.SUBTRACT:
                        result = operand1 - operand2
                    elif token == RpnCalculator.MULTIPLY:
                        result = RpnCalculator.multiply(operand1, operand2)
                    elif token == RpnCalculator.FLOOR_DIVIDE:
                        result = operand1 // operand2
                    else:
                        raise ValueError(f"Unrecognized operator: {token}")
                    
                    stack.push(result)
                else:
                    raise ValueError(f"Unrecognized token: {token}")

        if stack.is_empty() or stack.get_capacity() != 1:
            raise ValueError("Invalid RPN expression")

        return stack.pop()

    @staticmethod
    def multiply(a, b):
        # base case: when b is 0, the product is 0
        if b == 0:
            return 0
        elif b > 0:
            return a + RpnCalculator.multiply(a, b - 1)
        else:  # when b is less than 0
            return -RpnCalculator.multiply(a, -b)



#lost functionalities since we are using the the numpy instead of built in list ai yaa
def demo_lost_functionalities():
    #no more dynamic resizing since numpy arrays are fixed size once set
    #no mixed data types, only a single data type per numpy array
    #more operations 

    try:
        # demonstrating dynamic resizing issue
        stack = MyStack(-1, 3)  # A small capacity to illustrate the issue
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # attempting to push more items will raise an OverflowError due to fixed size
        stack.push(4)
    except OverflowError as e:
        print(f"Dynamic resizing issue: {e}")

    try:
        # demonstrating mixed data types issue
        stack = MyStack(-1, 5)
        stack.push(1)
        stack.push("string")  # Attempting to push a different data type
    except TypeError as e:
        print(f"Mixed data types issue: {e}")

            #proof of the lost functionalities in action
demo_lost_functionalities()


def test_rpn():
    expressions = [
        # valid expressions
        "3",              # single number
        "2 3 +",          # addition
        "2 3 -",          # subtraction
        "2 3 *",          # multiplication
        "6 3 //",         # floor division
        "2 3 4 + *",      # multiple operations
        "5 1 2 + 4 * + 3 -", # complex expression
        "4 2 + 3 * 10 2 // -", # another complex expression
        
        # invalid expressions
        "",               # empty string
        "1 +",            # insufficient operands
        "1 1",            # insufficient operator
        "1 1 fly",        # invalid operator
        "random junk",    # completely invalid
        "1 1 + +",        # too many operators
        "1 1 + 2 /",      # division with no operator
    ]

    for expr in expressions:
        try:
            result = RpnCalculator.eval(expr)
            print(f'"{expr}" = {result}')
        except Exception as e:
            print(f'"{expr}" fails to be evaluated: {e}')
test_rpn()


#Given by professor, no need to change to pass
def mystack_test():
    # Instantiate two empty stacks, one of 50 ints, another of 10 strings
    s1 = MyStack(-1, 50)
    s2 = MyStack("undefined")
    # and one more with bad argument
    try:
        s3 = MyStack(None, -100)
        print("Failed test: expected __init()__ to reject negative capcity but it didn't")
    except Exception as e:
        print("Successful test: handled negative capacity: " + str(e))

    # Confirm the stack capacities
    print("------ Stack Sizes -------\n  s1: {}   s2: {}\n".
          format(s1.get_capacity(), s2.get_capacity()))

    # Pop empty stack
    print("------ Test stack ------\n")
    try:
        s1.pop()
        print("Failed test: expected pop() to raise empty-stack exception but it didn't")
    except Exception as e:
        print("Successful test: handled popping empty s1: " + str(e))

    # Push some items
    s1.push(44)
    s1.push(123)
    s1.push(99)
    s1.push(10)
    s1.push(1000)
    # try to put a square peg into a round hole
    try:
        s1.push("should not be allowed into an int stack")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s2.push(444)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s1.push(44.4)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    # Push to s2
    s2.push("bank")
    s2.push("-34")
    s2.push("should be okay")
    s2.push("a penny earned")
    s2.push("item #9277")
    s2.push("where am i?")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    try:
        s2.push("This is when stack is full")
        print("Failed test: expected push() to throw exception but it didn't")
    except Exception as e:
        print("Successful test: handled pushing when stack is full: " + str(e))
    print("\n--------- First Stack ---------\n")

    # Pop and inspect the items
    for k in range(0, 10):
        try:
            print("[" + str(s1.pop()) + "]")
        except Exception as e:
            print("Successful test: handled popping empty stack s1: " + str(e))
    print("\n--------- Second Stack ---------\n")
    for k in range(0, 10):
        print("[" + str(s2.pop()) + "]")


if __name__ == "__main__":
    mystack_test()

