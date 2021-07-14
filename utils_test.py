import unittest
import utils

class SignsTest(unittest.TestCase):

    def setUp(self):
        self.html = """
        <html><body>
        <main>
        <section></section>
        <section></section>
        <section>
        <div><div><div>
        <div></div>
            <div>
            <p><span>12345</span></p>
            </div>
        </div></div></div>
        </section>
        </main>
        </body>
        </html>
        """

    def test_signs_count(self):
        self.assertEqual(utils.get_signs_count(self.html), 12345)
