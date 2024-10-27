
class StepValueError(ValueError):
    pass



class Iterator:
    def __init__(self, start, stop, step=1):

        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):

        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        current_value = self.pointer
        self.pointer += self.step
        return current_value



if __name__ == "__main__":

    iterator1 = Iterator(0, 10, 2)
    iterator2 = Iterator(10, 0, -2)

    print("Итерация iterator1:")
    for value in iterator1:
        print(value)

    print("\nИтерация iterator2:")
    for value in iterator2:
        print(value)