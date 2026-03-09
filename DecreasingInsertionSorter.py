# MSCS532 Assignment 1
# Implementation of Insertion Sort (Descending Order)

class DecreasingInsertionSorter:

    def __init__(self, data):
        # Store a copy so the original list remains unchanged
        self.values = list(data)

    def sort_values(self):
        """
        Perform insertion sort in descending order.
        """

        position = 1

        # Traverse the list
        while position < len(self.values):

            current_item = self.values[position]
            check_index = position - 1

            # Shift smaller elements to the right
            while check_index >= 0:

                if self.values[check_index] < current_item:
                    self.values[check_index + 1] = self.values[check_index]
                    check_index -= 1
                else:
                    break

            # Insert the element at the correct location
            self.values[check_index + 1] = current_item
            position += 1

        return self.values


def display_list(label, data):
    """Utility function for displaying lists"""
    print(label)
    print(data)
    print()


def main():

    # Different dataset from the previous example
    sample_numbers = [14, 2, 9, 6, 21, 4, 11]

    display_list("Original Array:", sample_numbers)

    sorter = DecreasingInsertionSorter(sample_numbers)
    result = sorter.sort_values()

    display_list("Sorted Array (Monotonically Decreasing):", result)


if __name__ == "__main__":
    main()
