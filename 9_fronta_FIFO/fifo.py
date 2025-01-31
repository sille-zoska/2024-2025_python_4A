class Fronta:
    def __init__(self):
        # Internal list to store items
        self.__items = []

    def push(self, item):
        """
        Add (enqueue) the item at the end of the queue.
        """
        self.__items.append(item)

    def pop(self):
        """
        Remove (dequeue) and return the front item from the queue.
        Returns None if the queue is empty.
        """
        if len(self.__items) == 0:
            return None
        return self.__items.pop(0)

    def display(self):
        """
        Display the current state of the queue (all elements from front to back).
        """
        if not self.__items:
            print("Fronta je prázdna.")
        else:
            print("Fronta (od najstaršieho k najnovšiemu):")
            for item in self.__items:
                print(item)

if __name__ == "__main__":
    # Quick test
    f = Fronta()
    f.push("jablko")
    f.push("hruska")
    f.push("jahoda")

    f.display()
    # Pop one item from the front
    item = f.pop()
    print(f"Odstránený prvok: {item}")
    f.display()

    # Pop the rest
    item = f.pop()
    item = f.pop()
    # Attempt one more pop
    item = f.pop()
    if item is None:
        print("Fronta je už prázdna.")
    f.display()
# end


