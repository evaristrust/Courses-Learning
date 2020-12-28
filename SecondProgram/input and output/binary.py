# with open("binary", 'bw') as bin_file:
#     for i in range(30):
#         bin_file.write(bytes([i]))
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

# you can omit the line 2 and do like this:

with open("binary", 'bw') as bin_file:
    bin_file.write(bytes(range(30)))

with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)

# another example:
# initializing variables

a = 65534 # FF FE
b = 65535 # FF FF
c = 65536 # 00 01 00 00
x = 2998302 # 02 2D C0 1E

with open("binary2", 'bw') as binFile2:
    binFile2.write(a.to_bytes(2, 'big')) # two parameters .. 1st: the number bytes we want
    binFile2.write(b.to_bytes(2, 'big'))  # 2nd: whether to return whether it's big or little indian
    binFile2.write(c.to_bytes(4, 'big'))
    binFile2.write(x.to_bytes(4, 'little'))


with open("binary2", 'br') as binFile2:
    e = int.from_bytes(binFile2(2), 'big')
    f = int.from_bytes(binFile2(2), 'big')
    g = int.from_bytes(binFile2(4), 'big')
    h = int.from_bytes(binFile2(4), 'big')
    i = int.from_bytes(binFile2(4), 'big')