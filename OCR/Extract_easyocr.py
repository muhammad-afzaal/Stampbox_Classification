import matplotlib.pyplot as plt
import cv2
from pylab import rcParams
from IPython.display import Image
import easyocr
from OCR.using_cv2 import make_gray, resizing


# from search_query import search_query, compare_ratio


# def show_graph(outdata):
#     for data in outdata:
#         cord = outdata[outdata.index(data)][0]
#         x_min, y_min = [min(idx) for idx in zip(*cord)]
#         x_max, y_max = [max(idx) for idx in zip(*cord)]
#         image = cv2.imread(image_path)
#         cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
#         plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def apply_ocr(img_path=None):
    try:
        # rcParams['figure.figsize'] = 2.4, 1.8
        # rcParams['figure.figsize'] = 3.4, 2.8
        # rcParams['figure.figsize'] = 6.4, 4.8
        # rcParams['figure.figsize'] = 8, 16
        rcParams['figure.figsize'] = 16, 32

        reader = easyocr.Reader(['en'])

        # Image(path_param.replace('C:', 'C:/Users/pixarsart/StampBox Classification/stampbox/'))
        # img = cv2.imread(path_param, 0)
        img_path = r'C:/Users/pixarsart/StampBox Classification/stampbox' + img_path
        # img_path = path_param
        # img_path = 'C:/Users/pixarsart/StampBox Classification/stampbox/media/File_Storage/geeks_RVewbTI.jpg'
        print('Image path is ', img_path)

        # output = reader.readtext(img, rotation_info=[90,180,270], detail=0, paragraph=False)
        # output = reader.readtext(img_path, rotation_info=[90, 180, 270])
        output = reader.readtext_batched(img_path)
        if output:
            text_list = list()
            for elem in output[0]:
                text_list.append(elem[1])
            return text_list
        else:
            return None

        # print("output", output)
        # print("output1", output1)
        # print(output2)
        # result_list = list()
        # for element in output:
        #     if len(element[1]) > 1 and element[1].lower() is not 'postage'.lower():
        #         # if 'u.s' in element[0][0] or ' us ' in element[0][0]: Untitled design(3)
        #
        #         result = search_query(input_param=element[1])
        #         if result:
        #             result_list.append((result, element[1]))
        #
        # print(result_list)
        # if len(result_list) > 1:
        #     print(compare_ratio(result_list=result_list))
        # else:
        #     print(result_list)

        # show_graph(outdata=output)
        # return output
    except Exception as e:
        print(f'[Extract Text OCR] the exception is {e}')
        return None


if __name__ == '__main__':
    apply_ocr()
    # image_path = \
    #     r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Images\Stamps_images\Untitled design (18).png"
    # output = apply_ocr(image_path)
    # print('________Untitled.png')
    # resizing(image_param=image_path)

    # image_path1 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_blur.jpg"
    # image_path2 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_blur_thresh.jpg"
    # image_path3 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_bw.jpg"
    # image_path4 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_index.jpg"
    # image_path5 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_inverted.jpg"
    # image_path6 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_thresh.jpg"
    # image_path7 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\inverted.jpg"
    # image_path8 = \
    #     r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\gray_inverted_no_noise.jpg"
    # image_path9 = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Extract Text\temp\no_noise_inverted.jpg"
    #
    # apply_ocr(image_path1)
    # print('________gray_blur.jpg')
    # apply_ocr(image_path2)
    # print('________gray_blur_thresh.jpg')
    # apply_ocr(image_path3)
    # print('________gray_bw.jpg')
    # apply_ocr(image_path4)
    # print('________gray_index.jpg')
    # apply_ocr(image_path5)
    # print('________gray_inverted.jpg')
    # apply_ocr(image_path6)
    # print('________gray_thresh.jpg')
    # apply_ocr(image_path7)
    # print('________inverted.jpg')
    # apply_ocr(image_path8)
    # print('________gray_inverted_no_noise.jpg')
    # apply_ocr(image_path9)
    # print('________no_noise_inverted.jpg')

    # gray_img = make_gray(image_path=image_path)
    # apply_ocr(gray_img)

# cord = output[-1][0]
# x_min, y_min = [min(idx)for idx in zip(*cord)]
# x_max, y_max = [max(idx)for idx in zip(*cord)]
# image = cv2.imread(image_path)
# cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0,0,255), 2)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
