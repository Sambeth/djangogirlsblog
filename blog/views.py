from django.shortcuts import render

# Create your views here.


def post_list(request):
    context = {}
    template = 'blog/post_list.html'
    return render(request, template, context)
