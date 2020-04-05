print("红楼梦人物出场次数：")
import jieba #jieba库的应用
excludes = {"什么","一个","我们","那里","你们","如今","说道","知道","起来","姑娘","这里","出来","他们","众人","自己",
            "一面","只见","怎么","两个","没有","不是","不知","这个","听见","这样","进来","咱们","告诉","就是","东西",
            "袭人","回来","大家","只是","只得","不敢","这些"
            }
           
            #列出需要删除的干扰词汇，在多次运行中不断添加来修正
           
txt = open("D:\红楼梦.txt","r",encoding='utf-8').read()

# 打开txt文件，格式是utf-8

words = jieba.lcut(txt)

#利用jieba库将红楼梦的所有语句分成词汇

counts = {}

#创建的一个空的字典

for word in words:
    if len(word) == 1:      #删去长度为1的词
        continue
    elif  word == "老太太":
          rword = "贾母"
    elif  word == "太太":
          rword = "王夫人"
    else:
          rword = word
          counts[word] = counts.get(word,0) + 1
    
    #如果字典中没有这个名字则创建，如果有就计数加一
    
for word in excludes:			
    del counts[word]
    
    #删除干扰词
    
items = list(counts.items())

#把保存[姓名：个数]的字典转换成列表

items.sort(key=lambda x:x[1],reverse = True)

#对上述列表进行排序，'True'是降序排列

for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count)) 

#输出前十个结果
