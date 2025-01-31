class ShopCart:
    def __init__(self):
        # Inicializácia prázdneho zoznamu pre položky v košíku
        self.items = []

    def addItem(self, name, price):
        # Pridanie položky do zoznamu
        self.items.append({"name": name, "price": price})

    def removeItem(self, name):
        # Odstránenie položky na základe názvu
        self.items = [item for item in self.items if item["name"] != name]

    def printContent(self):
        # Výpis obsahu košíka a celkovej hodnoty
        if not self.items:
            print("Košík je prázdny.")
        else:
            total = 0
            print("Položky v košíku:")
            for item in self.items:
                print(f"{item['name']} - {item['price']} EUR")
                total += item["price"]
            print(f"Celková hodnota: {total} EUR")

# Testovanie
cart = ShopCart()
cart.addItem("Kniha", 15.50)
cart.addItem("Pero", 1.20)
cart.printContent()
cart.removeItem("Pero")
cart.printContent()
