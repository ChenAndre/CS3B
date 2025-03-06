import unittest

class MfrListTests(unittest.TestCase):
    def test_map(self):
        lst = MfrList([1, 2, 3])
        squared = lst.map(lambda x: x ** 2)
        self.assertEqual(squared, [1, 4, 9])
        self.assertIsInstance(squared, MfrList)
    
    def test_filter(self):
        lst = MfrList([1, 2, 3, 4])
        evens = lst.filter(lambda x: x % 2 == 0)
        self.assertEqual(evens, [2, 4])
        self.assertIsInstance(evens, MfrList)
    
    def test_reduce(self):
        lst = MfrList([1, 2, 3, 4])
        sum_result = lst.reduce(lambda a, b: a + b, 0)
        self.assertEqual(sum_result, 10)
        
        no_initial = lst.reduce(lambda a, b: a + b)
        self.assertEqual(no_initial, 10)
        
        single = MfrList([5])
        self.assertEqual(single.reduce(lambda a, b: a + b), 5)
        
        with self.assertRaises(TypeError):
            MfrList().reduce(lambda a, b: a + b)
        
        with_initial_empty = MfrList().reduce(lambda a, b: a + b, 100)
        self.assertEqual(with_initial_empty, 100)
    
    def test_iter(self):
        lst = MfrList([1, 2, 3])
        elements = []
        for e in lst:
            elements.append(e)
        self.assertEqual(elements, [1, 2, 3])
        
        it = iter(lst)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)
        with self.assertRaises(StopIteration):
            next(it)

class GlobalFunctionTests(unittest.TestCase):
    def test_capitalize(self):
        self.assertEqual(capitalize(MfrList([])), MfrList([]))
        self.assertEqual(capitalize(MfrList(["test"])), ["Test"])
        self.assertEqual(capitalize(MfrList(["apple", "banana"])), ["Apple", "Banana"])
    
    def test_between(self):
        lst = MfrList([5, 10, 15, 20])
        result = between(lst, 10, 20)
        self.assertEqual(result, [10, 15])
        self.assertEqual(between(MfrList([]), 0, 1), [])
        self.assertEqual(between(MfrList([10]), 10, 20), [10])
    
    def test_oldest(self):
        with self.assertRaises(TypeError):
            oldest(MfrList([]))
        self.assertEqual(oldest(MfrList([("John", 30)])), "John")
        people = MfrList([("John", 28), ("Mary", 30), ("Bob", 30)])
        self.assertEqual(oldest(people), "Mary")
    
    def test_join(self):
        self.assertEqual(join(MfrList([]), "-"), "")
        self.assertEqual(join(MfrList([1]), "-"), "1")
        self.assertEqual(join(MfrList([1, 2, 3]), "-"), "1-2-3")
        self.assertEqual(join(MfrList(["a", "b", "c"]), ""), "abc")
    
    def test_same(self):
        self.assertTrue(same(MfrList([])))
        self.assertTrue(same(MfrList([5])))
        self.assertTrue(same(MfrList([5, 5, 5])))
        self.assertFalse(same(MfrList([5, 6, 5])))
    
    def test_count_str(self):
        lst = MfrList(["Apple", "apple", "BANANA"])
        self.assertEqual(count_str(lst, "apple"), 2)
        self.assertEqual(count_str(MfrList([]), "apple"), 0)
        self.assertEqual(count_str(MfrList(["apple"]), "APPLE"), 1)
    
    def test_longest_palindrome(self):
        with self.assertRaises(Exception):
            longest_palindrome(MfrList([]))
        with self.assertRaises(Exception):
            longest_palindrome(MfrList(["hello", "world"]))
        lst = MfrList(["racecar", "noon", "madam", "hello"])
        self.assertEqual(longest_palindrome(lst), "racecar")
        lst2 = MfrList(["level", "stats", "radar"])
        self.assertEqual(longest_palindrome(lst2), "level")

if __name__ == '__main__':
    unittest.main()