import random  #导入random 模块
from urllib.request import urlopen #导入urllib.request模块的urlopen方法
import sys #导入sys模块
WORD_URL = "http://learncodethehardway.org/words.txt" #词语的url给出了
WORDS = [] #定义一个WORD空列表

PHRASES = {
	"class %%%(%%%):":
	  "Make a class named %%% that is_a %%%.",
	"class %%%(object):\n\t def __init__(self,***)":
	  "class %%% has_a __init__ that takes self and *** params.",
	"class %%%(object):\n\t def ***(self,@@@)":
	  "class %%% has a function *** that takes self and @@@ params.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	  "From *** get the ***function,call it with params self and @@@.",
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'."
} #定义一个短语组成的字典

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english": #如果系统参数变量的长度为2，并且第二个参数变量为“english”
	PHRASE_FIRST = True #PHRASE_FIRST为True
else:
	PHRASE_FIRST = False
	
# load up the words form the website
for word in urlopen(WORD_URL).readlines(): #用word变量遍历打开的这个url所读取的每一行，
	WORDS.append(str(word.strip(),encoding="utf-8"))#把得到的word去空格，转为字符串，以utf-8编码，添加到WORDS空列表里面

print(WORDS)	
	 
def convert(snippet,phrase): #定义convert函数，它包含片段，短语两个参数
	
	#生成类名列表，把类名首字母都大写
	class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
	#从WORDS中随机选取snippet的“%%%”元素的个数个元素作为一个列表，w来遍历这个随机生成的列表，并且把w接收的列表元素的首字母都变成大写，
	#最后生成一个list，赋给class_names
	
	#生成其他名列表
	other_names = random.sample(WORDS,snippet.count("***"))
	#从WORDS中随机选取snippet中的“***”个数个元素，作为一个样本/抽样列表，返回给other_names。
	
	results = [] #返回结果结果列表（返回两个语句：key转化的question语句和value转化的answer语句）
	param_names = []#参数名列表
	
	#生成参数名列表
	for i in range(0,snippet.count("@@@")): #在0到snippet中“@@@”个数的范围内，循环，取到左边取不到右边，但总循环数还是“@@@”的个数
		param_count = random.randint(1,3) #生成一个指定范围内的随机整数，1-3都可以取到。
		param_names.append(','.join(random.sample(WORDS,param_count)))
		#在WORDS中随机选取1-3个元素组成一个列表，并且用','把列表中的元素连成一个字符串，再添加到param_names这个列表中
	
    #注意理解！！！！！！！！	
	for sentence in snippet, phrase: #sentence先等于snippet后等于phrase两个字符串！sentence分别等于snippet和phrase整体，然后分别整体返回给result（还是个字符串）。
		result = sentence[:]#并对sentence列表中的所有元素进行切片操作，返回给result列表
		
		#fake class names #改class名
		for word in class_names: #遍历刚才生成的首字母都是大写的class_names
			result = result.replace("%%%",word,1) #把result接收的snippet里的“%%%”用word一个一个替换掉，遍历结束生成一个新的result。
			
		#fake other names #改其他名字
		for word in other_names: #用word遍历other_names列表中的元素，
			result = result.replace("***",word,1) #用wrod一个一个替换掉result中的“***”，循环结束生成新的result
	
		# fake parameter lists #修改函数的参数列表
		for word in param_names: #遍历param_names列表（参数列表）
			result = result.replace("@@@",word,1)#用列表中的元素代替“@@@”，最后生成新的result
			
		results.append(result)
		#把更新后的result添加到results列表里面（先更新snippet代表的key，加进去，再更新phrase代表的value，生成新的results列表。）
	
	return results #convert函数最终返回results列表，它包含两个更新后的元素：更新后的key语句和value语句。
	
	
# keep going until they hit CTRL_D
try:
	while True:
		snippets = list(PHRASES.keys())#获取PHRASES中的keys，组成一个list，这就是snippets列表
		random.shuffle(snippets)#不返回值，直接就把该列表打乱放那了。
		
		for snippet in snippets:#在随机排序后的序列内遍历其元素
			phrase = PHRASES[snippet] #根据PHRASES中的key取其value值，赋给phrase.所以convert函数接收的就是：原PHRASES中的key和value值。
			question,answer = convert(snippet,phrase)#传入参数，key和value。返回问题和答案。
			if PHRASE_FIRST:#如果它为True
				question,answer = answer,question#互换
				
			print(question)
			
			input("> ")#试着输入答案
			print(f"ANSWER:  {answer}\n\n")#打印出答案
except EOFError:
	print("\nBYE")
	
	
