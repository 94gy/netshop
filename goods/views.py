from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator
import math
# Create your views here.
class IndexView(View):
    def get(self, request, cid=3, num=1):
        cid = int(cid)
        num = int(num)
        #查询所有类别信息
        categorys = Category.objects.all().order_by('id')
        #查询当前类别下的所有信息
        goodsList = Goods.objects.filter(category_id=cid).order_by('id')
        #分页（每页显示八条记录）
        pager = Paginator(goodsList, 8)
        #获取当前页数据
        page_goodsList = pager.page(num)

        #每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin =1

        #每页结束页码
        end = begin + 9
        if end > pager.num_pages:
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pagelist = range(begin, end + 1)


        return render(request, 'index.html', {'categorys':categorys, 'goodsList':page_goodsList, 'currentcid':cid, 'pagelist':pagelist, 'currentNum':num})
#装饰器
def recommend_view(func):
    def wrapper(detailView, request, goodsid, *args, **kwargs):
        #将存放在cookie中的goodsid获取
        cookie_str = request.COOKIES.get('recommend','')

        #存放所有goodsid的列表
        goodsIdList = [gid for gid in cookie_str.split() if gid.strip()]
        #最终需要获取的推荐商品
        goodsObjList = [Goods.objects.get(id=gsid) for gsid in goodsIdList if gsid != goodsid and Goods.objects.get(id=gsid).category_id==Goods.objects.get(id=goodsid).category_id][:4]
        #将goodsObjList传递给get方法
        response = func(detailView, request, goodsid, goodsObjList, *args, **kwargs)
        #判断goodsid是否存在goodsIdList
        if goodsid in goodsIdList:
            goodsIdList.remove(goodsid)
            goodsIdList.insert(0, goodsid)
        else:
            goodsIdList.insert(0, goodsid)
        #将goodsIdList中的数据保存到COOkie中
        response.set_cookie('recommend', ' '.join(goodsIdList), max_age=3*24*60*60)

        return response
    return wrapper

class DetailView(View):
    @recommend_view
    def get(self, request, goods_id, recommendList=[]):

        goods_id = int(goods_id)

        #根据商品id查询商品详情信息
        goods = Goods.objects.get(id=goods_id)

        return render(request,'detail.html', {'goods':goods,'recommendList':recommendList})
