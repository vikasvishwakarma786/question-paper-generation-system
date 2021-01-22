from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .model import User, Question, Createpaper


def index(request):
    if "email" in request.session:
        return redirect("add_question")
    return render(request, 'index.html')


def registration_view(request):
    return render(request, 'registration.html')


def registration_request(request):
    if request.method == "POST":
        reg_data = request.POST
        result = User.objects.raw("SELECT * FROM qupaper.userdetails WHERE email=\"" + reg_data['email'] + "\"")
        if len(result) > 0:
            messages.error(request, 'Email already exist...!')
            return redirect("registration_view")
        else:
            post = User()
            post.first_name = request.POST.get('first_name')
            post.last_name = request.POST.get('last_name')
            post.email = request.POST.get('email')
            post.password = request.POST.get('password')
            post.save()
            return redirect("http://127.0.0.1:8000")


def login_view(request):
    if "email" in request.session:
        return redirect("add_question")
    return render(request, 'login.html')


def login_request(request):
    global email
    email = request.POST['email']
    password = request.POST['password']
    result = User.objects.raw("SELECT * FROM qupaper.userdetails WHERE email=\"" + email + "\"")
    if len(result) > 0:
        if result[0].password == password:
            request.session["email"] = True
            request.session.set_expiry(0)
            return redirect("add_question")
        else:
            messages.error(request, 'invalid password')
            return redirect("login_view")
    else:
        messages.error(request, 'not registered')
        return redirect("login_view")


def add_question(request):
    if "email" in request.session:
        result = User.objects.raw("SELECT * FROM qupaper.userdetails WHERE email=\"" + email + "\"")
        name = result[0].first_name
        return render(request, 'addquestion.html', {'nm': name})
    return redirect("login_view")


def add_question_request(request):
    if request.method == "POST":
        quedata = request.POST
        post = Question()
        post.course = quedata['course']
        post.question = quedata['question']
        post.difficulty = quedata['difficulty']
        post.section = quedata['section']
        post.semester = quedata['semester']
        post.subject = quedata['subject']
        post.save()
        messages.success(request, 'SUCCESSFULLY ADDED')
        return render(request, "addquestion.html")


def createqpaper(request):
    if "email" in request.session:
        result = User.objects.raw("SELECT * FROM qupaper.userdetails WHERE email=\"" + email + "\"")
        name = result[0].first_name
        return render(request, 'createqpaper.html', {'nm': name})
    else:
        return redirect("login_view")


def create_request(request):
    if "email" in request.session:
        if request.method == "POST":
            createdata = request.POST
            print(type(createdata))
            post = Createpaper()
            post.course = createdata['course']
            post.semester = createdata['semester']
            post.subject = createdata['subject']
            post.difficulty = createdata['difficulty']
            post.noofsection = createdata['no_of_section']
            post.qps = createdata['no_of_question']
            post.code = createdata['code']
            post.cps = createdata['choice']
            post.time = createdata['time']
            post.marka = createdata['secA']
            var1 = int(createdata['no_of_question']) - 1
            var2 = int(createdata['no_of_question']) - 2
            var3 = {'a': var1, 'b': var2}
            if post.noofsection == '2':
                var4 = int(createdata['secB']) + int(createdata['secA'])
                var3.update({'c': var4})
                post.markb = createdata['secB']
                quesA = Question.objects.raw(
                    "SELECT * FROM qupaper.questions WHERE subject=\"" + post.subject + "\" and course=\"" + post.course +
                    "\" and difficulty=\"" + post.difficulty + "\" and section = \"A\" ORDER BY RAND() LIMIT " + post.qps + ";")
                quesB = Question.objects.raw(
                    "SELECT * FROM qupaper.questions WHERE subject=\"" + post.subject + "\" and course=\"" + post.course +
                    "\" and difficulty=\"" + post.difficulty + "\" and section = \"B\" ORDER BY RAND() LIMIT " + post.qps + ";")
                post.save()
                return render(request, 'paperpdf.html', {'A': quesA, 'B': quesB, 'cpp': createdata, 'var': var3})
            elif post.noofsection == '3':
                var4 = int(createdata['secB']) + int(createdata['secA']) + int(createdata['secC'])
                var3.update({'c': var4})
                post.markb = createdata['secB']
                post.markc = createdata['secC']
                quesA = Question.objects.raw(
                    "SELECT * FROM qupaper.questions WHERE subject=\"" + post.subject + "\" and course=\"" + post.course +
                    "\" and difficulty=\"" + post.difficulty + "\" and section = \"A\" ORDER BY RAND() LIMIT " + post.qps + ";")
                quesB = Question.objects.raw(
                    "SELECT * FROM qupaper.questions WHERE subject=\"" + post.subject + "\" and course=\"" + post.course +
                    "\" and difficulty=\"" + post.difficulty + "\" and section = \"B\" ORDER BY RAND() LIMIT " + post.qps + ";")
                quesC = Question.objects.raw(
                    "SELECT * FROM qupaper.questions WHERE subject=\"" + post.subject + "\" and course=\"" + post.course +
                    "\" and difficulty=\"" + post.difficulty + "\" and section = \"C\" ORDER BY RAND() LIMIT " + post.qps + ";")
                post.save()
                print(quesB[0].question)
                return render(request, 'paperpdf.html',
                              {'A': quesA, 'B': quesB, 'C': quesC, 'cpp': createdata, 'var': var3})
            post.save()
            quesA = Question.objects.raw(
                "SELECT * FROM qupaper.questions WHERE subject=\"" + post.subject + "\" and course=\"" + post.course +
                "\" and difficulty=\"" + post.difficulty + "\" and section = \"A\" ORDER BY RAND() LIMIT " + post.qps + ";")
            return render(request, 'paperpdf.html', {'A': quesA, 'cpp': createdata, 'var': var3})
    else:
        return redirect("login_view")


def show_question(request):
    if "email" in request.session:
        result = User.objects.raw("SELECT * FROM qupaper.userdetails WHERE email=\"" + email + "\"")
        name = result[0].first_name
        if request.method == "POST":
            infodata = request.POST
            x = infodata['course']
            y = infodata['subject']
            ques = Question.objects.raw(
                "SELECT * FROM qupaper.questions WHERE subject=\"" + y + "\" and course=\"" + x + "\"")
            print(ques[0].question)
            return render(request, 'showquestion.html', {'que': ques, 'nm': name})
        else:
            return render(request, 'showquestion.html', {'nm': name})
    else:
        return redirect("login_view")


def logout_request(request):
    request.session.set_expiry(0)
    logout(request)
    return redirect("http://127.0.0.1:8000")
