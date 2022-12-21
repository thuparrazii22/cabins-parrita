from django import forms
from .models import *
from django.contrib.auth.models import User

class FormUser(forms.ModelForm):
    #contrasena2 = forms.CharField(max_length=100)
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput
        }
        fields = ['password', 'username', 'first_name', 'last_name', 'email']

class FormRegion(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class FormCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class FormCreateProject(forms.ModelForm):
    class Meta:
        model = Project
        widgets = {
            'username': forms.HiddenInput
        }
        fields = '__all__'
    
class FormPaymentMethod(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormUnidadMedida(forms.ModelForm):
    class Meta:
        model = MeasureUnit
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormWorker(forms.ModelForm):
    class Meta:
        model = Worker
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormBill(forms.ModelForm):
    class Meta:
        model = Bill
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormBillDetail(forms.ModelForm):
    class Meta:
        model = BillDetail
        widgets = {
            'user': forms.HiddenInput,
            'quantity': forms.NumberInput(
                attrs={
                    'onkeyup': 'setPrecioTotal();'
                }
            ),
            'unitary_price': forms.NumberInput(
                attrs={
                    'onkeyup': 'setPrecioTotal();'
                }
            )
        }
        fields = '__all__'

class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormProjectDetail(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormProjectWorker(forms.ModelForm):
    class Meta:
        model = ProjectWorker
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'