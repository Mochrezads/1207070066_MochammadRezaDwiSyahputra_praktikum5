# pemanggil library
import numpy as np#pemanggil library numpy untuk manipulasi array
import cv2 #pemanggil library cv2 untuk melakukan pembacaan dalam folder
import matplotlib.pyplot as plt #pemanggil library berfungsi untuk menampilkan dan memploting gambar yang akan ditampilkan 

img = cv2.imread("Gambar/gambar5.jpg") #mpembacaan gambar yang tersimpan dalam satu folder

#mendapatkan/define resolusi dan tipe gambar
img_height = img.shape[0] #memasukkan nilai tinggi gambar dalam variabel
img_width = img.shape[1] #memasukkan nilai lebar gambar dalam variabel
img_channel = img.shape[2] #memasukkan jumlah channel gambar dalam variable
img_type = img.dtype #membuat array untuk dimensi perubahan gambar

#percobaan pertama buat brightness untuk gambar grayscale 
#membuat variable img_brightness untuk menampung
img_brightness = np.zeros(img.shape, dtype=np.uint8)

#membuat fungsi penambahan brightness dengan nilai yang menjadi parameter 
def brighter (nilai) : #fungsi untuk melakukan penambahan brightness
    for y in range (0, img_height): #memberikan interval range untuk etiap pixel secara vertikal 
        for x in range (0, img_width):#memberikan interval range untuk setiap pixel secara horizontal
            #mendapatkan nilai warna red green blue pada pixel dengan variabel x,y
            red = img[y][x][0]#red
            green = img[y][x][1]#green
            blue = img[y][x][2]#blue
            gray = (int(red) + int(green) + int(blue))/3#rumus untuk menghitung rata rata nilai warna grayscale
            if gray >255: #penentuan nilai grayscake menggunakan fungsi if
                gray = 255 #gray sama dengan 255
            if gray < 0: #jika gray kurang dari0
                gray = 0 #gray sama dengan 0
            img_brightness[y][x]= (gray, gray, gray)#menyimpan nilai grayscale hasil dari proses
            
#menampilkan gambar dengan parameter -100
brighter(-100)#menambahkan nilai brightness
plt.imshow(img_brightness)#menampilkan gambar hasil proses
plt.title("brightness -100")#memberikan judul pada gambar hasil proses yang akan ditampilkan 
plt.show()#menampilkan keseluruhan gambar

brighter(100)#menambahkan nilai brightness
plt.imshow(img_brightness)#menampilkan gambar hasil perubahan 
plt.title("brightness 100")#memberikan judul atau tittle pada gambar 
plt.show()#menampilkan keseluruhan gambar

#brightness RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)

#fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai):#fungsi untuk menambahkan brightness
    for y in range(0, img_height):#memberikan interval range pada gambar secara vertical
        for x in range(0, img_width):#memberikan interval range pada gambar secara horizontal
            red = img[y][x][0]#menambahkan nilai intensirtah pada varialbe x,y
            red += nilai
            #penentuan nilai hasil menggunakan fungsi if
            if red > 255 :
                red = 255
                if red < 0 :
                    red = 0
            green = img[y][x][1]#menambahkan intensitas warna dengan variabel x,y
            green += nilai
            #penentuan nilai hasil menggunakan fungsi if
            if green > 255 :
                green = 255
                if green < 0 :
                    green = 0
            blue = img[y][x][2]#menambahkan nilai intensitas warna
            blue += nilai
            #penentuan nilai hasil menggunakan fungsi if
            if blue > 255 :
                blue = 255
                if blue< 0 :
                    blue = 0
            img_rgbbright[y][x] = (red, green, blue)#menampilkan gambar hasil dari perobahan
            
#menampilkan gambar dengan parameter -100
rgbbrighter(-100)#menambahkan nilai brightness pada gambar yang akan ditampilkan
plt.imshow(img_rgbbright)#menampilkan gambar hasil
plt.title("rgbbrightness -100")#memasukkan judul pada gambar
plt.show()#plt.show() Seperti yang dapat kita lihat di atas, kita menuliskan plt untuk memanggil library matplotlib

rgbbrighter(100)#menambahkan nilai brighness
plt.imshow(img_rgbbright)#menampilkan gambar hasil
plt.title("rgbbrightness 50")#memasukkan judul pada gambar
plt.show()#plt.show() Seperti yang dapat kita lihat di atas, kita menuliskan plt untuk memanggil library matplotlib

#kontras

img_contrass = np.zeros (img.shape, dtype=np.uint8)
#melakukan dan memberinkan nilai contras pada gambar serta melakukan penentuan intensitas warna dan proses perubahan contrass pada gambar
def contrass (nilai) :
        for y in range(0, img_height):
            for x in range(0, img_width):
                red = img[y][x][0]
                green = img[y][x][1]
                blue = img[y][x][2]
                gray = (int (red) + int(blue) + int(green))/3
                gray += nilai
                if gray > 255:
                    gray = 255
            img_contrass[y][x] = (gray, gray, gray)
            
#menampilkan gambar dengan parameter -100, serta memasukkan judul atau tittle dan menampilkannya
contrass(100) #contrass yang dipilih 100
plt.imshow(img_contrass)
plt.title("contrass 100")
plt.show ()#plt.show() Seperti yang dapat kita lihat di atas, kita menuliskan plt untuk memanggil library matplotlib
#menampilkan gambar dengan parameter 50, serta memasukkan judul atau tittle dan menampilkannya

contrass(50) #contrass yang dipilih 50
plt.imshow(img_contrass)
plt.title("contrass 50")
plt.show()#plt.show() Seperti yang dapat kita lihat di atas, kita menuliskan plt untuk memanggil library matplotlib

img_autocontrass = np.zeros(img.shape, dtype=np.uint8)
#melakukan serta merubah nilai gambar menggunakan fungsi autocontrass, melakukan perubahan intensitas warna dengan rumus 
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)
autocontrass()
#menampilkan keseluruhan gambar hasil auto contras dan memasukkan judul untuk gambar
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")#title yang akan muncul
plt.show()#plt.show() Seperti yang dapat kita lihat di atas, kita menuliskan plt untuk memanggil library matplotlib