from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from reviews.models import ReviewsAndRatings
from .models import Product, Category, Reviews
from .forms import ProductForm, ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all products, to sort and search the products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction =='desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You have not submitted a valid search")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual products and details """

    product = get_object_or_404(Product, pk=product_id)

    reviews = Reviews.objects.filter(product=product)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')

        if comment:
            reviews = Reviews.objects.create(
                product=product,
                rating=rating,
                # comment=comment,
                name=request.user
            )

            messages.success(request, 'You have rated this item!')
        else:
            messages.error(request,'Someting went wrong')

    template = 'products/product_detail.html'


    context = {
        "product": product,
        'reviews': reviews,
    }

    return render(request, template, context)

@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owner can do this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have sccessfully added a new product')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please check your form is valid')

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form':form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owner can do this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Successfully Updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update prouct. Please check the edit form is valid.')
    else:

        form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owner can do this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')
    return redirect(reverse('products'))


@login_required
def review_product(request):
    """
    A view to to add reviews and tratings to products
    """

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have sccessfully reviewed this product')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to review product. Please check your form is valid')

    else:
        form = ReviewForm()

    template = 'products/review_product.html'
    context = {
        'form':form,
    }

    return render(request, template, context)
