from urllib import request
import re
class Spider():
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<li class="game-live-item" .*>([\w\W]*?)</li>'
    name_pattern = '<i class="nick" title=".*">([\w\W]*?)</i>'
    number_pattern = '<i class="js-num">([\w\W]*?)</i></span>'

    def __fetch_content(self):
        # 获取网页HTML进行分析
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        # 分析HTML获取对应的主播名字和人气
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name_html = re.findall(Spider.name_pattern,html)
            number_html = re.findall(Spider.number_pattern,html)
            anchor = {'name':name_html,'number':number_html}
            anchors.append(anchor)
        return anchors

    def __refine(self,anchors):
        # 数据精炼
        l = lambda anchor :{'name':anchor['name'][0].strip(),
                            'number':anchor['number'][0]}
        return map(l,anchors)

    def __sort(self,anchors):
        # 排序
        anchors = sorted(anchors,key=self.__sort_col,reverse=True)
        return anchors

    def __sort_col(self,anchors):
        # 处理排序字段
        r = re.findall("\d+\.\d+?",anchors['number'])
        number = float(r[0])
        if '万' in anchors['number']:
            number *= 10000
        elif '千' in anchors['number']:
            number *= 1000
        return number

    def __show(self,anchors):
        # 展示
        for rank in range(len(anchors)):
            print('Rank  {:5s}   {:40s}   {:10s}   {:15s}'.format(str(rank+1),anchors[rank]['name'],anchors[rank]['number'],str(self.__sort_col(anchors[rank]))))


    def go(self):
        # 主函数
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)
        a = 1

spider = Spider()
spider.go()