from django.db.models import Value
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline

from goods.models import Products


def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query), is_active=True, category__is_active=True)
    
    vector = SearchVector("name", "description")
    search_query = SearchQuery(query)
    
    word_count = len(query.strip().split())
    if word_count <= 2:
        normalization = Value(2)
    else:
        normalization = Value(2).bitor(Value(4))
        
    result = (
        Products.objects
        .annotate(rank=SearchRank(vector, search_query, normalization=normalization))
        .filter(rank__gt=0, is_active=True, category__is_active=True)
        .order_by("-rank")
    )
    
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: rgba(201, 55, 137, 0.3);">',
            stop_sel='</span>',
        )
    )
    
    return result
    
    # keywords = [word for word in query.split() if len(word) > 2]
    
    # q_objects = Q()
    
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
        
    # return Products.objects.filter(q_objects)