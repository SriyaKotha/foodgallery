from django.shortcuts import redirect, render
from .forms import ImageForm, ImageUpdateForm
from .models import Image
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    img = Image.objects.all().order_by('id')
    paginator = Paginator(img, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ImageForm()
    return render(request=request, template_name="add_image.html", context={"image_form": form})

def edit_image(request, id):
    obj = Image.objects.get(id=id)
    if request.method == "POST":
        form = ImageUpdateForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ImageUpdateForm()
    ImgName = obj.ImgName
    return render(request, 'edit_image.html', {'form': form, 'ImgName': ImgName})

def view_image(request):
    return render(request, 'view_image.html')

def delete_image(request, id):
    Image.objects.get(id=id).delete()
    return redirect('/')

def search_image(request):
    name = request.GET.get('ImgName')
    data = Image.objects.filter(ImgName__icontains=name).order_by('id')
    paginator = Paginator(data, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html', {'page_obj': page_obj, 'name':name})
