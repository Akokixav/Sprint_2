from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
import random
from account import models as amod


@view_function
def process_request(request):
    context = {
        'now': datetime.now(),
        'timecolor': random.choice(['red', 'blue', 'green', 'red']),
        # 'username': amod.FomoUser.objects.get(first_name = "Stephane").username,
    }
    context['users'] = amod.FomoUser.objects.all()
    print('>>>>>>>>>>', context)

    return dmp_render(request, 'index.html', context)
