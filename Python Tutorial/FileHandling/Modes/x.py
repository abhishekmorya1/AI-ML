# x -> creates new and open for writing

file = open("xsample.txt", "x")
file.write("New file created using x mode")
file.close()