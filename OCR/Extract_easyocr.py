import matplotlib.pyplot as plt
from pylab import rcParams
from IPython.display import Image
import easyocr
from OCR.using_cv2 import make_gray, resizing


def apply_ocr(img_path=None):
    try:
        rcParams['figure.figsize'] = 16, 32

        reader = easyocr.Reader(['en'])

        img_path = r'C:/Users/pixarsart/StampBox Classification/stampbox' + img_path
        print('Image path is ', img_path)
        output = reader.readtext_batched(img_path)
        if output:
            text_list = list()
            for elem in output[0]:
                text_list.append(elem[1])
            return text_list
        else:
            return None

    except Exception as e:
        print(f'[Extract Text OCR] the exception is {e}')
        return None


if __name__ == '__main__':
    apply_ocr()
