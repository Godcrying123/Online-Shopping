from django.shortcuts import render
from django.views import View
from .models import Category

# Create your views here.
def index(request):
    return render(request, 'product/index.html',)


class IndexView(View):
    template_name = 'product/index.html'

    def get_context(self):
        firstCategories = Category.firstlevelcategory(Category)
        for x in firstCategories:
            for y in x.secondlevelcategory():
                print(y)
        # secondCategories = Category.secondlevelcategory(firstCategories)
        context = {
            'firstcategorylist': firstCategories,
            # 'secondcategorylist': secondCategories,
        }
        return context

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)
