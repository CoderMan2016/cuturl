from django.shortcuts import render
from .models import Link
from django.shortcuts import redirect
from django.template import loader
from django.template.base import Template
from django.http import HttpResponse
from random import choice
import string
import qrcode
from django.http import JsonResponse
import os
import qrcode.image.svg

def index(request):
    if request.is_ajax():
        if request.POST.get('link'):
            link = create_link(request.POST.get('link'))
            create_qr_jpg(link.short_link)
            create_qr_svg(link.short_link)
            return HttpResponse(loader.get_template('App/include/main-section.html').render({'short_link': link.short_link}, request))
        if request.POST.get('reset'):
            return HttpResponse(loader.get_template('App/include/main-section.html').render({}, request))

    return render(request, 'App/index.html')

def create_link(url):
    return Link.objects.create(url = url, short_link = generate_short_link())

def generate_short_link():
    short_url = ''.join(choice(string.ascii_lowercase) for i in range(4))
    return short_url if check_availability_short_link(short_url) else generate_short_link()

def check_availability_short_link(short_url):
    return False if Link.objects.filter(short_link = short_url).count() > 0 else True

def redirect_link(request, short_link):
    return redirect(Link.objects.get(short_link = short_link).url)

def API_URL(request):
    link = create_link(str(request.GET.get('url')))
    return JsonResponse({'short_link': link.short_link})

def create_qr_svg(link):
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make('https://cuturl.pythonanywhere.ru/' + link, image_factory=factory)
    img_file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/App/static/QR/', link + "_qr_.svg"), 'wb')
    img.save(img_file, 'SVG')
    img_file.close()

def create_qr_jpg(link):
    qr = qrcode.QRCode()
    qr.add_data('https://cuturl.pythonanywhere.ru/' + link)
    img = qr.make_image(fill_color="#4285F4", back_color="white")

    img_file = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/App/static/QR/', link + "_qr_.jpg"), 'wb')
    img.save(img_file, 'JPEG')
    img_file.close()
