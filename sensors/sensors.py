def read_sensor_data(file_name):
    try:
        with open(file_name, 'r') as file:
            # Načíta hodnoty zo súboru do zoznamu
            data = [int(line.strip()) for line in file]
        
        # Skontrolujeme, či sú nejaké hodnoty v súbore
        if len(data) == 0:
            print("Súbor je prázdny.")
            return

        # Vypočítame maximálnu, minimálnu hodnotu a priemer
        max_value = max(data)
        min_value = min(data)
        avg_value = sum(data) / len(data)
        
        # Vytlačíme výsledky
        print(f"Maximálna hodnota: {max_value}")
        print(f"Minimálna hodnota: {min_value}")
        print(f"Priemer hodnôt: {avg_value:.2f}")

    except FileNotFoundError:
        print(f"Súbor {file_name} neexistuje.")
    except ValueError:
        print("Súbor obsahuje neplatné dáta. Každý riadok musí obsahovať celé číslo.")

# Načítanie názvu súboru a spustenie programu
file_name = input("Zadajte názov súboru: ")
read_sensor_data(file_name)
