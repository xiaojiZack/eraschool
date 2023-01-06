import erajs.api as a

def shop_page():
    def buy(item,price):
        f = True
        for i in price:
            if a.sav()['资源'][i]<price[i]:
                f= False
                a.msg('{}不足'.format(i))
        if f:
            if not item in a.sav()['物品']:
                a.sav()['物品'][item] = 1
            else:
                a.sav()['物品'][item] += 1
            for i in price:
                a.sav()['资源'][i] -= price[i]
            a.msg('成功购买[{}]'.format(item))
            a.repeat()
    
    def check_tech(item):
        f = True
        tech = a.dat()['shop_item'][item]['科技需求']
        t = a.sav()['科技']
        for i in tech:
            if i=='无': return f
            elif not i in a.sav()['科技']: 
                f= False
        return f

    items = a.dat()['shop_item']
    a.page()
    a.t()
    a.t('{}G'.format(a.sav()['资源']['金钱']))
    a.divider()
    a.mode()
    a.t('持有物品:')
    for i in a.sav()['物品']:
        if a.sav()['物品'][i]>1:
            a.t('[{}]*{}'.format(i,a.sav()['物品'][i]))
        else:
            a.t('[{}]'.format(i))
    a.divider()
    a.mode('grid',4)
    for i in items:
        buyable = True
        price_text = ""
        if i in a.sav()['物品'] and items[i]['可重复'] == '否':
            buyable = False
            price_text = "售罄"
            a.t()
        elif check_tech(i): 
            for j in items[i]['价格']: price_text = price_text+j+ ":"+ str(items[i]['价格'][j])
            a.b('{}||{}'.format(i,price_text),buy,i,items[i]['价格'],disabled = not buyable,popup = '{}'.format(items[i]['描述']))
            a.t()
    a.divider()
    a.b('返回',a.back)
