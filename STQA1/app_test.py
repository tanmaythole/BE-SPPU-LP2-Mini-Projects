import unittest
import app


class EmiTest(unittest.TestCase):

    def test_emi(self):

        self.assertEqual(app.calculate_emi(10000, 10, 2), 461.45)

        self.assertEqual(app.calculate_emi(20000, 15, 3), 693.31)

        self.assertEqual(app.calculate_emi(54236, 6.75, 4), 1292.47)

        self.assertEqual(app.calculate_emi(102548, 7.5, 5), 2054.85)

        self.assertEqual(app.calculate_emi(75980, 5.5, 3), 2294.28)

        self.assertEqual(app.calculate_emi(257360, 7.0, 4), 6162.81)




class FdTest(unittest.TestCase):

    def test_fd(self):

        self.assertEqual(app.calculate_fd(10000, 6.75, 2), 11395.56)
        
        self.assertEqual(app.calculate_fd(20000, 15, 3), 30417.5)

        self.assertEqual(app.calculate_fd(54236, 6.75, 4), 70430.24)

        self.assertEqual(app.calculate_fd(102548, 6.75, 2), 116859.21)

        self.assertEqual(app.calculate_fd(75980, 5.5, 2), 84567.64)

        self.assertEqual(app.calculate_fd(257360, 7.0, 2), 294651.46)




if __name__ == '__main__':
    unittest.main()