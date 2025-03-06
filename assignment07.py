class MfrList(list):

    """A class that's a Python list with map(), filter(), reduce() added"""
    
    @staticmethod
    def validate_func(func):
        """Validate func is callable, raises TypeError if not"""
        if not callable(func):
            raise TypeError(f"'{type(func)}' is not callable")
    
    def map(self, func):
        """Applies func to each element, returns a new MfrList"""
        self.validate_func(func)
        return MfrList([func(e) for e in self])
    
    def filter(self, func):   #impleement ts
        """Filters elements based on func, returns a new MfrList"""
        self.validate_func(func)
        return MfrList([e for e in self if func(e)])
    
    def reduce(self, func, initial=None): #implement ts
        """Reduces the list to a single value using func and optional initial value"""
        self.validate_func(func)
        if initial is None:
            if len(self) == 0:
                raise TypeError("reduce() of empty sequence with no initial value")
            elif len(self) == 1:
                return self[0]
            result = self[0]
            start_index = 1
        else:
            result = initial
            start_index = 0
        
        for element in self[start_index:]:
            result = func(result, element)
        
        return result
    
    def __iter__(self):
        return MfrListIterator(self)


class MfrListIterator:
    def __init__(self, mfr_list):
        self.mfr_list = mfr_list
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.mfr_list):
            value = self.mfr_list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self


def capitalize(mfrlist):
    return mfrlist.map(lambda s: s.capitalize())


def between(mfrlist, inclusive_start, exclusive_end):
    return mfrlist.filter(lambda x: inclusive_start <= x < exclusive_end)


def oldest(mfrlist):
    return mfrlist.reduce(lambda a, b: b if b[1] > a[1] else a)[0]


def join(mfrlist, sep):
    return mfrlist.reduce(lambda a, e: f"{a}{sep}{e}" if a else str(e), initial="")


def same(mfrlist):
    return mfrlist.reduce(
        lambda acc, elem: (
            (True if acc[1] is None else acc[0] and (elem == acc[1])),
            (elem if acc[1] is None else acc[1])
        ),
        initial=(True, None)
    )[0]


def count_str(mfrlist, key):
    key_lower = key.lower()
    return mfrlist.map(lambda s: s.lower() == key_lower).reduce(lambda a, b: a + b, 0)


def longest_palindrome(mfrlist):
    palindromes = mfrlist.filter(lambda s: s == s[::-1])
    return palindromes.reduce(lambda a, b: a if len(a) >= len(b) else b)


# Sample functions provided in the starter code from prof
def square(mfrlist):
    return mfrlist.map(lambda x: x ** 2)


def odds(mfrlist):
    return mfrlist.filter(lambda x: x % 2 == 1)


def add_all(mfrlist):
    return mfrlist.reduce(lambda a, b: a + b, 0)


def sum_of_squares(mfrlist):
    return mfrlist.map(lambda x: x ** 2).reduce(lambda a, b: a + b, 0)


def is_in(mfrlist, key):
    return mfrlist.map(lambda e: e == key).reduce(lambda a, b: a or b, False)


def test():
    """Sample usage from prof"""
    mfrlist = MfrList([12, 98, 53])
    print(f"square({mfrlist}) => {square(mfrlist)}")
    print(f"add_all({mfrlist}) => {add_all(mfrlist)}")
    print(f"odds({mfrlist}) => {odds(mfrlist)}")
    
    # Additional tests
    print("\nAdditional Tests:")
    names = MfrList([("John", 28), ("Mary", 30), ("Bob", 30)])
    print(f"Oldest: {oldest(names)}")  # get Mary
    
    numbers = MfrList([5, 10, 15, 20])
    print(f"Between 10 and 20: {between(numbers, 10, 20)}")  # get [10, 15]
    
    words = MfrList(["apple", "banana", "cherry"])
    print(f"Capitalize: {capitalize(words)}")  # get ['Apple', 'Banana', 'Cherry']
    
    joined = join(MfrList([1, 2, 3]), "-")
    print(f"Joined: {joined}")  # get "1-2-3"
    
    same_test1 = MfrList([5, 5, 5])
    same_test2 = MfrList([5, 6, 5])
    print(f"All same test1: {same(same_test1)}")  # shud be True
    print(f"All same test2: {same(same_test2)}")  # False
    
    count_test = MfrList(["Apple", "apple", "APPLE"])
    print(f"Count 'apple': {count_str(count_test, 'apple')}")  # 3
    
    palindromes = MfrList(["racecar", "noon", "madam", "hello"])
    print(f"Longest palindrome: {longest_palindrome(palindromes)}")  # racecar


if __name__ == '__main__':
    test()