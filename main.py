import pytesseract as tess
import glob
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

finaltxt = []

# for a in range(1, 88):


for im in glob.glob("Terms and Condition/Cropped/*.jpg"):
    img = cv2.imread(im)
    txt = tess.pytesseract.image_to_string(img)
    lst = txt.splitlines()

    for i in range(len(lst)):
        if not lst[i].strip():
            continue
        finaltxt.append(lst[i])

# for z in range(len(finaltxt)):
#     print(finaltxt[z])

# with open('List.txt', 'w') as f:
#     [f.write("%s\n" % item) for item in finaltxt]


print('\n'.join(finaltxt))
