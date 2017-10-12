import gzip
import numpy as np

def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic,'big')
        print("Magic is:", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab,'big')
        print("Num of labels is:", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

    return labels

def read_images_from_file(filename):
    with gzip.open(filename,'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic,'big')
        print("Magic is:", magic)

        noimg = f.read(4)
        noimg = int.from_bytes(noimg,'big')
        print("Number of images is:", noimg)

        norow = f.read(4)
        norow = int.from_bytes(norow,'big')
        print("Number of rows is:", norow)

        nocol = f.read(4)
        nocol = int.from_bytes(nocol,'big')
        print("Number of cols is:", nocol)

        images = []

        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                row.append(cols)
            images.append(rows)
    return images

train_images = read_labels_from_file("train-images-idx3-ubyte.gz")
test_images = read_labels_from_file("t10k-images-idx3-ubyte.gz")

print("Train Images:")
print(train_images)
#print("Test Images:")
#print(test_images)

#for row in train_images:
#    for col in train_images:
#        print('.' if col <= 127 else '#', end='')
        

import PIL.Image as pil
test = np.array(train_images)
pixel = test.reshape(1, 60000)
img = pil.fromarray(test, mode = "P")
img = img.convert('RGB')
img.show()
img.save('2.png')

# train_labels = read_labels_from_file("train-labels-idx1-ubyte.gz")
# test_labels = read_labels_from_file("t10k-labels-idx1-ubyte.gz")

#print("Train Labels:")
#print(train_labels)
#print("Test Labels:")
#print(test_labels)