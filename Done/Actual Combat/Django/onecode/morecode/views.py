from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse
import morecode.models as Models


# Create your views here.


def article_detail(request, article_id):
    # articles = get_object_or_404(Models.Articles, pk=article_id)
    # articles = Models.Articles.objects.filter(pk=1)
    # print(articles)
    # print(articles.__dict__)
    # article = {'title': articles.article_title, 'detail': articles.article_detail, 'details': articles.article_details}
    # return render(request, 'article_detail.html', {'articles': articles})
    return HttpResponse('文章id是:%s' % article_id)


# def articleinsert(request):
#     articles = Models.Articles(article_title='干脆面', article_detail="干脆面，一种即食型休闲食品。")
#     articles = Models.Articles(article_title='百度百科', article_detail="百度百科是百度公司推出的一部内容开放、自由的网络百科全书。")
#     articles = Models.Articles(article_title='百度', article_detail="百度（纳斯达克：BIDU"
#                                                                   "）是全球最大的中文搜索引擎，中国最大的以信息和知识为核心的互联网综合服务公司，全球领先的人工智能平台型公司。")
#     articles.save()
#     return HttpResponse('插入成功')


def article_list(request):
    articles = Models.Articles.objects.all()
    return render_to_response('article_list.html', {'articles': articles})
