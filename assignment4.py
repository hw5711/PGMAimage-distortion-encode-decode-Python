# To change input file, in line 165
# To change output file, in line 66
# To input threshold, in line 185, second parameter
import numpy as np

tmp1 = []
tmp2 = []
tmp3 = []

class NewPicture:
    a = []  # store the x of replaced location
    b = []  # store the y of repladce location
    c = []  # store the replaced number
    h = 0
    w = 0
    arr2d =[h][w]
    array1d = []

    def __init__(self, height, width):
        self.a = []
        self.b = []
        self.c = []
        self.h = height
        self.w = width

    def set_arr(self,array):
        self.arr2d = array

    def add_a(self, num):
        self.a.append(num)

    def add_b(self, num):
        self.b.append(num)

    def add_c(self, num):
        self.c.append(num)

    def create_pic(self, hight, width):

        self.w = width
        self.h = hight
        p_num = self.w * self.h

        index = 0
        counter = 0 # Count number of pixles has been changed
        while (len(self.a) - index) != 0:
            number1 = self.a[index]
            number2 = self.b[index]
            number3 = self.c[index]
            index += 1
            self.arr2d[number1][number2] = number3
            counter += 1
            # print("number1, number2, number3")
            # print(number1, number2, number3)

        print("Total number of changed pixels: ", counter)

        # store two dimentions array into an one dimention array
        for i in range(0, self.h):
            for j in range(0, self.w):
                self.array1d.append(self.arr2d[i][j])
        print("")
        print("updated 2d array")
        print(self.arr2d)
        # open file for writing
        filename = 'baboon2-test256.pgm'
        fout = open(filename, 'wb')

        # define PGM Header
        pgmheader = 'P2' + '\n' + str(self.w) + ' ' + str(self.h) + '\n' + str(255) + '\n'
        pgmheader_byte = bytearray(pgmheader, 'utf-8')

        # write the header to the file
        fout.write(pgmheader_byte)

        # write the data to the file
        img = np.reshape(self.array1d, (self.h, self.w))
        for j in range(self.h):
            bnd = list(img[j, :])
            bnd_str = np.char.mod('%d', bnd)
            bnd_str = np.append(bnd_str, '\n')
            bnd_str = [' '.join(bnd_str)][0]
            bnd_byte = bytearray(bnd_str, 'utf-8')
            fout.write(bnd_byte)

        fout.close()


def read_pgm(name):
    with open(name) as f:
        lines = f.readlines()

    # Ignore commented lines
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    # Makes sure it is ASCII format (P2)
    assert lines[0].strip() == 'P2'

    # Convert data to a list of integers
    data1 = []
    for line in lines[1:]:
        data1.extend([int(c) for c in line.split()])
    # data[0]is the content, data[1]is the size of hight and width, data[2] is the max pixel, data[3]is the total pixels
    return (np.array(data1[3:]),(data1[1],data1[0]), data1[2],len(np.array(data1[3:])),data1[1], data1[0])


def check(new_array, threshold, x, y, x0, y0):

    # count num of pixels
    var_quad = 0
    num_pixels = 0
    avg_pixels = 0
    count = 0   # accumulate the num of pixels
    count1 = 0  # accumulate actual pixel color
    count2 = 0  # accumulate the varquad
    # Count the pixels numbers
    for i1 in range(x0, x):
        for j1 in range(y0, y):
            if new_array[i1][j1] != 0:
                count += 1

    num_pixels = count

    # if (x - x0) <= 1 and (y - y0) <= 1 :
    if count <=1 :
        return

    else:
        # Count avg of pixels
        for i2 in range(x0, x):
            for j2 in range(y0, y):
                count1 += new_array[i2][j2]

        avg_pixels = count1 / num_pixels
        # print("ave pix and count1 is: ", avg_pixels, count1)

        # Count variance of quad
        for i3 in range(x0, x):
            for j3 in range(y0, y):
                count2 += pow((new_array[i3][j3] - avg_pixels), 2)
        var_quad = pow(count2 /(num_pixels-1), 0.5)
        # var_quad = count2 / (num_pixels - 1)
        # print("variance quad : ", var_quad)

        if var_quad <= threshold:
            for i4 in range(x0, x):
                for j4 in range(y0, y):
                    new_array[i4][j4] = avg_pixels
                    tmp1.append(i4)
                    tmp2.append(j4)
                    tmp3.append(avg_pixels)
            return

        else:
            x1 = (x - x0) // 2
            y1 = (y - y0) // 2
            check(new_array, threshold, x1, y, x0, y0+y1)  # northwest
            check(new_array, threshold, x, y, x0 + x1, y0 + y1)  # northeast
            check(new_array, threshold, x1, y1, x0, y0)  # southwest
            check(new_array, threshold, x, y1, x0 + x1, y0)  # southeast


def convert12(pic, xIndex, yIndex):
    for i in range(0, xIndex):
        for j in range(0, yIndex):
            if pic[i][j] < 21:
                pic[i][j] = 0
            elif pic[i][j] >= 21 and pic[i][j] < 42:
                pic[i][j] = 1
            elif pic[i][j] >= 42 and pic[i][j] < 63:
                pic[i][j] = 2
            elif pic[i][j] >= 63 and pic[i][j] < 84:
                pic[i][j] = 3
            elif pic[i][j] >= 84 and pic[i][j] < 105:
                pic[i][j] = 4
            elif pic[i][j] >= 105 and pic[i][j] < 126:
                pic[i][j] = 5
            elif pic[i][j] >= 126 and pic[i][j] < 147:
                pic[i][j] = 6
            elif pic[i][j] >= 147 and pic[i][j] < 168:
                pic[i][j] = 7
            elif pic[i][j] >= 168 and pic[i][j] < 189:
                pic[i][j] = 8
            elif pic[i][j] >= 189 and pic[i][j] < 210:
                pic[i][j] = 9
            elif pic[i][j] >= 210 and pic[i][j] < 231:
                pic[i][j] = 10
            else:
                pic[i][j] = 11

#    return pic

def convert2(pic, xIndex, yIndex):
    for i in range(0, xIndex):
        for j in range(0, yIndex):
            if pic[i][j] < 128:
                pic[i][j] = 0
            else:
                pic[i][j] = 1

 #   return pic

if __name__ == '__main__':
    fileName = "/Users/huanwu/Documents/GitHub/PGMAimage-distortion-encode-decode-Python/baboon.pgma"
    print("Opened file name baboon.pgm")
    data = read_pgm(fileName)
    length = data[4]
    print(data[2]) # max gray color reading in the pic
    print(data[3]) # total pixels in the pic
    print(data[4]) # hight of the pic
    print(data[5]) # width of the pic
    # transfer the pgma 1D array into a 2D array and print out
    A1 = np.array(data[0])
    A2 = np.array(data[0])
    B1 = np.reshape(A1, (-1, length))
    B2 = np.reshape(A2, (-1, length))
    print(" 1 - dimentions array ( input pic ) :")
    print(A1)
    print("")
    print("2 - dimentions array ( store in 2D array ) :")
    print(B1)
    print("")
    convert12(B1, data[4], data[5])
    print(" convert to 12 - gray level array :")
    print(B1)
    print("")
    convert2(B2, data[4], data[5])
    print(" convert to 2 - gray level array: ")
    print(B2)

    #x_start = 0
    #y_start = 0
    # data[4] is the width of 2D array, data[5] is the hight of 2D array
    # second parameter is threshold
    #print("")
    #print("Threshold is: ", 256)
    #check(B, 256, data[4], data[5], x_start, y_start)

    # create a new pic object
    # pic = NewPicture(data[4], data[5])
    #
    # for i in range(0, len(tmp1)):
    #     pic.add_a(tmp1[i])
    # for j in range(0, len(tmp2)):
    #     pic.add_b(tmp2[j])
    # for k in range(0, len(tmp3)):
    #     pic.add_c(tmp3[k])
    #
    # pic.set_arr(B)
    # pic.create_pic(data[4],data[5])


