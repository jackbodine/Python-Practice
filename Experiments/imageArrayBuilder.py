from PIL import Image

# This program takes an image and saves four files corresponding to the RGBA values.
# I had to write this program to extract data for use in a separate python project that uses Jython.

INCREMENT = 3

i = Image.open('images/wanderer.png')
size = i.size
pix = i.load()

print(size)

c_strings = ["" for _ in range(3)]

for x in range(0, size[0], INCREMENT):
    for y in range(0, size[1], INCREMENT):
        color = pix[x, y]
        for i in range(3):
            c_strings[i] += str(color[i]) + ","

    for i in range(3):
        c_strings[i] = c_strings[i][:-1] + "\n"
    percentage = str(x/size[0]*100)
    print(percentage + "%")

for i in range(3):
    values = "rgba"
    name = "export/" + values[i] + "_file.txt"
    file = open(name, "x")
    file.write(c_strings[i])
    file.close()
