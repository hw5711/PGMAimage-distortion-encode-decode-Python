import numpy as np
import numpy


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

    return (np.array(data1[3:]),(data1[1],data1[0]), data1[2],len(np.array(data1[3:])),data1[1], data1[0])


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


def convert2(pic, xIndex, yIndex):
    for i in range(0, xIndex):
        for j in range(0, yIndex):
            if pic[i][j] < 128:
                pic[i][j] = 0
            else:
                pic[i][j] = 1


def decode(picfilename):
    inputPic = read_pgm(picfilename)
    inputArray = np.array(inputPic[0])
    if inputPic[2] > 1:
        for i in range(0, data[3]):
            if inputArray[i] == 0:
                inputArray[i] = 10
            elif inputArray[i] == 1:
                inputArray[i] = 31
            elif inputArray[i] == 2:
                inputArray[i] = 52
            elif inputArray[i] == 3:
                inputArray[i] = 73
            elif inputArray[i] == 4:
                inputArray[i] = 94
            elif inputArray[i] == 5:
                inputArray[i] = 115
            elif inputArray[i] == 6:
                inputArray[i] = 136
            elif inputArray[i] == 7:
                inputArray[i] = 157
            elif inputArray[i] == 8:
                inputArray[i] = 178
            elif inputArray[i] == 9:
                inputArray[i] = 199
            elif inputArray[i] == 10:
                inputArray[i] = 220
            else:
                inputArray[i] =  241
    else:
        for i in range(0, data[3]):
            if inputArray[i] == 0:
                inputArray[i] = 64
            elif inputArray[i] == 1:
                inputArray[i] = 192

    return inputArray


def createFile(fname, B):
    fout = open(fname, 'wb')
    # define PGM Header
    pgmheader = 'P2' + '\n' + str(data[4]) + ' ' + str(data[5]) + '\n' + str(255) + '\n'
    pgmheader_byte = bytearray(pgmheader, 'utf-8')
    # write the header to the file
    fout.write(pgmheader_byte)
    # write the data to the file
    for j in range(data[5]):
        bnd = list(B[j, :])
        bnd_str = np.char.mod('%d', bnd)
        bnd_str = np.append(bnd_str, '\n')
        bnd_str = [' '.join(bnd_str)][0]
        bnd_byte = bytearray(bnd_str, 'utf-8')
        fout.write(bnd_byte)
    fout.close()

def calDistortion(arr1, arr2, xIndex, yIndex):
    counter = 0
    for i in range(0, xIndex):
        for j in range(0, yIndex):
            counter = arr2[i][j] - arr1[i][j]

    return counter


def absoluteDiff(arr1, arr2, xIndex, yIndex):
    arr = numpy.zeros([xIndex,yIndex])
    for i in range(0, xIndex):
        for j in range(0, yIndex):
            if arr1[i][j] >= arr2[i][j]:
                arr[i][j] = (arr1[i][j] - arr2[i][j])
            else:
                arr[i][j] = (arr2[i][j] - arr1[i][j])

    return arr


if __name__ == '__main__':
    fileName = "/Users/huanwu/Documents/GitHub/PGMAimage-distortion-encode-decode-Python/baboon.pgma"
    print("Opened file name baboon.pgm")
    data = read_pgm(fileName)
    length = data[4]
    print(data[2]) # Max gray color reading in the pic
    print(data[3]) # Total pixels in the pic
    print(data[4]) # Width of the pic
    print(data[5]) # Hight of the pic

    # Transfer the pgma 1D array into a 2D array and print out
    A1 = np.array(data[0])
    A2 = np.array(data[0])
    B1 = np.reshape(A1, (-1, length))
    B2 = np.reshape(A2, (-1, length))
    print("\n1 - dimentions array ( input pic ) :\n", A1)
    print("\n2 - dimentions array ( store in 2D array ) :\n", B1)

    # Convert image to 12 gray level image
    convert12(B1, data[4], data[5])
    print("\nconvert to 12 - gray level array :\n", B1)
    # Convert image to 2 gray level image
    convert2(B2, data[4], data[5])
    print("\nconvert to 2 - gray level array: \n", B2)

    # Create 2 images with 2 levels
    filename1 = 'baboon12gray.pgm'
    createFile(filename1, B1)

    filename2 = 'baboon2gray.pgm'
    createFile(filename2, B2)

    # Decode 2 level images and store as pgma images
    filePath = "/Users/huanwu/Documents/GitHub/PGMAimage-distortion-encode-decode-Python/"
    newName1 = filePath + filename1
    newName2 = filePath + filename2
    C1 = decode(newName1)
    C2 = decode(newName2)
    print("\ndecoded 12-level gray image is : ", C1)
    print("\ndecoded 2-level gray image is : ", C2)

    # Transfer c1 and c2 to 2-dimension arrays
    D1 = np.reshape(C1, (-1, length))
    D2 = np.reshape(C2, (-1, length))
    decodeFile1 = 'baboon12gray-decoded.pgm'
    decodeFile2 = 'baboon2gray-decoded.pgm'
    createFile(decodeFile1, D1)
    createFile(decodeFile2, D2)

    # Calculate the distortion
    num1 = calDistortion(B1, D1, data[4], data[5])/data[3]
    num2 = calDistortion(B2, D2, data[4], data[5])/data[3]

    print("\ndistortion of 12-gray image is: ", num1)
    print("\ndistortion of 2-gray image is: ", num2)

    # Create error images
    E1 = absoluteDiff(B1, D1, data[4], data[5])
    E2 = absoluteDiff(B2, D2, data[4], data[5])
    errImage1 = 'baboon12gray--errorImage.pgm'
    errImage2 = 'baboon2gray--errorImage.pgm'
    createFile(errImage1, E1)
    createFile(errImage2, E2)
