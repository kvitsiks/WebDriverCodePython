import unittest

from Tests.ForLoopExampleTest import ForLoopExampleTest
from Tests.ValidLoginTest import ValidLoginTest


def suite():
    my_suite = unittest.TestSuite()

    my_suite.addTest(ValidLoginTest("test valid login"))
    my_suite.addTest(ForLoopExampleTest("test_operator"))

    return my_suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
    # unittest.main()
