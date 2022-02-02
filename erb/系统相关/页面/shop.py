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
    a.mode('grid',3)
    for i in items:
        if i in a.sav()['物品'] and items[i]['可重复'] == '否':
            pass
        else:
            a.b('{}'.format(i),buy,i,items[i]['价格'],popup = '{}'.format(items[i]['价格']))
            a.t()
    a.divider()
    a.b('返回',a.back)
