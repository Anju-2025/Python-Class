class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # the iterator object itself

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Usage
my_iter = MyIterator(0, 5)
for num in my_iter:
    print(num)


def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# Usage
gen = my_generator(0, 5)
for num in gen:
    print(num)
