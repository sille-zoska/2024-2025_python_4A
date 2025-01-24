class Time:
    def __init__(self, hours, minutes):
        """Konštruktor, ktorý berie hodiny a minúty."""
        if not (0 <= hours < 24):
            raise ValueError("Hodiny musia byť v rozsahu 0 až 23.")
        if not (0 <= minutes < 60):
            raise ValueError("Minúty musia byť v rozsahu 0 až 59.")
        self.__hours = hours
        self.__minutes = minutes

    def display(self):
        """Vypíše aktuálny čas vo formáte hh:mm."""
        print(self.getTime())

    def getTime(self):
        """Vracia čas vo formáte hh:mm."""
        return f"{self.__hours:02}:{self.__minutes:02}"

    def add(self, h, m):
        """Posunie čas o h hodín a m minút. Môžu to byť aj záporné hodnoty."""
        total_minutes = self.__hours * 60 + self.__minutes + h * 60 + m
        total_minutes = total_minutes % (24 * 60)  # Zaistíme, že čas bude v rámci 24 hodín

        self.__hours = total_minutes // 60
        self.__minutes = total_minutes % 60

# Globálna funkcia na vytvorenie novej inštancie Time
def createTime(time, h, m):
    """Vytvorí novú inštanciu Time posunutú o h hodín a m minút."""
    new_time = Time(time._Time__hours, time._Time__minutes)  # Prístup k privátnym atribútom
    new_time.add(h, m)
    return new_time

# Testovanie triedy Time
if __name__ == "__main__":
    t1 = Time(10, 30)
    t1.display()  # Vytlačí 10:30
    t1.add(2, 45)  # Posunie čas o 2 hodiny a 45 minút
    t1.display()  # Vytlačí 13:15

    t2 = createTime(t1, -3, 30)  # Vytvorí novú inštanciu posunutú o -3 hodiny a 30 minút
    t2.display()  # Vytlačí 09:45
