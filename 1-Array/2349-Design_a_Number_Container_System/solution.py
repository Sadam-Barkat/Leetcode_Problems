class NumberContainers:

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = {}  # Maps number -> sorted list of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                # Remove the old index
                self.number_to_indices[old_number].remove(index)
                if not self.number_to_indices[old_number]:  # If empty, delete the key
                    del self.number_to_indices[old_number]

        # Update the index mapping
        self.index_to_number[index] = number

        # Insert index into the correct position (maintaining sorted order)
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
        self._insert_sorted(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        # Return the smallest index or -1 if not found
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1

    def _insert_sorted(self, lst, value):
        """Binary insertion to keep the list sorted"""
        left, right = 0, len(lst)
        while left < right:
            mid = (left + right) // 2
            if lst[mid] < value:
                left = mid + 1
            else:
                right = mid
        lst.insert(left, value)
