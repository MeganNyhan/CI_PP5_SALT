from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


# Create your views here.


# all products view


def all_products(request):
    """ A view to show all products, including sorting and search queries """

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

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = '-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criterial")
                return redirect(reverse('products'))
            queries = Q(name_icontaines=query) | Q(description_icontaines=query)
            products = products.filter(queries)

    current_sorting = '{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):
    """ A view to show products in more detail """

    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()
    reviews = product.reviews.all().order_by('created_on')
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.product = product
        review.save()
        messages.success(request,
                         "Your review has been posted")
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'review_form': review_form,
        'reviews': reviews
    }

    return render(request, 'product_detail.html', context)


# add products view


@login_required
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# edit products view


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure\
                                     the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, 'You are editing {product.name}')

    template = 'edit-product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# delete products view


@login_required
def delete_product(request, product_id):
    """ Delete Product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Superusers can do this')
        return redirect(reverse, 'home')
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted Successfully!')
    return redirect(reverse('products'))
