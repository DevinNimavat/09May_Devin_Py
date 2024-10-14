from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from myapp.models import CommentData
from myapp.serializer import commentSerial


# Create your views here.

@api_view(['GET'])
def getdata(request):
    try:
        data = CommentData.objects.all()
        print(data)
    except CommentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = commentSerial(data, many=True)
    print(serial)
    return Response(data=serial.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_data_id(request, id):
    try:
        data = CommentData.objects.get(id=id)
    except CommentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = commentSerial(data)
    return Response(data=serial.data, status=status.HTTP_200_OK)


@api_view(['POST','GET'])
def add_data(request):
    try:
        data = CommentData.objects.all()
        print(data)
    except CommentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    newserial = commentSerial(data, many=True)
    if request.method == 'POST':
        serial = commentSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(data=newserial.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def update_comment(request,id):
    try:
        data1=CommentData.objects.get(id=id)

        print(data1)
    except CommentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=commentSerial(data1)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=commentSerial(data=request.data,instance=data1)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def patch_update(request,id):
    try:
        data1=CommentData.objects.get(id=id)

        print(data1)
    except CommentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=commentSerial(data1)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PATCH':
        serial=commentSerial(data=request.data,instance=data1,partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET'])
def delete_comment(request,id):
    try:
        data=CommentData.objects.get(id=id)
    except CommentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=commentSerial(data)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        CommentData.delete(data)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)