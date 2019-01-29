from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import *
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError
from django.utils.text import slugify


class ObjectDetailsMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact = slug)
        return render(request, self.template, context={
        self.model.__name__.lower(): obj, 'admin_object': obj, 'detail': True
        })


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj=get_object_or_404(self.model, slug__iexact=slug)
        bound_form=self.model_form(instance=obj)
        return render(request, self.template, context={
        'form': bound_form, self.model.__name__.lower(): obj
        })

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={
        'form': bound_form, self.model.__name__.lower(): obj
        })


class ObjectDeleteMixin:
    model = None
    template = None
    urll = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={
        self.model.__name__.lower(): obj
        })

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.urll))


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    try:
        new_slug = translit(new_slug, reversed=True)
    except LanguageDetectionError:
        pass
    return new_slug + '-' + str(int(time()))


class ObjectMixin:
    details_url = None
    update_url = None
    delete_url = None

    def get_absolute_url(self):
        return reverse(self.details_url, kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse(self.update_url, kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse(self.delete_url, kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
