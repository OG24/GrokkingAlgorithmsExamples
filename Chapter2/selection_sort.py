import random


class SelectionSort:
    def __init__(self, array_size):
        self.array_size = array_size
        self.numbers = list()
        self.sorted_number = list()

    def create_list(self):
        for i in range(self.array_size):
            self.numbers.append(random.randint(0, 1000))

    def sort(self):
        copy_list = list(self.numbers)
        for i in range(len(self.numbers)):
            local_min_index = 0

            for j in range(len(copy_list)):
                if copy_list[j] <= copy_list[local_min_index]:
                    local_min_index = j
            self.sorted_number.append(copy_list[local_min_index])
            copy_list.pop(local_min_index)


if __name__ == "__main__":
    selection_sort = SelectionSort(100)
    selection_sort.create_list()

    selection_sort.sort()
    print(selection_sort.sorted_number)
