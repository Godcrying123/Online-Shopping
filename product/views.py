from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product

# Create your views here.


class IndexView(View):
    template_name = 'product/index.html'

    def get_context(self):
        firstCategories = Category.firstlevelcategory(Category)
        context = {
            'firstcategorylist': firstCategories,
        }
        return context

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)


class CategoryProductList(generic.ListView):
    model = Product
    template_namme = 'product/categorylist.html'
    paginate_by = 10



    def get_context(self, categoryslug):
        firstCategories = Category.firstlevelcategory(Category)
        if categoryslug == 'all':
            productlist = Product.objects.all()
        else:
            category = get_object_or_404(Category, slug=categoryslug)
            productlist = category.categoryproductlist()
        context = {
            'firstcategorylist': firstCategories,
            'productlist': productlist,
        }
        return context

    def get(self, request, *args, **kwargs):
        categoryslug = kwargs.get('categoryslug', 'all')
        context = self.get_context(categoryslug)
        productlist = context['productlist']
        paginator = Paginator(productlist, 2)
        page = self.request.GET.get('page', 1)
        try:
            currentPage = int(page)
            productpage = paginator.page(currentPage)
        except PageNotAnInteger:
            productpage = paginator.page(1)
        except EmptyPage:
            productpage = paginator.page(paginator.num_pages)
        context['productlist'] = productpage.object_list
        print(locals())
        return render(request, self.template_namme, locals())
