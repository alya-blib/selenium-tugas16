import unittest
import category
import customer
import login
import registrasi

if __name__ == '__main__':

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    # suite.addTests(loader.loadTestsFromModule(First_Test))
    suite.addTests(loader.loadTestsFromModule(category))
    suite.addTests(loader.loadTestsFromModule(customer))
    suite.addTests(loader.loadTestsFromModule(login))
    suite.addTests(loader.loadTestsFromModule(registrasi))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

