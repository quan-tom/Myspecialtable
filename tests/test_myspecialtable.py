# test_my_special_table.py
import unittest
import logging
from src.my_special_table import MySpecialTable
from utils.data_utils import special_data_table

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
tl = logging.FileHandler('Myspecialtabletest.log')
logger.addHandler(tl)

class TestMySpecialTable(unittest.TestCase):
    def test_special_data_table(self):
        # Test case for the special_data_table function

        # Test case 1: Non-zero slots
        number_of_slots = 5
        values = [10, 15, 20, 25, 30]
        find_item = 20

        my_table = MySpecialTable(number_of_slots)
        for val in values:
            my_table.add_item(val)

        result = special_data_table(number_of_slots, values, find_item)
        self.assertEqual(result, find_item, "Item should be found in the table")
        logger.info(f"Test case 'test_special_data_table' passed with result: {result}")

        # Test case 2: 0 slots (special case)
        number_of_slots_zero = 0
        values_zero_slots = [42, 56, 78]
        find_item_zero_slots = 56

        with self.assertRaises(ValueError) as context:
            MySpecialTable(number_of_slots_zero)

        self.assertEqual(
            str(context.exception),
            "Number of slots cannot be 0.",
            "Exception message should indicate that 0 slots are not allowed"
        )
        logger.info(f"Test case 'test_special_data_table' passed with exception: {context.exception}")

        # # Test case 3: too many parameters in MySpecialTable
        # number_of_slots = 5
        # values = [10, 15, 20, 25, 30]
        #
        # with self.assertWarns(UserWarning) as context:
        #     # Try to create MySpecialTable with too many parameters
        #     my_table = MySpecialTable(number_of_slots, *values)
        #
        # self.assertEqual(
        #     str(context.warning),
        #     "Too many parameters provided. MySpecialTable only accepts 'slots'.",
        #     "Warning message should indicate that too many parameters are provided."
        # )
        # logger.info("Test case 'test_too_many_parameters' passed with warning.")

    def test_add_item(self):
        # Test case for the add_item method

        number_of_slots = 5
        values = [10, 15, 20, 25, 30]
        item_to_add = 35

        my_table = MySpecialTable(number_of_slots)
        for val in values:
            my_table.add_item(val)

        my_table.add_item(item_to_add)

        self.assertIn(item_to_add, my_table.table[0], "Item should be added to the table")
        logger.info(f"Test case 'test_add_item' passed")

    def test_find_item(self):
        # Test case for the find_item method

        number_of_slots = 5
        values = [10, 15, 20, 25, 30]
        item_to_find = 20

        my_table = MySpecialTable(number_of_slots)
        for val in values:
            my_table.add_item(val)

        result = my_table.find_item(item_to_find)

        self.assertEqual(result, item_to_find, "Item should be found in the table")
        logger.info(f"Test case 'test_find_item' passed with result: {result}")

    def test_find_item_not_present(self):
        # Test case for the find_item method when the item is not present

        number_of_slots = 5
        values = [10, 15, 20, 25, 30]
        item_not_present = 40

        my_table = MySpecialTable(number_of_slots)
        for val in values:
            my_table.add_item(val)

        result = my_table.find_item(item_not_present)

        self.assertEqual(result, -1, "Item should not be found in the table")
        logger.info(f"Test case 'test_find_item_not_present' passed with result: {result}")

    def test_another_case(self):
        # Another test case
        self.assertEqual(1 + 1, 2, "1 + 1 should equal 2")
        logger.info(f"Test case 'test_another_case' passed")

if __name__ == '__main__':
    unittest.main()
