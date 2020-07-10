def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    # You have to code here!
    def nested_f(number):
        assert type(number) == int
        return number / n
    return nested_f

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3

if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):

        def setUp(self):
            self.testing_numbers = {
                6: (3,18),
                20: (5,100),
                3: (18,54),
                }

        def test_make_division_by(self):
            for key, value in self.testing_numbers.items():
                division_by_n = make_division_by(value[0])
                self.assertEqual(key, division_by_n(value[1]),
                'Please, check the closure "make_division_by(n)"')

        def tearDown(self):
            del(self.testing_numbers)

    run()
    unittest.main()