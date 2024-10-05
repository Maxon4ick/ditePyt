from django.shortcuts import get_object_or_404, render
from .models import NewsItem, NewsItemTag
from .paginator import paginator


def news(request):
    # object_list = NewsItem.objects.all()
    # objects = paginator(request, object_list, 1)
    #
    # return render(request, 'news/main_page.html', {'objects': objects})
    # # return render(request, 'news/main_page.html')
    items = NewsItem.objects.all()
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],  # For random css styles
    }

    return render(request, 'news/main_page.html', context)



def news_item_details(request, item_slug):
    item = get_object_or_404(NewsItem, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'news/item_details.html', context)


def news_tag_details(request, slug):
    tag = get_object_or_404(NewsItemTag, slug=slug)
    items = NewsItem.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }
    return render(request, 'news/tag_details.html', context)


def news_tag_list(request):
    tags = NewsItemTag.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
    }
    return render(request, 'news/tag_list.html', context)
