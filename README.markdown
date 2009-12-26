Django/Cheetah Example
=========================

This is a simple project and application demonstrating
using Cheetah (with dynamically compiled templates) for 
building views inside of [Django](http://www.djangoproject.com/) 
applications.

Requires
----------
 * [Django](http://www.djangoproject.com/)
 * [Cheetah](http://cheetahtemplate.org) (>= v2.2.1)

Getting Started
-----------------
For all intents and purposes, using Cheetah in place of Django's
templating system is a trivial change in how you write your *views*. 

After following the Django [getting started](http://docs.djangoproject.com/en/1.1/intro/tutorial01/) 
documentation, you'll want to create a directory for your Cheetah templates, such 
as `Cheetar/templates`. Be sure to `touch __init__.py` in your template 
directory to ensure that templates can be imported if they need to.

Add your new template directory to the `TEMPLATE_DIRS` attribute
in your project's `settings.py`. 

Once that is all set up, utilizing Cheetah templates in Django is just 
a matter of a few lines in your view code:

    import Cheetah.Django

    def index(req):
        return Cheetah.Django.render('index.tmpl', greet=False)

**Note**: Any keyword-arguments you pass into the `Cheetah.Django.render()` 
function will be exposed in the template's "searchList", meaning you can
then access them with $-placeholders. (i.e. `$greet`)
