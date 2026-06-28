
word = "python"
line = 1

with open(r"C:\Users\Vivek\AI-ML\Python Tutorial\FileHandling\Practice\sample.txt", "r") as f:
    while True:
        data = f.readline()

        if not data:      # End of file
            print(f"{word} not found")
            break

        if word in data:
            print(f"{word} found in line {line}")
            break

        line += 1