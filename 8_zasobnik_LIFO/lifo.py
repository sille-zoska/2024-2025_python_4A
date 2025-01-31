class Zasobnik:
    def __init__(self):
        self.__items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.__items.append(item)

    def pop(self):
        """
        Pop the top item off the stack and return it.
        Returns None if the stack is empty.
        """
        if self.isEmpty():
            return None
        return self.__items.pop()

    def display(self):
        """Display the contents of the stack from top to bottom."""
        if self.isEmpty():
            print("Zásobník je prázdny.")
        else:
            print("Zásobník (vrch -> spodok):")
            # The last element in the list is the top of the stack
            for item in reversed(self.__items):
                print(item)

    def isEmpty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.__items) == 0

    def __len__(self):
        """
        Return the number of items in the stack.
        This allows using len() function on the instance, e.g. len(z).
        """
        return len(self.__items)

if __name__ == "__main__":
    # Quick test
    z = Zasobnik()
    z.push("jablko")
    z.push("hruska")
    z.push("jahoda")
    z.display()
    print("Počet prvkov v zásobníku:", len(z))

    popped_item = z.pop()
    print(f"Vybral som: {popped_item}")
    z.display()

    popped_item = z.pop()
    popped_item = z.pop()
    popped_item = z.pop()  # Another pop on empty stack => None
    if popped_item is None:
        print("Zásobník je už prázdny.")
    z.display()
