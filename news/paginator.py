from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def paginator(request, items, items_on_page):
#     paginator = Paginator(items, items_on_page)
#     page_number = request.GET.get('page')
#
#     return paginator.get_page(page_number)

def paginator(request, items, items_on_page):
    # page = request.GET.get('page', 1)
    page = request.GET.get('page')
    paginator = Paginator(items, items_on_page)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects
