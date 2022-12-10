import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    # # ## OLD
    # # def test_email(self):
    # #     emp_1 = Employee('Malcolm', 'Abiad', 50000)
    # #     emp_2 = Employee('Sue', 'Smith', 60000)

    # #     self.assertEqual(emp_1.email, 'Malcolm.Abiad@email.com')
    # #     self.assertEqual(emp_2.email, 'Sue.Smith@email.com')


    # #     emp_1.first = 'John'
    # #     emp_2.first = 'Jane'

    # #     self.assertEqual(emp_1.email, 'John.Abiad@email.com')
    # #     self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    
    # # def test_fullname(self):
    # #     emp_1 = Employee('Malcolm', 'Abiad', 50000)
    # #     emp_2 = Employee('Sue', 'Smith', 60000)

    # #     self.assertEqual(emp_1.fullname, 'Malcolm Abiad')
    # #     self.assertEqual(emp_2.fullname, 'Sue Smith')

    # #     emp_1.first = 'John'
    # #     emp_2.first = 'Jane'

    # #     self.assertEqual(emp_1.fullname, 'John Abiad')
    # #     self.assertEqual(emp_2.fullname, 'Jane Smith')


    # # def test_apply_raise(self):
    # #     emp_1 = Employee('Malcolm', 'Abiad', 50000)
    # #     emp_2 = Employee('Sue', 'Smith', 60000)

    # #     emp_1.apply_raise()
    # #     emp_2.apply_raise()

    # #     self.assertEqual(emp_1.pay, 52500)
    # #     self.assertEqual(emp_2.pay, 63000)


    # ### Setup and Teardown methods - DRY method

    # ## Setup Method - Will run code before every single test
    # def setUp(self):
    #     self.emp_1 = Employee('Malcolm', 'Abiad', 50000)
    #     self.emp_2 = Employee('Sue', 'Smith', 60000)


    # ## Tear Down Method - Will run code after every single test
    # def tearDown(self):
    #     pass

    
    # def test_email(self):
    #     self.assertEqual(self.emp_1.email, 'Malcolm.Abiad@email.com')
    #     self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')


    #     self.emp_1.first = 'John'
    #     self.emp_2.first = 'Jane'

    #     self.assertEqual(self.emp_1.email, 'John.Abiad@email.com')
    #     self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    
    # def test_fullname(self):
    #     self.assertEqual(self.emp_1.fullname, 'Malcolm Abiad')
    #     self.assertEqual(self.emp_2.fullname, 'Sue Smith')

    #     self.emp_1.first = 'John'
    #     self.emp_2.first = 'Jane'

    #     self.assertEqual(self.emp_1.fullname, 'John Abiad')
    #     self.assertEqual(self.emp_2.fullname, 'Jane Smith')


    # def test_apply_raise(self):
    #     self.emp_1.apply_raise()
    #     self.emp_2.apply_raise()

    #     self.assertEqual(self.emp_1.pay, 52500)
    #     self.assertEqual(self.emp_2.pay, 63000)


    ### Setup and Teardown methods - With Print Statements

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    ## Setup Method - Will run code before every single test
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Malcolm', 'Abiad', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)


    ## Tear Down Method - Will run code after every single test
    def tearDown(self):
        print('tearDown\n')

    
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Malcolm.Abiad@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')


        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Abiad@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    
    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Malcolm Abiad')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Abiad')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')


    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    ## Mocking method
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:

            ## Test for Success
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Abiad/May')
            self.assertEqual(schedule, 'Success!')

            ## Test for Failure
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()