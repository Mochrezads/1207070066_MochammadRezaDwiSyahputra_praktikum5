
import matplotlib.pyplot as plt #pemanggil library matplotlib penampilan visualisasi 
#matplotlib online
import cv2 #pemanggil library pembacaan gambar
from skimage.util import invert #pemanggil fungsi invert dari library skimage.utill

import numpy as np #pemanggil library untuk manipulasi array
#pembacaan gambar yang disimpan dalam folder
img1 = cv2.imread("Gambar/gambar3.jpg")#gambar yang akan ditampilkan
img2 = cv2.imread("Gambar/gambar4.jpg")#gambar yang akan ditampilkan

 
#cropping image
img1Cropped = img1.copy()#crop lalu dicopy
img1Cropped = img1Cropped[0:256, 64:320]#ukuran skala cropped
#pembuatan duplikat gambar yang akan di potong
img2Cropped = img2.copy()#gambar 2 crop lalu dicopy
img2Cropped = img2Cropped[64:256, 128:320]#ukuran skala cropped

#pembuatan plot gambar yang akan ditampilkan
fig, axes = plt.subplots (2, 2, figsize = (12, 12))
ax = axes.ravel()

ax[0].imshow(img1)#menampilkan gambar 1 dengan fungsi imshow
ax[0].set_title ("Citra Input 1")#memasukkan tittle atau judul gambar pada igm1

ax[1].imshow(img2, cmap='gray')#penampilan atau memunculkan img 2 dengan fungsi imshow
ax[1].set_title ("Citra Input 2")#memasukkan tittle atau judul gambar pada img2

ax[2].imshow(img1)#menampilkan atau memunculkan gambar 1 hasil dari pemotongan
ax[2].set_title("Citra Output 1")#memasukkan judul atau tittle pada gambar hasil pemotongan

ax[3].imshow(img2, cmap='gray')#menampilkan atau memunculkan gambar 2 hasil dari pemotongan 
ax[3].set_title('Citra Output 2')#memasukkan judul atau tittle pada gambar 2 hasil pemotongan

#citra Negative
inv = invert(img1Cropped)#melakukan inversi citra dengan fungsi invert
#menampilkan input dan output hasil dari inversi citra
print('Shape Input : ', img1Cropped.shape)
print('Shape Output : ',inv.shape)
#pembuatan subplot untuk menampilkan gambar hasil inversi citra
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
#menampilkan gambar 1 serta memasukkan judul atau tittle pada gambar sebelum terjadinya invert
ax[0].imshow(img1)
ax[0].set_title("Citra Input")#title yang akan muncul
#pembuatan histogram serta memasukkan judul untuk histogram pada gambar 1 
ax[1].hist(img1Cropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')#titile yang akan muncul
#menampilkan serta memberi judul hasil invert
ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')
#menampilkan serta memberi judul histogram hasil invert
ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')#title yang akan muncul

copyCamera = img2Cropped.copy().astype(float)#mengcopy gambar awal agar tidak terpengaruh 
#menyimpan dimensi gambar yang akan diolah
shape = copyCamera.shape
output1 = np.empty(shape)
#proses perhitungan untuk melakukan pengubahan pixel
for baris in range(0, shape[0]-1):
    for kolom in range(0, shape[1]-1):
        a1 = baris#untuk baris pixel
        b1 = kolom#untuk kolom pixel
        output1[a1, b1] = copyCamera[baris, kolom] /100

#memploting hasil dari perubahan pixel input dan output histogram dan gambar
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

#menampilkan serta memberikan judul pada gambar dan histogram sebelum dilakukan perubahan dan setelah dilakukan perubahan
ax[0].imshow(img2Cropped, cmap='gray')
ax[0].set_title("Citra Input") #tulisan yang akan muncul

ax[1].hist(img2Cropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')#tulisan yang akan muncul

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')#tulisan yang akan muncul

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')#tulisan yang akan muncul
plt.show()#menampilkan gamar

