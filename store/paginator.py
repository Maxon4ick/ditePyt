from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

# def paginator(request, items, items_on_page):
#     paginator = Paginator(items, items_on_page)
#     page_number = request.GET.get('page')
#
#     return paginator.get_page(page_number)


def paginator(request, items, items_on_page):

    paginator = Paginator(items, items_on_page)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    return obj