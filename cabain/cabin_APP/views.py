from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

########################MENU################################

@login_required
def main_menu(request):
    return render(request, 'menu_principal.html')


######################REGISTRO###############################


def registrarse(request):
    form = FormUser()
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            firs_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User(username=username, first_name=firs_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            return redirect(main_menu)
    context = {
        'form': form
    }
    return render(request, 'registro.html', context)


####################PROYECTO##################################


@login_required
def crear_proyecto(request):
    form = FormCreateProject(initial={'username': request.user})
    if request.method == 'POST':
        form = FormCreateProject(request.POST, initial={'username': request.user})
        if request.user.id != int(form.data['username']):
            return redirect(crear_proyecto)
        if form.is_valid():
            form.save()
            return redirect(listado_proyectos)
    context = {'form': form}
    return render(request, 'proyecto_nuevo.html', context)

@login_required
def listado_proyectos(request):
    proyectos = Project.objects.filter(username=request.user)
    context = {'items': proyectos}
    return render(request, 'listado_proyectos.html', context)

@login_required
def eliminar_proyecto(request, id):
    proyectos = Project.objects.get(id=id)
    proyectos.delete()
    return redirect(proyecto)

@login_required
def proyecto(request, id):
    proyecto = Project.objects.get(id=id)
    materiales = ProjectDetail.objects.filter(user=request.user, project=proyecto)
    trabajos = ProjectWorker.objects.filter(user=request.user, project=proyecto)
    form_material = FormProjectDetail(initial={'user':request.user,'project':proyecto})
    form_trabajo = FormProjectWorker(initial={'user':request.user,'project':proyecto})
    context = {
        'proyecto': proyecto,
        'materiales': materiales,
        'trabajos': trabajos,
        'form_material': form_material,
        'form_trabajo': form_trabajo
    }
    return render(request, 'proyecto.html', context)

@login_required
def crear_material(request,id):
    proyecto_selec = Project.objects.get(id=id)
    if request.method == 'POST':
        form_material = FormProjectDetail(request.POST, initial={'user':request.user,'project':proyecto_selec})
        if form_material.is_valid():
            form_material.save()
            return redirect(proyecto, id=id)
    return redirect(proyecto, id=id)

@login_required
def crear_trabajo(request,id):
    proyecto_selec = Project.objects.get(id=id)
    if request.method == 'POST':
        form = FormProjectWorker(request.POST, initial={'user':request.user,'project':proyecto_selec})
        if form.is_valid():
            form.save()
            return redirect(proyecto, id=id)
    return redirect(proyecto, id=id)



#################METODO DE PAGO#################################

@login_required
def payment_method(request):
    form = FormPaymentMethod(initial={'user': request.user})
    if request.method == 'POST':
        form = FormPaymentMethod(request.POST, initial={'user': request.user})
        if request.user.id != int(form.data['user']):
            return redirect(payment_method)
        if form.is_valid():
            form.save()
            return redirect(payment_method)
    metodos = PaymentMethod.objects.all()
    context = {
        'form': form,
        'metodos': metodos
        }
    return render(request, 'metodo_pago.html', context)

@login_required
def eliminar_metodo_pago(request, id):
    metodo = PaymentMethod.objects.get(id=id)
    metodo.delete()
    return redirect(payment_method)

@login_required
def actualizar_metodo_pago(request, id):
    metodo = PaymentMethod.objects.get(id=id)
    form = FormPaymentMethod(instance=metodo)
    if request.method == 'POST':
        form = FormPaymentMethod(request.POST, instance=metodo)
        if form.is_valid():
            form.save()
            return redirect(payment_method)
    metodos = PaymentMethod.objects.filter(user=request.user)
    context = {
        'form': form,
        'metodos': metodos
    }
    return render(request, 'actualizar_metodo_pago.html', context)


################UNIDAD DE MEDIDA################################

@login_required
def unidad_medida(request):
    form = FormUnidadMedida(initial={'user': request.user})
    if request.method == 'POST':
        form = FormUnidadMedida(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(unidad_medida)
    unidades = MeasureUnit.objects.all()
    context = {
        'form': form,
        'unidades': unidades
    }
    return render(request, 'unidadMedida.html', context)

@login_required
def actualizar_unidad_medida(request, id):
    unidad = MeasureUnit.objects.get(id = id)
    form = FormUnidadMedida(instance=unidad)
    if request.method == 'POST':
        form = FormUnidadMedida(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect(unidad_medida)
    unidades = MeasureUnit.objects.all()
    context = {
        'form': form,
        'unidades': unidades
    }
    return render(request, 'editar_unidadMedida.html', context)

@login_required    
def eliminar_unidad_medida(request, id):
    unidad = MeasureUnit.objects.get(id=id)
    unidad.delete()
    return redirect(unidad_medida)


#######################MAESTROS##########################################

@login_required
def maestro(request):
    form = FormWorker(initial={'user': request.user})
    maestros = Worker.objects.all()
    if request.method == 'POST':
        form = FormWorker(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(maestro)
    context = {
        'form': form,
        'maestros': maestros
        }
    return render(request, 'maestro.html', context)

@login_required
def actualizar_maestro(request, id):
    worker = Worker.objects.get(id=id)
    form = FormWorker(instance=worker)
    if request.method == 'POST':
        form = FormWorker(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect(maestro)
    context = {'form': form}
    return render(request, 'actualizar_maestro.html', context)

@login_required
def eliminar_maestro(request, id):
    worker = Worker.objects.get(id=id)
    worker.delete()
    return redirect(maestro)


#################PRODUCTO#################################################


@login_required
def producto(request):
    productos = Product.objects.filter(user=request.user)
    form = FormProduct(initial={'user': request.user})
    if request.method == 'POST':
        form = FormProduct(request.POST, initial={'user': request.user})
        if form.is_valid:
            form.save()
            return redirect(producto)
    context = {
        'items': productos,
        'form': form
    }
    return render(request, 'producto.html', context)

@login_required
def eliminar_producto(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(producto)

####falta funcion actulizar producto####
@login_required
def actualizar_producto(request, id):
    product = Product.objects.get(id=id)
    form = FormProduct(instance=product)
    if request.method=='POST':
        form = FormProduct(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect(producto)
    context = {
        'form': form
    }
    return


###################FACTURA#################################################


@login_required
def crear_factura(request):
    form = FormBill(initial={'user': request.user})
    if request.method == 'POST':
        form = FormBill(request.POST, initial={'user': request.user})
        if request.user.id != int(form.data['user']):
            return redirect(crear_factura)
        if form.is_valid():
            form.save()
            id_bill = Bill.objects.filter(bill_number=form.data['bill_number'])[0].id 
            return redirect(detalle_factura, id=id_bill)
    context = {'form': form}
    return render(request, 'nuevaFactura.html', context)


@login_required
def listado_factura(request):
    facturas = Bill.objects.filter(user=request.user)
    context = {'items': facturas}
    return render(request, 'listado_facturas.html', context)


################DETALLE DE FACTURA############################################


@login_required
def crear_deatalle_factura(request):
    form = FormBillDetail(initial={'user': request.user})
    if request.method == 'POST':
        form = FormBillDetail(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(listado_factura)
    context = {'form': form}
    return render(request, 'nuevo_detalle_factura.html', context)

@login_required
def eliminar_detalle_factura(request, id):
    bill = Bill.objects.get(id=id)
    bill.delete()
    return redirect(detalle_factura)

@login_required
def detalle_factura(request, id):
    bill = Bill.objects.get(id=id)
    initial={
            'user': request.user, 
            'bill': bill
            }
    detalle = BillDetail.objects.filter(user=request.user, bill=bill)
    form = FormBillDetail(initial=initial)
    if request.method == 'POST':
        form = FormBillDetail(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            return redirect(detalle_factura, id=id)
    context = {
        'form': form,
        'items': detalle,
        'bill': bill
    }
    return render(request, 'listado_detalle_factura.html', context)


#####################CLIENTE###################################################


@login_required
def crear_cliente(request):
    form = FormClient(initial={'user': request.user})
    if request.method == 'POST':
        form = FormClient(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(listado_factura)
    context = {'form': form}
    return render(request, 'nuevo_cliente.html', context)



####################PROVEEDOR###################################################


@login_required
def crear_proveedor(request):
    form = FormProveedor(initial={'user': request.user})
    if request.method == 'POST':
        form = FormProveedor(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(listado_factura)
    context = {'form': form}
    return render(request, 'nuevo_proveedor.html', context)




