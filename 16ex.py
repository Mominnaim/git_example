from sys import argv

script, filename = argv

print(f"we are going to delete this file {filename}")
print(f'If you do want to do that, please press control C')
print(f'If you do not want that hit return')

input("?")

print("Opening file...")
target = open(filename, "w")

print('TRUNCATING THE FILE. GOODBYE!')
target.truncate()

print("Now I will ask you for three lines")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finaly we close it.")
target.close()