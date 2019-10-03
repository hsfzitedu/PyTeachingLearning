from tkinter import Tk
from tkinter.ttk import Label, Button, Combobox, Style

HouseholdFoodWaste = ("菜叶","橙皮","葱","饼干","番茄酱","蛋壳","西瓜皮","马铃薯","鱼骨","甘蔗","玉米","骨头（鸡鸭鹅）","虾壳","蛋糕","面包","草莓","西红柿","梨","蟹壳","香蕉皮","辣椒","巧克力","茄子","豌豆皮","苹果","树叶","花生壳")

ResidualWaste = ("贝壳","化妆刷","海绵","发胶","卫生纸","旧镜子","桃核","陶瓷碗","一次性筷子","西梅核","坏的花盆","脏污衣服","烟蒂","湿垃圾袋 ","扫把","牙刷","过期化妆品","牙膏皮","水彩笔","调色板","打火机","荧光棒","医用手套","医用纱布","医用棉签","创口贴","注射器")

RecyclableWaste = ("塑料瓶","食品罐头","玻璃瓶","易拉罐","报纸","旧书包","旧手提包","旧鞋子","牛奶盒","旧塑料篮子","旧玩偶","玻璃壶","旧铁锅","垃圾桶","塑料梳子","旧帽子","旧夹子","废锁头","篮球","旧纸袋","纸盒","旧玩具","木质梳子","香水瓶","煤气罐")

HazardousWaste = ("油漆桶","电池","油漆","过期的胶囊药物","含汞温度计","过期药片","荧光灯","蓄电池","杀虫剂")

mainwin = Tk()

Label(mainwin, text="湿垃圾").pack()
Combobox(mainwin, values=HouseholdFoodWaste).pack()

Label(mainwin, text="干垃圾").pack()
Combobox(mainwin, values=ResidualWaste).pack()

Label(mainwin, text="可回收物").pack()
Combobox(mainwin, values=RecyclableWaste).pack()

Label(mainwin, text="有害垃圾").pack()
Combobox(mainwin, values=HazardousWaste).pack()
