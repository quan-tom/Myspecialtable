class MySpecialTable:
    def __init__(self, slots):
        if slots == 0:
            raise ValueError("Number of slots cannot be 0.")

        self.slots = slots
        self.table = []
        self.create_table()

    def hash_key(self, value):
        # A simple hash function using modulo
        return hash(value) % self.slots

    def create_table(self):
        # Initialize an empty table with slots
        self.table = [[] for _ in range(self.slots)]

    def add_item(self, value):
        key = self.hash_key(value)
        self.table[key].append(value)

    def find_item(self, item):
        key = self.hash_key(item)
        slot = self.table[key]
        return item if item in slot else -1


def special_data_table(number_of_slots, values, find_item):
    myTable = MySpecialTable(number_of_slots)
    for val in values:
        myTable.add_item(val)

    return myTable.find_item(find_item)


# # Example usage:
# number_of_slots = 10
# values = [23, 45, 67, 89, 12]
# find_item = 67
#
# result = special_data_table(number_of_slots, values, find_item)
# print(result)
