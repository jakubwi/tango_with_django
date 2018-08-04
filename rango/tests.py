from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders
from rango.models import Category

# Thanks to Enzo Roiz https://github.com/enzoroiz who made these tests during an internship with us

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('images/rango.jpg')
        self.assertIsNotNone(result)


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def add_cat(name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views = views
        c.likes = likes
        c.save()
        return c

    def test_index_view_with_categories(self):
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_cats =len(response.context['categories'])
        self.assertEqual(num_cats , 4)