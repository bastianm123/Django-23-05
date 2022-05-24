from os import stat
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Producto
from rest_producto.serializers import ProductoSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_productos(request):
    if request.method == 'GET':
        listaProductos = Producto.objects.all()
        serializer = ProductoSerializer(listaProductos, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = ProductoSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)