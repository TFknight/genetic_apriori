import csv
import random

a ='红酒 啤酒 可乐 雪碧 芬达 冰红茶 橙汁 椰汁 柠檬茶 矿泉水 咖啡 白酒 牛奶 酸奶 奶茶 面包 饼干 豆干 薯片 薯条 百奇 猪肉 牛肉 羊肉 鸡肉 鸭肉 鱼肉 百叶 豆腐 茶干 鸡蛋 鸭蛋' \
   '鹌鹑蛋 鹅蛋 八角 桂皮 香叶 丁香 豆蔻 肉桂 陈皮 白芷 砂仁 当归 党参 胡萝卜 娃娃菜 大白菜 油菜 菜心 小青菜 卷心菜 包菜 西兰花 雷笋 茼蒿 京葱 小葱 芫荽 芹菜 豌豆头  木耳' \
   '香菇 平菇 蘑菇 金针菇 杏鲍菇 海鲜菇 香椿 茭白 扁豆 豇豆 花菜 四季豆 荷兰豆 年糕 猪蹄冻 火腿 红肠 苹果 梨子 青提 黑提 荔枝 枇杷 圣女果 火龙果 牛油果 龙眼 柠檬 李子 杏子' \
   '菜刀 砧板 漏勺 平底锅 砂锅 炒锅 电饭锅 电磁炉 铲子 筷子 搅拌机 空气炸锅 微波炉 烤箱 榨汁机 豆浆机 豆瓣酱 黄豆酱 甜面酱 海鲜酱 蚝油 老抽 生抽 鲜味生抽 米醋 白醋 香醋 陈醋' \
   '糖 冰糖 盐 鸡精 味精 小苏打 酵母粉 面粉 料酒 生粉 奶油 黄油 大豆油 菜籽油 尿布 推车 娃娃机 洗面奶 爽肤水 洁面乳 沐浴露 洗发露 肥皂 牙膏 牙刷 毛巾 脸盆 水牙线 面膜 粉底'
a=a.split()
len = a .__len__()
allThings=list()
csvFIle = open('test_01.csv','w',encoding='UTF-8')
writer = csv.writer(csvFIle)
i = 0
try:
    while i<10000:
        writer.writerow(random.sample(a,random.randint(1,len-1)))
        i = i+1
finally:
    csvFIle.close()

print(a)