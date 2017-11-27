from django.views.generic import ListView

# Create your views here.
from .models import Post


class Home_page_view(ListView):
    model = Post
    template_name = "message_app/index.html"
