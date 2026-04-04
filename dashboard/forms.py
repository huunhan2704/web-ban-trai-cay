from django import forms
from fruit_store.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'image', 'description']
        # Thêm class của Bootstrap để form đẹp hơn
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


from django import forms
from fruit_store.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] # Thường danh mục chỉ cần tên
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên danh mục...'}),
        }