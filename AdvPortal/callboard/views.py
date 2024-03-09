from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.template import loader, TemplateDoesNotExist
from django.template.loader import get_template
from .models import Advert, Category

APP = 'callboard/'  # {% extends 'default.html' %}


def index(request):
    adv_category = Advert.objects.filter(is_active=True).select_related('category')[:10]
    categories = Category.objects.all()
    paginator = Paginator(adv_category, 2)  # количество элементов списка на одной странице
    if 'page' in request.GET:
        page_number = request.GET['page']   # номер текущей страницы из GET-запроса
    else:
        page_number = 1
    page = paginator.get_page(page_number)
    # page.object_list - список элементов на одной странице
    context = {'categories':  categories, 'page': page, 'adv_category': page.object_list}
    return render(request, APP + 'index.html', context)


def other_page(request, page):
    try:
        template = get_template(APP + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
