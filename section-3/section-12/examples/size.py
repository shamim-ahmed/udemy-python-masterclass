import sys

def my_range(n: int):
    print("my_range starts")
    val = 0

    while val < n:
        print("my_range is returning {}".format(val))
        yield val
        val += 1

_ = input("line 12")
# big_range = range(5)
big_range = my_range(1000)
_ = input("line 15")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

_ = input("line 22")
for x in big_range:
    print("line 24 - inside for loop")
    big_list.append(x)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
