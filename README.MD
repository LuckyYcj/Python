    -basis: 基础
    -database: 数据库
    -demo: 实例
    -emailutil: 邮件发送
    -file: 文件操作
    -module-os: 操作系统
    -reptile: 爬虫
    -tools: 实用工具


python 基础：

https://www.runoob.com/python3/python3-examples.html

pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
比如我要安装 Django。用以下的一条命令就可以，方便快捷。
pip install Django==1.7
升级包
pip install --upgrade SomePackage
升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。
卸载包
pip uninstall SomePackage
搜索包
pip search SomePackage
显示安装包信息
pip show
查看指定包的详细信息
pip show -f SomePackage
列出已安装的包
pip list
查看可升级的包
pip list -o

基础：
1. r'' '' 默认不转义
2. ''' '''多行内容
3. len()函数可以获得list元素的个数
4. list insert() pop()删除末尾元素 pop(i)删除指定位置元素
5. tuple 元祖 有序列表  tuple一旦初始化就不能修  元祖指向的list 是可变的
6. int() 转换类型
7. for...in循环  while循环  break语句可以提前退出循环  continue语句，跳过当前的这次循环，直接开始下一次循环   for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
8. range()函数 生成一个整数序列 range(5) --> 0 1 2 3 4 5
9. dict全称dictionary 字典 使用键-值（key-value）存储，具有极快的查找速度  要避免key不存在的错误，有两种办法，
		一是通过in判断key是否存在：'Thomas' in d
		二是通过dict提供的get()方法，如果key不存在，可以返回None
		要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

10. set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。 要创建一个set，需要提供一个list作为输入集合  s = set([1, 2, 3])
11. 使用内建的isinstance函数可以判断一个变量是不是字符串：
12. list() 遍历函数

函数：
1. 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号: 然后，在缩进块中编写函数体，函数的返回值用return语句返回
	def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
2. from 文件名 import 函数名
3. 如果想定义一个什么事也不做的空函数，可以用pass语句
4. 函数可以同时返回多个值，但其实就是一个tuple
5. import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
6. 默认参数 定义默认参数要牢记一点：默认参数必须指向不变对象！
7. 可变函数  *nums表示把nums这个tuple的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
8. 关键字参数 **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
9. 命名关键字参数
10. 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

高级特性：
1. 切片(Slice)
2. 迭代(Iteration)
3. 列表生成式即List Comprehensions  写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，x * x for x in range(1, 11)]
4. 生成器
5. 迭代器

函数：
1. Python内建了map()和reduce()函数
	map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
		>>> def f(x):
		...     return x * x
		...
		>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
		>>> list(r)
		[1, 4, 9, 16, 25, 36, 49, 64, 81]
	reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
2. 内建的filter()函数用于过滤序列  和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
3. 内置的sorted()函数就可以对list进行排序  它还可以接收一个key函数来实现自定义的排序
	sorted([36, 5, -12, 9, -21], key=abs)
	[5, 9, -12, -21, 36]


五种数据类型：
Number String List Tuple Dictionary
Number(int, float, bool, complex) 二进制 0b 八进制 0o  十六进制 0x
type() 查看变量类型
String ''' '''多行内容(三个单引号) 切片访问 str[0:1] String不支持修改
List 可以负向索引获取 切片访问 list[0:2] for in 遍历
Tuple 元祖 有序列表  tuple一旦初始化就不能修 切片访问 Tuple[0:2]
Dictionary key-value

输入输出函数 input() print()

while 循环

函数

面向对象编程 （OOP）
类， 对象， 实例化， 实例变量， 方法

文件的读写
打开文件 open()

图形界面


常用工具包:

01 文件读写:
文件的读写包括常见的txt、Excel、xml、二进制文件以及其他格式的数据文本，主要用于本地数据的读写。

open(name[, mode[, buffering]])  [Python内置函数]Python默认的文件读写方法  ★★★
numpy.loadtxt、numpy.load和numpy.fromfile  [第三方库]Numpy自带的读写函数，包括loadtxt、load和fromfile，用于文本、二进制文件读写 ★★★
pandas.read_*  [第三方库]Pandas自带的read文件方法，例如ead_csv、read_fwf、read_table等，用于文本、Excel、二进制文件、HDF5、表格、SAS文件、SQL数据库、Stata文件等的读写  ★★★
xlrd  [第三方库]用于Excel文件读取  ★★
xlwt  [第三方库]用于Excel文件写入  ★★
pyexcel-xl  [第三方库]用于Excel文件读写  ★★
xluntils  [第三方库]用于Excel文件读写  ★★
pyExcelerator  [第三方库]用于Excel文件读写  ★
openpyxl  [第三方库]用于Excel文件读写  ★
lxml  [第三方库]xml和HTML读取和解析  ★★★
xml  [Python标准库]xml对象解析和格式化处理  ★★★
libxml2  [第三方库]xml对象解析和格式化处理  ★
xpath  [第三方库]xml对象解析和格式化处理  ★★
win32com  [第三方库]有关Windows系统操作、Office（Word、Excel等）文件读写等的综合应用库  ★


02 网络抓取和解析
网络抓取和解析用于从互联网中抓取信息，并对HTML对象进行处理，有关xml对象的解析和处理的库在“1.文件读写”中找到。

requests  [第三方库]网络请求库，提供多种网络请求方法并可定义复杂的发送信息  ★★★
urllib  [Python标准库] Python自带的库，简单的读取特定URL并获得返回的信息  ★★
urllib2  [Python标准库] Python自带的库，读取特定URL并获得返回的信息，相对于urllib可处理更多HTTP信息，例如cookie、身份验证、重定向等  ★★
urlparse  [Python标准库] Python自带的URL解析库，可自动解析URL不同的域、参数、路径等  ★★★
HTMLParser  [Python标准库]Python自带的HTML解析模块，能够很容易的实现HTML文件的分析  ★★★
Scapy  [第三方库]分布式爬虫框架，可用于模拟用户发送、侦听和解析并伪装网络报文，常用于大型网络数据爬取  ★★★
Beautiful Soup  [第三方库]Beautiful Soup是网页数据解析和格式化处理工具，通常配合Python的urllib、urllib2等库一起使用  ★★★


03 数据库连接
数据库连接可用于连接众多数据库以及访问通用数据库接口，可用于数据库维护、管理和增、删、改、查等日常操作。

mysql-connector-python  [第三方库]MySQL官方驱动连接程序  ★★★
MySQL-python  [第三方库]MySQL连接库  ★★
cx_Oracle  [第三方库]Oracle连接库  ★★★
psycopg2  [第三方库]Python编程语言中非常受欢迎的PostgreSQL适配器  ★★★
redis  [Python标准库]Redis连接库  ★★★
pymongo  [第三方库]MongoDB官方驱动连接程序  ★★★
HappyBase  第三方库]HBase连接库  ★★★
py2neo  [第三方库]Neo4j连接库  ★★★
cassandra-driver  [第三方库] Cassandra（1.2+）和DataStax Enterprise（3.1+）连接库  ★★★
sqlite3  [Python标准库] Python自带的模块，用于操作SQLite数据库  ★★★
pysqlite2  [第三方库] SQLite 3.x连接库  ★★
bsddb3  [第三方库]Berkeley DB连接库 bsddb3
bsddb  [Python标准库] Python自带的模块，提供了一个到Berkeley DB库的接口  ★★
dbhash  [Python标准库] Python自带的模块，dbhash模块提供了使用BSD数据库库打开数据库的功能。该模块镜像了提供对DBM样式数据库访问的其他Python数据库模块的接口。 bsddb模块需要使用dbhash  ★★
adodb  [第三方库] ADOdb是一个数据库抽象库，支持常见的数据和数据库接口并可自行进行数据库扩展，该库可以对不同数据库中的语法进行解析和差异化处理，具有很高的通用性  ★★★
SQLObject  [第三方库] SQLObject是一种流行的对象关系管理器，用于向数据库提供对象接口，其中表为类、行为实例、列为属性  ★★
SQLAlchemy  [第三方库] SQLAlchemy是Python SQL工具包和对象关系映射器，为应用程序开发人员提供了SQL的全部功能和灵活性控制  ★★
ctypes  [第三方库] ctypes是Python的一个外部库，提供和C语言兼容的数据类型，可以很方便地调用C DLL中的函数  ★★★
pyodbc  [第三方库] Python通过ODBC访问数据库的接口库  ★★★
Jython  [第三方库] Python通过JDBC访问数据库的接口库  ★★★

04 数据清洗转换
数据清洗转换主用于数据正式应用之前的预处理工作。

frozenset([iterable])  [Python内置函数]返回一个新的frozenset对象，可选择从iterable取得的元素  ★★★
int(x)  [Python内置函数]返回x的整数部分  ★★★
isinstance(object, classinfo)  [Python内置函数]返回object是否是指定的classinfo实例信息  ★★★
len(s)  [Python内置函数]返回对象的长度或项目数量  ★★★
long(x)  [Python内置函数]返回由字符串或数字x构造的长整型对象  ★★★
max(iterable[, key])  [Python内置函数]返回一个可迭代或最大的两个或多个参数中的最大项  ★★★
min(iterable[, key])  [Python内置函数]返回一个可迭代或最大的两个或多个参数中的最小项  ★★★
range(start, stop[, step])  [Python内置函数]用于与for循环一起创建循环列表，通过指定start（开始）、stop（结束）和step（步长）控制迭代次数并获取循环值  ★★★
raw_input(prompt)  [Python内置函数]捕获用户输入并作为字符串返回（不推荐使用input作为用户输入的捕获函数） ★★★
round(number[, ndigits])  [Python内置函数]返回number小数点后ndigits位的四舍五入的浮点数  ★★★
set([iterable])  [Python内置函数]返回一个新的集合对象，可选择从iterable获取的元素  ★★★
slice(start, stop[, step])  [Python内置函数]返回表示由范围（start、stop、step）指定的索引集的切片对象  ★★
sorted(iterable[, cmp[, key[, reverse]]])  [Python内置函数]从iterable的项中返回一个新的排序列表  ★★★
xrange(start, stop[, step])  [Python内置函数]此函数与range()非常相似，但返回一个xrange对象而不是列表  ★★★
string  [Python标准库]字符串处理库，可实现字符串查找、分割、组合、替换、去重、大小写转换及其他格式化处理  ★★★
re[Python标准库]正则表达式模块，在文本和字符串处理中经常使用  ★★★
random  [Python标准库]该模块为各种分布实现伪随机数生成器，支持数据均匀分布、正态（高斯）分布、对数正态分布、负指数分布、伽马和β分布等  ★★★
os  [Python标准库]用于新建、删除、权限修改、切换路径等目录操作，以及调用执行系统命令  ★★★
os.path  [Python标准库]针对目录的遍历、组合、分割、判断等操作，常用于数据文件的判断、查找、合并  ★★★
prettytable  [Python标准库]格式化表格输出模块  ★★
json  [Python标准库]Python对象与json对象的转换  ★★★
base64  [Python标准库]将任意二进制字符串编码和解码为文本字符串的Base16，Base32和Base64  ★★★

05 数据计算和统计分析
数据计算和统计分析主要用于数据探查、计算和初步数据分析等工作。

numpy  [第三方库]NumPy是Python科学计算的基础工具包，很多Python数据计算工作库都依赖它  ★★★
scipy  [第三方库]Scipy是一组专门解决科学和工程计算不同场景的主题工具包  ★★★
pandas  [第三方库]Pandas是一个用于Python数据分析的库，它的主要作用是进行数据分析。Pandas提供用于进行结构化数据分析的二维的表格型数据结构DataFrame，类似于R中的数据框，能提供类似于数据库中的切片、切块、聚合、选择子集等精细化操作，为数据分析提供了便捷  ★★★
statsmodels  [第三方库]Statsmodels是Python的统计建模和计量经济学工具包，包括一些描述性统计、统计模型估计和统计测试，集成了多种线性回归模型、广义线性回归模型、离散数据分布模型、时间序列分析模型、非参数估计、生存分析、主成分分析、核密度估计以及广泛的统计测试和绘图等功能  ★★★
abs(x)  [Python内置函数]返回x的绝对值  ★★★
cmp(x, y)  [Python内置函数]比较两个对象x和y，并根据结果返回一个整数。 如果x <y，则返回值为负数，如果x == y则为零，如果x> y则返回值为正  ★★
float(x)  [Python内置函数]返回从数字或字符串x构造的浮点数  ★★★
pow(x, y[, z])  [Python内置函数]返回x的y次幂。如果z存在，则返回x的y次幂，模z  ★★★
sum(iterable[, start])  [Python内置函数]从左到右依次迭代，返回总和  ★★★
math  [Python标准库]数学函数库，包括正弦、余弦、正切、余切、弧度转换、对数运算、圆周率、绝对值、取整等数学计算方法  ★★★
cmath  [Python标准库]与math基本一致，区别是cmath运算的是复数★★
decimal[Python标准库]10进制浮点运算★★
fractions[Python标准库]分数模块提供对有理数算术的支持★★

06 自然语言处理和文本挖掘
自然语言处理和文本挖掘库主要用于以自然语言文本为对象的数据处理和建模。

nltk  [第三方库]NLTK是一个Python自然语言处理工具，它用于对自然语言进行分类、解析和语义理解。目前已经有超过50种语料库和词汇资源★★★
pattern  [第三方库]Pattern是一个网络数据挖掘Python工具包，提供了用于网络挖掘（如网络服务、网络爬虫等）、自然语言处理（如词性标注、情感分析等）、机器学习（如向量空间模型、分类模型等）、图形化的网络分析模型★★★
gensim  [第三方库]Gensim是一个专业的主题模型（发掘文字中隐含主题的一种统计建模方法）Python工具包，用来提供可扩展统计语义、分析纯文本语义结构以及检索语义上相似的文档★★★
结巴分词  [第三方库]结巴分词是国内流行的Python文本处理工具包，分词模式分为三种模式：精确模式、全模式和搜索引擎模式，支持繁体分词、自定义词典等，是非常好的Python中文分词解决方案，可以实现分词、词典管理、关键字抽取、词性标注等★★★
SnowNLP  [第三方库]SnowNLP是一个Python写的类库，可以方便的处理中文文本内容。该库是受到了TextBlob的启发而针对中文处理写的类库，和TextBlob不同的是这里没有用NLTK，所有的算法都是自己实现的，并且自带了一些训练好的字典★★
smallseg  [第三方库] Smallseg是一个开源的、基于DFA的轻量级的中文分词工具包。可自定义词典、切割后返回登录词列表和未登录词列表、有一定的新词识别能力★★
spaCy  [第三方库] spaCy是一个Python自然语言处理工具包，它结合Python和Cython使得自然语言处理能力达到了工业强度★★★
TextBlob  [第三方库]TextBlob 是一个处理文本数据的Python库，可用来做词性标注、情感分析、文本翻译、名词短语抽取、文本分类等★★
PyNLPI  [第三方库] PyNLPI是一个适合各种自然语言处理任务的集合库，可用于中文文本分词、关键字分析等，尤其重要的是其支持中英文映射，支持UTF-8和GBK编码的字符串等★★★

07 图像和视频处理
图像处理和视频处理主要适用于基于图像的操作、处理、分析和挖掘，如人脸识别、图像识别、目标跟踪、图像理解等。

PIL  [第三方库]PIL是一个常用的图像读取、处理和分析的库，提供了多种数据处理、变换的操作方法和属性★★
OpenCV  [第三方库]OpenCV是一个强大的图像和视频工作库。它提供了多种程序接口，支持跨平台（包括移动端）应用。OpenCV的设计效率很高，它以优化的C / C ++编写，库可以利用多核处理。除了对图像进行基本处理外，还支持图像数据建模，并预制了多种图像识别引擎，如人脸识别★★★
scikit-image  [第三方库] scikit-image（也称skimage）是一个图像处理库，支持颜色模式转换、滤镜、绘图、图像处理、特征检测等多种功能★★
imageop  [Python标准库] Python自带的函数，对图像基本操作，包括裁剪、缩放、模式转换★
colorsys  [Python标准库] Python自带的函数，实现不同图像色彩模式的转换★
imghdr  [Python标准库] Python自带的函数，返回图像文件的类型★

08 音频处理
音频处理主要适用于基于声音的处理、分析和建模，主要应用于语音识别、语音合成、语义理解等。

TimeSide  [第三方库] TimeSide是一个能够进行音频分析、成像、转码、流媒体和标签处理的Python框架，可以对任何音频或视频内容非常大的数据集进行复杂的处理★★★
audiolazy  [第三方库]audiolazy是一个用于实时声音数据流处理的库，支持实时数据应用处理、无限数据序列表示、数据流表示等★★
pydub  [第三方库] pydub支持多种格式声音文件，可进行多种信号处理（例如压缩、均衡、归一化）、信号生成（例如正弦、方波、锯齿等）、音效注册、静音处理等★★★
audioop  [Python标准库] Python自带的函数，可实现对声音片段的一些常用操作★★
tinytag  [第三方库] tinytag用于读取多种声音文件的元数据，涵盖MP3、OGG、OPUS、MP4、M4A、FLAC、WMA、Wave等格式★★
aifc  [Python标准库] Python自带的函数，读写AIFF和AIFC文件★
sunau  [Python标准库] Python自带的函数，读写Sun AU文件★
wave  [Python标准库] Python自带的函数，读写WAV文件★★
chunk  [Python标准库] Python自带的函数，读取EA IFF 85块格式的文件★
sndhdr  [Python标准库] Python自带的函数，返回声音文件的类型★
ossaudiodev  [Python标准库]该模块支持访问OSS（开放声音系统）音频接口★★★

09 数据挖掘/机器学习/深度学习
数据挖掘、机器学习和深度学习等是Python进行数据建模和挖掘学习的核心模块。

Scikit-Learn  [第三方库]scikit-learn（也称SKlearn）是一个基于Python的机器学习综合库，内置监督式学习和非监督式学习机器学习方法，包括各种回归、聚类、分类、流式学习、异常检测、神经网络、集成方法等主流算法类别，同时支持预置数据集、数据预处理、模型选择和评估等方法，是一个非常完整、流行的机器学习工具库★★★
TensorFlow  [第三方库]TensorFlow 是谷歌的第二代机器学习系统，内建深度学习的扩展支持，任何能够用计算流图形来表达的计算，都可以使用 TensorFlow★★★
NuPIC  [第三方库] NuPIC是一个以HTM（分层时间记忆）学习算法为工具的机器智能平台。NuPIC适合于各种各样的问题，尤其适用于检测异常和预测应用★★★
Orange  [第三方库] Orange通过图形化操作界面，提供交互式数据分析功能，尤其适用于分类、聚类、回归、特征选择和交叉验证工作★★★
theano  [第三方库] Theano是非常成熟的深度学习库。它与Numpy紧密集成，支持GPU计算、单元测试和自我验证★★★
keras  [第三方库] Keras是一个用Python编写的高级神经网络API，能够运行在TensorFlow或者Theano之上，它的开发重点是实现快速实验★★
neurolab  [第三方库] Neurolab是具有灵活网络配置和Python学习算法的基本神经网络算法库。它包含通过递归神经网络（RNN）实现的不同变体，该库是同类RNN API中最好的选择之一★★
PyLearn2  [第三方库] PyLearn2是基于Theano的深度学习库，它旨在提供极大的灵活性，并使研究人员可以进行自由可控制，参数和属性的灵活、开放配置是亮点★★★
OverFeat  [第三方库] OverFeat是一个深度学习库，主要用于图片分类、定位物体检测★★
Pyevolve  [第三方库] Pyevolve是一个完整的遗传算法框架，也支持遗传编程★★
Caffe  [第三方库] Cafffe是一个深度学习框架，主要用于计算机视觉，它对图像识别的分类具有很好的应用效果★★

10 数据可视化
数据可视化主要用于做数据结果展示、数据模型验证、图形交互和探查等方面。

Matplotlib  [第三方库] Matplotlib是Python的2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形，开发者可以仅需要几行代码，便可以生成多种高质量图形★★★
seaborn  [第三方库] Seaborn是在Matplotlib的基础上进行了更高级的API封装，它可以作为Matplotlib的补充★★
bokeh  [第三方库] Bokeh是一种交互式可视化库，可以在WEB浏览器中实现美观的视觉效果★★★
Plotly  [第三方库] Plotly提供的图形库可以进行在线WEB交互，并提供具有出版品质的图形，支持线图、散点图、区域图、条形图、误差条、框图、直方图、热图、子图、多轴、极坐标图、气泡图、玫瑰图、热力图、漏斗图等众多图形★★★
VisPy  [第三方库] VisPy是用于交互式科学可视化的Python库，旨在实现快速，可扩展和易于使用★★
PyQtGraph  [第三方库] PyQtGraph是一个建立在PyQt4 / PySide和numpy之上的纯Python图形和GUI库，主要用于数学/科学/工程应用★★
ggplot  [第三方库] ggplot是用Python实现的图形输出库，类似于 R中的图形展示版本★★★

11 交互学习和集成开发
交互学习和集成开发主要用来做Python开发、调试和集成之用，包括Python集成开发环境和IDE。

IPython  [第三方库]IPython 是一个基于Python 的交互式shell，比默认的Python shell 好用得多，支持变量自动补全、自动缩进、交互式帮助、魔法命令、系统命令等，内置了许多很有用的功能和函数★★★
Elpy  [第三方库] Elpy是Emacs用于Python的开发环境，它结合并配置了许多其他软件包，它们都是用Emacs Lisp和Python编写的★★
PTVS  [第三方库] Visual Studio 的 Python 工具★★
PyCharm  [外部工具]PyCharm带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、项目管理、代码跳转、智能提示、自动完成、单元测试、版本控制并可集成IPython、系统终端命令行等，在PyCharm里几乎就可以实现所有有关Python工作的全部过程★★★
LiClipse  [外部工具] LiClipse是基于Eclipse的免费多语言 IDE，通过其中的PyDev可支持 Python开发应用★★
Spyder  [外部工具] Spyder是一个开源的Python IDE，由IPython和众多流行的Python库的支持，是一个具备高级编辑、交互式测试、调试以及数字计算环境的交互式开发环境★★

12 其他Python协同数据工作工具
其他Python协同数据工作工具指除了上述主题以外，其他在数据工作中常用的工具或库。

tesseract-ocr  [外部工具]这是一个Google支持的开源OCR图文识别项目，支持超过200种语言（包括中文），并支持自定义训练字符集，支持跨Windows、Linux、Mac OSX 多平台使用★★★
RPython  [第三方库]R集成库★★★
matpython  [第三方库]MATLAB集成库★★★
Lunatic Python  [第三方库]Lua集成库★★
PyCall.jl  [第三方库]Julia集成库★★
PySpark  [第三方库] Spark提供的Python API★★★
dumbo  [第三方库] 这个模块可以让Pythoner轻松的编写和运行 Hadoop 程序，程序版本比较早，可以作为参考★★
dpark  [第三方库]Python对Spark的克隆版本，类MapReduce框架★★
streamparse  [第三方库]Streamparse允许通过Storm对实时数据流运行Python代码★★★





一门语言好用、方便的程度在很多时候会取决于这门语言相关的库够不够丰富，Python 之所以火爆除了其本身的语法和特性之外，还在一定程度上取决于其有太多太多库的支持，不论是官方维护的还是第三方开发的。就比如说做机器学习为什么很多人都用 Python，一个非常大的因素就是 TensorFlow 和 PyTorch 对 Python 的支持。当然在这里并不是说 Python 的库真的就全的不要不要的，它在某些领域或者项目的生态还是有待完善的。

正好昨天刷到知乎一个问题「你见过哪些相见恨晚的 Python 库？」，其意就是想了解下有哪些非常好用的提高生产力的 Python 库。一些回答直接把 awesome-python 贴过来，点赞非常多，当然多归多，但是里面很多都是些过期的或者其实没太有什么价值的库，反而会增加了挑选库的成本。我大体上把一些回答过了一遍，另外结合自己平时了解的内容，稍微对一些基础生产力库做了简单的梳理，在这里分享给大家。

所以这里就不再针对于一些特殊的场景推荐了，如一些 Web开发库、网络请求库、数据操作库、数据分析库、机器分析库等等。下面主要罗列一些适用范围和方向较广，对于一些基础设施的建设比较有用，能在多数场景下提高 Python 生产力的库，描述比较简单，主要是提供一个列表，仅供参考哈。

attrs、cattrs

GitHub：https://github.com/python-attrs/attrs、https://github.com/Tinche/cattrs

简化类的定义、序列化反序列化等操作。

个人写的简介：https://mp.weixin.qq.com/s/oHK-Y4lOeaQCFtDWgqXxFA

loguru

GitHub：https://github.com/Delgan/loguru

可简化日志记录写法。

个人写的简介：https://mp.weixin.qq.com/s/5Ri1WS5cTGCNAQ0I_zYycg

autopep8

GitHub：https://github.com/hhatto/autopep8

把 Python 代码转成符合 PEP8 规范的代码。

psutil

GitHub：https://github.com/giampaolo/psutil

Python 实现任务监控的库。

furl

GitHub：https://github.com/gruns/furl

对 url 的处理非常方便，比 urllib 等库好用多。

retrying、tenacity

GitHub：https://github.com/rholder/retrying、https://github.com/jd/tenacity

异常重试库，如出错之后重试多少次，尤其在发起一些 HTTP 请求时非常有用，当然也能用于其他地方。

typing

Docs：https://docs.python.org/zh-cn/3/library/typing.html#module-typing

对 Python 类型的支持，支持多种类型、嵌套类型，也推荐多多使用 Python 的类型注解。

argparse

Docs：https://docs.python.org/zh-cn/3/library/argparse.html

个人曾经使用过几个命令行解析工具，如 docopt，但后来还是转回来了 argparse，功能齐全强大。

absl-py

GitHub：https://github.com/abseil/abseil-py

个人感觉比 argparse 更易用的库，如 TensorFlow 就在使用这个，对于定义一些 Flag 非常方便。

pipenv

GitHub：https://github.com/pypa/pipenv

功能更全的包管理工具，集成虚拟环境、支持 Lock 机制锁定安装包版本和依赖信息。当然也有坑点，可自行搜索。

drf

Docs：https://www.django-rest-framework.org/

基于 Django 的 REST Framework，快速实现 REST API。

watchdog

GitHub：https://github.com/gorakhargosh/watchdog

方便监视文件系统改动。

glob

Docs：https://docs.python.org/3/library/glob.html

对文件的操作非常方便。

2to3

Docs：https://docs.python.org/2/library/2to3.html

把 Python2 代码转成 Python3 代码。

glom

GitHub：https://github.com/mahmoud/glom

对 JSON 嵌套的处理非常方便。

pathlib

Docs：https://docs.python.org/3/library/pathlib.html

更为方便的 Python 路径操作库。

environs

GitHub：https://github.com/sloria/environs

对于环境变量的获取非常方便，支持多种类型，如 int、bool 等。

pysnooper

GitHub：https://github.com/cool-RR/PySnooper

非常方便简单的 Python 调试器，可以追踪到代码每一处细节的执行状态。

tqdm

GitHub：https://github.com/tqdm/tqdm

进度条控制显示非常方便。

sh

GitHub：https://github.com/amoffat/sh

对 Linux 一些命令的封装，简单好用又高效。

faker

GitHub：https://github.com/joke2k/faker

模拟数据的生成。

个人写的简介：https://mp.weixin.qq.com/s/iLjr95uqgTclxYfWWNxrAA

arrow、dateutil、dateparser、pendulum

GitHub：https://github.com/crsmithdev/arrow、https://github.com/dateutil/dateutil、https://github.com/scrapinghub/dateparser、https://github.com/sdispater/pendulum

时间解析和处理库，非常方便。arrow 目前 Star 最多，好评最多。

yagmail

GitHub：https://github.com/kootenpv/yagmail

方便的发邮件库，替代自带的 smtplib。

chardet

GitHub：https://github.com/chardet/chardet

字符串类型编码检测。

pypinyin

GitHub：https://github.com/mozillazg/python-pinyin

汉字转拼音，在一些中文转化处理上很有用。

个人写的简介：https://mp.weixin.qq.com/s/NvA3j8Ns1-6CFgWpUcWwQw

sphinx

Docs：https://www.sphinx-doc.org/en/master/

编写文档使用，大多数 Python 库文档都是这个写的，如 Scrapy、requests。

个人 sphinx + markdown 的样例：https://github.com/Gerapy/Docs

jinja2

GitHub：https://github.com/pallets/jinja

一个方便的模板引擎，呈现页面时很方便。

click

GitHub：https://github.com/pallets/click

更方便灵活地实现命令行传递参数。

ray

GitHub：https://github.com/ray-project/ray

分布式多进程管理。

supervisor

GitHub：https://github.com/Supervisor/supervisor

进程管理工具，如实现多任务后台运行，Docker 打包时会经常用到。

apscheduler

GitHub：https://github.com/agronholm/apscheduler

Python 定时任务，不过 K8S 也可以实现，个人目前可能更倾向于 K8S。

intelpython

Home：https://software.intel.com/en-us/distribution-for-python

这不是 Python 库，是一个 Intel 开发的基于 Intel 处理器优化的 Python 解释器，对于大规模运算提升很大。

完毕。

好啦，先推荐这么多了，后面还会慢慢积累，大家可以了解下，个人感觉有不少库还是能极大提高生产力的。