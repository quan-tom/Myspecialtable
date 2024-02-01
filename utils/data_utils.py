# data_utils.py
from src.my_special_table import MySpecialTable

def special_data_table(number_of_slots, values, find_item):
    my_table = MySpecialTable(number_of_slots)
    for val in values:
        my_table.add_item(val)

    return my_table.find_item(find_item)
