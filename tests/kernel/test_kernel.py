from app.kernel.kernel import Kernel
import app.storage
import unittest


class TestRoutes(unittest.TestCase):


    def test_init_kernel(self):
        self.kernel = Kernel(123)
        self.assertEqual(self.kernel.kernel_id, 123)
        self.assertEqual(self.kernel.threshold, Kernel.DEFAULT_THRESHOLD)
        print(app.storage.client)

    def test_ready_to_predict(self):
        app.storage.data_amount = lambda x: 11
        self.kernel = Kernel(123)
        self.assertTrue(self.kernel.ready_to_predict())


if __name__ == '__main__':
    unittest.main()
