
# open file and read file

# file = open(r"C:\Users\abbim\OneDrive\Desktop\AIML\Python Tutorial\FileHandling\data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# writeline means print one line of data

# file = open(r"C:\Users\abbim\OneDrive\Desktop\AIML\Python Tutorial\FileHandling\data.txt", "r")
# content = file.readline()
# print(content)
# file.close()

# writeline means print multiple line of data

file = open(r"C:\Users\abbim\OneDrive\Desktop\AIML\Python Tutorial\FileHandling\data.txt", "r")
content = file.readlines()
print(content)
file.close()

