from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .models import Profile
from django.template import loader
import pdfkit
import io


# Create your views here.
def accept_form(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        summary = request.POST.get("summary")
        degree = request.POST.get("degree")
        school = request.POST.get("school")
        university = request.POST.get("university")
        previous_work = request.POST.get("previous_work")
        skills = request.POST.get("skills")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)

        # print(profile)
        x = profile.save()


        redirect_url = reverse('details', kwargs={"id" : profile.pk})

        return redirect(redirect_url)

    return render(request, 'cv_pdf/accept.html', {"title":"Create CV"})


def view_all(request):
    profiles = Profile.objects.all()

    return render(request, "cv_pdf/all.html", {"title" : "All CVs", "profiles": profiles})


def details(request, id):
    profile = Profile.objects.get(pk=id)

    return render(request, 'cv_pdf/resume.html', context={"title" : "View", "profile":profile})


def download(request, id):
    profile = Profile.objects.get(pk=id)
    template = loader.get_template('cv_pdf/resume.html')
    html = template.render({"profile":profile})

    options = {
        "page-size": "Letter",
        "encoding": "UTF-8"
    }

    pdf = pdfkit.from_string(html, False, options=options)

    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = 'resume.pdf'
    return response
