import unittest
from hashlib import sha256
from blockhain import hash, merkle_tree

class TestBlockchainFunctions(unittest.TestCase):


    def test_hash(self):
        self.assertEqual(
            hash("hello"),
            sha256("hello".encode('utf-8')).hexdigest()
        )
        self.assertEqual(
            hash("12345"),
            sha256("12345".encode('utf-8')).hexdigest()
        )


        self.assertNotEqual(
            hash("hello"),
            hash("world")
        )


    def test_merkle_tree(self):
        # Набор транзакций
        transactions = [
            hash("Alice pays Bob 10"),
            hash("Bob pays Charlie 5"),
            hash("Charlie pays Dave 2"),
            hash("Dave pays Eve 1")
        ]


        merkle_root = merkle_tree(transactions)
        self.assertIsInstance(merkle_root, str)
        self.assertEqual(len(merkle_root), 64)

        single_transaction = [hash("Alice pays Bob 10")]
        self.assertEqual(merkle_tree(single_transaction), single_transaction[0])

        transactions_odd = [
            hash("Alice pays Bob 10"),
            hash("Bob pays Charlie 5"),
            hash("Charlie pays Dave 2")
        ]
        merkle_root_odd = merkle_tree(transactions_odd)
        self.assertIsInstance(merkle_root_odd, str)
        self.assertEqual(len(merkle_root_odd), 64)

if __name__ == '__main__':
    unittest.main()
