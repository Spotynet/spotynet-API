import json
from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import VisitorsExpoce

# Create your views here.
class StudentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
            if id>0:
                student = list(VisitorsExpoce.objects.filter(id = id).values())
                if (len(student)>0):
                    student = student[0]
                    datos = {'message': 'Success', 'student': student}
                else:
                    datos = {'message': 'Estudiante no encontrado...'}
                return JsonResponse(datos)                       
            else: 
                students = list(VisitorsExpoce.objects.values())
                if (len(students)>0):
                    datos = {'message': 'Success', 'students': students}
                else:
                    datos = {'message': 'No hay estudiantes en nuestra BD'}
                return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        
        if (VisitorsExpoce.objects.filter(email = jd['email']).first()):
            return HttpResponseBadRequest("Ya existe ese correo en nuestra BD")
        else:    
            VisitorsExpoce.objects.create(
                attend = jd['attend'],
                firstName = jd['firstName'],
                lastName = jd ['lastName'],
                email = jd ['email'],
                age = jd ['age'],
                country = jd ['country'],
                cState = jd ['cState'],
                phone = jd ['phone'],
                languageLevel = jd ['languageLevel'],
                program = jd ['program'],
                studyArea = jd ['studyArea'],
                dateStart = jd ['dateStart'],
                pay = jd ['pay'],
                sourceLead = jd ['sourceLead'],
                fuente = jd ['fuente']
            )
        datos = {'message': 'Success'}
        return JsonResponse(datos)


    def put(self, request,id):
        try:
                student = VisitorsExpoce.objects.filter(id = id).first()
                if (not student):
                    return HttpResponseBadRequest("No existe este ID en nuestra BD")

                jd = json.loads(request.body)
                student.attend = jd['attend']
                student.firstName = jd['firstName']
                student.lastName = jd ['lastName']
                student.email = jd ['email']
                student.age = jd ['age']
                student.country = jd ['country']
                student.cState = jd ['cState']
                student.phone = jd ['phone']
                student.languageLevel = jd ['languageLevel']
                student.program = jd ['program']
                student.studyArea = jd ['studyArea']
                student.dateStart = jd ['dateStart']
                student.pay = jd ['pay']
                student.sourceLead = jd ['sourceLead']
                
                student.save()
                return HttpResponse("Estudiante actualizado")
        except:
                return HttpResponseBadRequest("Error en los datos enviados")
    
    def delete(self,request,id):
        try:
            student = VisitorsExpoce.objects.filter(id = id).first()
            if (not student):
                return HttpResponseBadRequest("No existe este ID en nuestra BD")
             
            student.delete()
            return HttpResponse("Estudiante eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")