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


def sel_function(img):
    text_list = use_sel_model(img)
    if text_list:
        repeat = False
        status_code = status.HTTP_200_OK
        response = {
            'success': True,
            'status_code': status_code,
            'message': 'Image File added Successfully',
            # 'data': serializer.data,
            'extracted_details': text_list
        }
        remove_img(img)
        return response, status_code, repeat

    else:
        repeat = True
        status_code = status.HTTP_204_NO_CONTENT
        response = {
            'success': False,
            'status_code': status_code,
            'message': 'Unable to Apply OCR'
        }
        # remove_img(img)
        return response, status_code, repeat


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
            # logger.info(
            #     f"REMOTE_HOST: {request.stream.META.get('REMOTE_HOST')} || REMOTE_ADDR: {request.stream.META.get('REMOTE_ADDR')}")
            logger.info(f"User-Agent: {request.headers.get('User-Agent')}")
            logger.info('[METHOD: POST] [ClassificationView] Predicting text from image')
            print('DATA HERE: ', request.FILES)
            if request.data['media_file']:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info(f"File uploaded successfully, as {serializer.data}")
                    img = serializer.data['media_file']
                    img = env['Base_Path'] + img

                    text_list = use_sel_model(img)
                    if text_list:
                        # repeat = False
                        status_code = status.HTTP_200_OK
                        response = {
                            'success': True,
                            'status_code': status_code,
                            'message': 'Image File added Successfully',
                            # 'data': serializer.data,
                            'extracted_details': text_list
                        }
                        remove_img(img)
                        return Response(response, status_code)

                    else:
                        # repeat = True
                        status_code = status.HTTP_204_NO_CONTENT
                        response = {
                            'success': False,
                            'status_code': status_code,
                            'message': 'Unable to Apply OCR'
                        }
                        remove_img(img)
                        return Response(response, status_code)

                    # # loop
                    # # iteration 1
                    # response, status_code, repeat = sel_function(img)
                    # if repeat == True:
                    #     response, status_code, repeat = sel_function(img)
                    #     # iteration 2
                    #     if repeat == True:
                    #         response, status_code, repeat = sel_function(img)
                    #         # iteration 3 final
                    #         if repeat == True:
                    #             remove_img(img)
                    #             return Response(response, status_code)
                    #         else:
                    #             return Response(response, status_code)
                    #
                    #     else:
                    #         return Response(response, status_code)
                    #
                    # else:
                    #     return Response(response, status_code)

                else:
                    logger.warn(f'serializers throws error : {serializer.errors}')
                    raise Exception

        except Exception as e:
            logger.error(f'[METHOD: POST] [ClassificationView] exception occurred as {e}')
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'status_code': status_code,
                'success': False,
                'message': f'bad request {e}'
            }
            return Response(response, status_code)
