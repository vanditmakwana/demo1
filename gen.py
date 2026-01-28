# def my_genrator():
#     for i in range(100000):
#         yield i

# gen=my_genrator()

# for j in gen:
#     print(j,end=" ")

file_path="demo.txt"

with open(file_path) as file:
    lines=(line.strip() for line in file)
    for i in lines:
        print(i)