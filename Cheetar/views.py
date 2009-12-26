# Create your views here.
import Cheetah.Django

def index(req):
    return Cheetah.Django.render('index.tmpl', greet=False)
