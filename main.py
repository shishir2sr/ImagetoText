import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2

finaltxt = []

for a in range(1, 88):
    img = cv2.imread('Cropped/%s.jpg' %a)
    txt = tess.pytesseract.image_to_string(img)
    lst = txt.splitlines()

    for i in range(len(lst)):
        if not lst[i].strip():
            continue
        finaltxt.append(lst[i])

# for z in range(len(finaltxt)):
#     print(finaltxt[z])

with open('List.txt', 'w') as f:
    [f.write("%s\n" % item) for item in finaltxt]














