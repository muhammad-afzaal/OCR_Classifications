import matplotlib.pyplot as plt
import cv2
from pylab import rcParams
from IPython.display import Image
import easyocr

rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])
image_path = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Images\Trained\npm-2000_2020_75x.jpg"

Image(image_path)

output = reader.readtext(image_path)

print(output)

# cord = output[-1][0]
# x_min, y_min = [min(idx)for idx in zip(*cord)]
# x_max, y_max = [max(idx)for idx in zip(*cord)]
# image = cv2.imread(image_path)
# cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0,0,255), 2)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
