import cv2
import os
import glob
count = 0
im_names = sorted(glob.glob(os.path.join("/content/drive/MyDrive/SACK_THURSDAY2/SACK_NEW_8TH_DEC/ARIELRED_NEW", '*.jpeg')))
for im_name in im_names:
    file_name = os.path.basename(im_name).split('.')[0]
    file_name = file_name.split()[0]
    imag = cv2.imread(im_name,1)
    count +=1
    print(count)
    resize_imag = cv2.resize(imag, (150, 150))
    cv2.imwrite("/content/drive/MyDrive/SACK_THURSDAY2/SACK_NEW_8TH_DEC/ARIELRED_NEW/re%s .jpeg"%file_name,resize_imag)
