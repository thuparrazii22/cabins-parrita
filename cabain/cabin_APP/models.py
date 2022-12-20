from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Region(models.Model):
    region_name = models.CharField(max_length=64, verbose_name='Región')

    def __str__(self):
        return self.region_name

class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Región')
    city_name = models.CharField(max_length=64, verbose_name='Ciudad')

    def __str__(self):
        return self.city_name

class Commune(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ciudad')
    commune_name = models.CharField(max_length=64, verbose_name='Comuna')

    def __str__(self):
        return self.commune_name

class Bank(models.Model):
    bank_name = models.CharField(max_length=30, verbose_name='Banco')

    def __str__(self):
        return self.bank_name

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_name = models.CharField(max_length=30, verbose_name='Método de pago')

    def __str__(self):
        return self.payment_name

class MeasureUnit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=20, verbose_name='Unidad de medida')
    symbol = models.CharField(max_length=20, verbose_name='Símbolo')

    def __str__(self):
        return self.symbol

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30, verbose_name='Nombre del producto')
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida')
    category = models.CharField(max_length=30, verbose_name='Categoría')

    def __str__(self):
        return self.product_name

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_rut = models.CharField(max_length=12, verbose_name='Rut Cliente')
    client_name = models.CharField(max_length=60, verbose_name='Nombre')
    client_last_name = models.CharField(max_length=60, verbose_name='Apellido')
    client_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ciudad')
    client_commune = models.ForeignKey(Commune, on_delete=models.CASCADE, verbose_name='Comuna')
    client_address = models.CharField(max_length=60, verbose_name='Dirección')

    def __str__(self):
        return self.client_name

class Proveedor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, verbose_name='Rut Proveedor')
    name = models.CharField(max_length=60, verbose_name='Nombre')
    last_name = models.CharField(max_length=60, verbose_name='Apellido')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ciudad')
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, verbose_name='Comuna')
    address = models.CharField(max_length=60, verbose_name='Dirección')
    
    def __str__(self):
        return self.name

class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_number = models.IntegerField(verbose_name='Número de factura')
    emision_date = models.DateTimeField(verbose_name='Fecha de emisión')
    supplier = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name='Proveedor')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    seller_name = models.CharField(max_length=60, verbose_name='Nombre vendedor')
    seller_last_name = models.CharField(max_length=60, verbose_name='Apellido vendedor')
    observations = models.CharField(max_length=120, verbose_name='Observaciones', blank=True, null=True)
    subtotal = models.IntegerField(verbose_name='Subtotal')
    iva = models.IntegerField(verbose_name='IVA')
    total = models.IntegerField(verbose_name='Total')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, verbose_name='Método de pago')
    limit_date = models.DateField(verbose_name='Fecha de vencimiento')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name='Banco', blank=True, null=True)
    iban = models.CharField(max_length=60, verbose_name='IBAN', blank=True, null=True)
    email = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Número de contacto')

    def __str__(self):
        return self.bill_number

class BillDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, verbose_name='Número factura')
    correlative = models.IntegerField(verbose_name='Correlativo')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    description = models.CharField(max_length=120 , verbose_name='Descripción', blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Cantidad')
    unitary_price = models.IntegerField(verbose_name='Precio unitario')
    discount = models.IntegerField(verbose_name='Descuento')
    total = models.IntegerField(verbose_name='Total')

    def __str__(self):
        return f'{self.bill}-{self.correlative}'
    
class Project(models.Model):
    project_name = models.CharField(max_length=60, verbose_name='Nombre Proyecto')
    surface = models.IntegerField(verbose_name='Superficie(m2)')
    total_price = models.IntegerField(verbose_name='Presupuesto', blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        return self.project_name

class ProjectDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto')
    product = models.ForeignKey(BillDetail, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return f'{self.project}-{self.product}'

class Worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=60, verbose_name='Nombre')
    last_names = models.CharField(max_length=60, verbose_name='Apellido')
    contact = models.IntegerField(verbose_name='Celular')

    def __str__(self):
        return f'{self.names} {self.last_names}'
    
class ProjectWorker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Trabajador')
    work = models.CharField(max_length=60, verbose_name='Trabajo')
    payment = models.IntegerField(verbose_name='Costo')
    balance = models.IntegerField(verbose_name='Deuda')