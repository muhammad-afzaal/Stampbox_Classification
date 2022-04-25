from OCR.Extract_easyocr import apply_ocr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpers.log_util import logger
from rest_framework.permissions import AllowAny
from classification.serializer import image_Add_serializer
from classification.using_selenium import use_sel_model
import os
from stampbox.config import Config
import shutil
# Create your views here.
env = Config.environment(mode_selection='development')


def remove_img(img_param):
    if os.path.exists(img_param):
        os.remove(img_param)
    else:
        print('File not deleted', img_param)


class ClassificationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = image_Add_serializer

    def get(self, request, *args, **kwargs):
        status_code = status.HTTP_200_OK
        response = {
            'status': status_code,
            'success': True,
            'message': 'GET API Working'
        }
        return Response(response, status_code)

    def post(self, request, *args, **kwargs):
        try:
            logger.info(
                f"REMOTE_HOST: {request.stream.META.get('REMOTE_HOST')} || REMOTE_ADDR: {request.stream.META.get('REMOTE_ADDR')}")
            logger.info(f"User-Agent: {request.headers.get('User-Agent')}")
            logger.info('[METHOD: POST] [ClassificationView] Predicting text from image')

            if request.data['media_file']:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info(f"File uploaded successfully, as {serializer.data}")
                    img = serializer.data['media_file']
                    img = env['Base_Path'] + img
                    # print('Relative Path', os.path.relpath(img))
                    # apply_ocr(os.path.relpath(img))
                    # text_list1 = apply_ocr(img)
                    text_list = use_sel_model(img)
                    # text_list = text_list1.append(text_list2)
                    if text_list:
                        status_code = status.HTTP_200_OK
                        response = {
                            'success': True,
                            'status_code': status_code,
                            'message': 'Image File added Successfully',
                            'data': serializer.data,
                            'related_text': text_list
                        }
                        remove_img(img)
                        return Response(response, status_code)
                    else:
                        status_code = status.HTTP_204_NO_CONTENT
                        response = {
                            'success': False,
                            'status_code': status_code,
                            'message': 'Unable to Apply OCR'
                        }
                        remove_img(img)
                        return Response(response, status_code)

                else:
                    logger.warn(f'serializers throws error : {serializer.errors}')
                    raise Exception

                # print(request.FILES['image'], type(request.FILES['image']), str(request.FILES['image']))
                # img = str(request.FILES['image'])
                # apply_ocr(img)
                # status_code = status.HTTP_200_OK
                # response = {
                #     'status': status_code,
                #     'success': True,
                #     'message': 'POST API Working'
                # }
                #
                # return Response(response, status_code)

        except Exception as e:
            logger.error(f'[METHOD: POST] [ClassificationView] exception occurred as {e}')
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'status_code': status_code,
                'success': False,
                'message': f'bad request {e}'
            }
            return Response(response, status_code)
