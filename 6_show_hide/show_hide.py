def main():
    # 1. Read lines from data.txt
    with open("data.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    # 2. The first line is x (number of records)
    x = int(lines[0])

    # 3. The next x lines are the items
    items = lines[1 : x + 1]

    # 4. Initialize removed state for each item
    removed = [False] * x

    # 5. Remaining lines in the file are index toggles
    toggles = lines[x + 1 :]

    # 6. Toggle removal or restoration of items
    for t in toggles:
        index_val = int(t)
        if index_val == -1:
            # End of toggles
            break
        if 0 <= index_val < x:
            # Flip removal state
            removed[index_val] = not removed[index_val]

    # 7. Print items that are not removed
    for i in range(x):
        if not removed[i]:
            print(items[i])

if __name__ == "__main__":
    main()
