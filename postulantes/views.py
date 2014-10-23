#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from forms import UploadFileForm 
from models import Comuna, Postulante 

# Create your views here.




def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #aqui va todo lo que tengo que hacer
            f = request.FILES['f']
            postulantes = f.readlines()
            for chunk in postulantes:
                chunk = chunk.split(';')
                fecha = chunk[0].decode('iso-8859-1')
        
                try:
                    fecha = fecha.split('-')[2] + '-' + fecha.split('-')[1] + '-' + fecha.split('-')[0] 

                except:
                    fecha = None 

                rut = chunk[1].decode('iso-8859-1')
                nombres = chunk[2].decode('iso-8859-1').title()
                apellidos = chunk[3].decode('iso-8859-1').title()
                domicilio=chunk[4].decode('iso-8859-1').title()
                comuna =chunk[5].decode('iso-8859-1').title()
                os10 =chunk[6].decode('iso-8859-1')
                if ('NO' or 'no' or 'No') in os10:
                    os10 = False
                elif ('SI' or 'SÍ' or 'sí' or 'si' or 'Sí' or 'Si') in os10:
                    os10 = True


                sexo =chunk[7].decode('iso-8859-1')
                medio =chunk[8].decode('iso-8859-1')
                cargo =chunk[9].decode('iso-8859-1')
                telefono =chunk[10].decode('iso-8859-1')
                observaciones = chunk[11].decode('iso-8859-1')
                print nombres, apellidos 
                postulante = Postulante(fecha=fecha, rut=rut, nombres=nombres, apellidos=apellidos, domicilio=domicilio, 
                comuna=comuna, os10=os10, sexo=sexo, medio=medio, cargo=cargo, telefono=telefono, 
                observaciones=observaciones)
                postulante.save()
                #comuna = Comuna(region_id=1, nombre=chunk.decode('iso-8859-1'))
                #comuna.save()
            return HttpResponse('OK') 
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form':form})
