from django import forms
from cabin_APP.models import Client, BillDetail, Product, Region, City, Project, PaymentMethod, MeasureUnit, Worker, Bill
from django.contrib.auth.models import User

class FormUser(forms.ModelForm):
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
            'user': forms.HiddenInput
        }
        fields = '__all__'

class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        widgets = {
            'user': forms.HiddenInput
        }
        fields = '__all__'