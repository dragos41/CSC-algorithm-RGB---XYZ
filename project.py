from PIL import Image

# Task 1

def RGBtoXYZ(rFile,wFile):
  theFile = open(rFile, "r")
  Index = []
  for value in theFile.read().split("\n"):
    Index.append(value)
  theFile.close()
  r = 0
  f = open (wFile,"w+")
  while r < (len(Index) -2):
    x = 0.431 * int(Index[r]) + 0.342 * int(Index [r+1]) + 0.178 * int(Index[r+2])
    y = 0.222 * int(Index[r]) + 0.707 * int(Index [r+1]) + 0.071 * int(Index[r+2])
    z = 0.020 * int(Index[r]) + 0.130 * int(Index [r+1]) + 0.939 * int(Index[r+2])
    f.write("%d\n%d\n%d\n" % (x, y, z))
    r = r + 3
  f.close()

def XYZtoRGB(rFile,wFile):
  theFile = open(rFile, "r")
  Index = []
  for value in theFile.read().split("\n"):
    Index.append(value)
  theFile.close()
  x = 0
  f = open (wFile,"w+")
  while x < (len(Index) -2):
    r = 3.063 * int(Index[x]) - 1.393 * int(Index [x+1]) - 0.476 * int(Index[x+2])
    g = - 0.969 * int(Index[x]) + 1.876 * int(Index [x+1]) + 0.042 * int(Index[x+2])
    b = 0.068 * int(Index[x]) - 0.229 * int(Index [x+1]) + 1.069 * int(Index[x+2])
    f.write("%d\n%d\n%d\n" % (r, g, b))
    #f.write("%d\n%d\n%d\n" % (b, g, r))
    x = x + 3
  f.close()

# Task 2

def TXTtoIMG(txt,image):
  theFile = open(txt, "r")
  Index = []
  for value in theFile.read().split("\n"):
    Index.append(value)
  theFile.close()
  r = 0
  tuplu = []
  while r < (len(Index)-2 ):
    tuplu.append((int(Index[r]) ,int( Index[r+1] ), int(Index[r+2])))
    r = r + 3
  img = Image.new('RGB',(256,170))
  #img = Image.new('RGB',(384,256))
  
  pixel = img.load
  print (len(tuplu))
  img.putdata(tuplu)
  img.save(image)
  img.show() 
  
def IMGtoTXT(image, txt):
  img = Image.open (image,"r")
  pix = img.load()
  f = open (txt,"w+")
  print ("Pixel & Lenght:")
  print (img.size[0])
  print (img.size[1])
  print (pix[0,2])
  for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
      f.write("%d\n%d\n%d\n" % (pix[x,y][0],pix[x,y][1],pix[x,y][2] ))
  f.close()


IMGtoTXT("parrots.jpg","RGB.txt")
RGBtoXYZ("RGB.txt","XYZ.txt")
#XYZtoRGB("XYZ.txt","RGB3.txt")
#TXTtoIMG("RGB3.txt","new1.jpg")

XYZtoRGB("XYZ-curs.txt","RGB2.txt")
TXTtoIMG("RGB2.txt","new.jpg")
