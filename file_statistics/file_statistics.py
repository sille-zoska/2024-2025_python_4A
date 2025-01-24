def file_statistics(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Počet riadkov
        num_lines = len(lines)

        # Počet slov
        num_words = sum(len(line.split()) for line in lines)

        # Počet znakov
        num_chars = sum(len(line) for line in lines)

        # Vytlačíme výsledky
        print(f"Počet riadkov: {num_lines}")
        print(f"Počet slov: {num_words}")
        print(f"Počet znakov: {num_chars}")

    except FileNotFoundError:
        print(f"Súbor {file_name} neexistuje.")

# Načítanie názvu súboru a spustenie programu
file_name = input("Zadajte názov súboru: ")
file_statistics(file_name)
