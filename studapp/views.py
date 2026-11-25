from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from studapp.models import StudentDb
from studapp.serializers import StudentSerializer,RegisterSerializers



class RegisterView(APIView):

   permission_classes = [AllowAny]
   def post(self,request):
           serializers_instance = RegisterSerializers(data=request.data)
           if serializers_instance.is_valid():
               serializers_instance.save()
               return Response(data={
                   "Message":"Registration sucessfull..!"},status=201)
           return Response(
               data=serializers_instance.errors,status=400 )


class StudentView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        students = StudentDb.objects.all()

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)



    def post(self, request):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class StudentRetrieveDeleteUpdateView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, pk):

        student = get_object_or_404(StudentDb, id=pk)

        serializer = StudentSerializer(student)

        return Response(serializer.data)


    # PUT - Update student

    def put(self, request, pk):

        student = get_object_or_404(StudentDb, id=pk)

        serializer = StudentSerializer(student,data=request.data )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def delete(self, request, pk):

        student = get_object_or_404(StudentDb, id=pk)

        student.delete()

        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_200_OK
        )


