# Create a tableMult() method which creates and displays the multiplication table of a given integer.
# Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, …, 9.


class multTables():

    def __init__(self) -> None:
        pass

    def tableMult(self, num):

        table = []

        for i in range(1, 11):
            table.append(num * i)

        return table
    
    def allTableMult(self):
        pass

multTables_instance = multTables()