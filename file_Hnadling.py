file = open("sample.txt", "w")

file.write("Hello python \n")
file.write("hello world\n")
file.write("hello class\n")
lines = ["this is a line \nthis is another line \nthis is the line3 \n"]

file.writelines(lines)
file.close()