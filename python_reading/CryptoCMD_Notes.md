
### CryptoCMD代码阅读笔记
#### 各文档的功能

1. .Github <br/>
    ***
   - CONTRIBUTING.md <br/>
    说明性文档：如果有程序员发现CryptoCMD的代码有bug并且想要改进需要怎么做 <br/>
    ***
   - ISSUE_TEMPLATE.md <br/>
    文件模板：程序员完成修改后提交时需要填写的文档，说明所作修改的类别(新功能、现有功能的改进、错误的修正等)以及修改的详情 <br/>
    ***
   - PULL_REQUEST_TEMPLATE.md<br/>
    文件模板：程序员pull request的时候需要对自己做出的更改作出详细说明<br/>
    ***
2. cryptocmd<br/>
    ***
   - \_\_init \_\_.py <br/>
   将文件夹变成一个Python模块，批量导入模块<br/>
   此处为导入core代码以及\_\_version\_\_版本记录代码<br/>
   这两个代码文件在同一目录下<br/>
   ***
   - \_\_version\_\_.py <br/>
   记录代码版本<br/>
   ***
   - core.py & utils.py <br/>
   核心代码，实现从<https://coinmarketcap.com>抓取货币历史数据<br/>
   这部分的笔记会在代码注释中写出<br/>
   ***
3. examples<br/>
   ***
   - get\_csv.py <br/>
   一个例子，代码运行后会从网页抓取比特币的所有历史数据，并生成一个csv文档<br/>
   ***
4. .gitignore <br/>
   ***
   说明性文档：调用了的资源；<br/>
   ***
5. .travis.yml<br/>
   ***
   说明性文档：说明所使用的语言、适用的语言版本、安装方法、示例；<br/>
   ***
6. LICENSE <br/>
   ***
   说明性文档：许可与权限<br/>
   ***
7. MANIFEST.IN<br/>
   ***
   用于包含其他文件（READNE,LICENSE,requirements）；<br/>
   ***
8. Pipfile & Pipfile.lock <br/>
   ***
   这两个都是pipnev包的配置文件，用以代替requirements.txt;<br/>
   Pipfile.lock通过hash算法将包的名称和版本及依赖关系生成哈希值，可以保证包的完整性；<br/>
   Pipnev：有效管理Python的多个环境和各种包；<br/>
   ***
9. README.rst<br/>
   ***
   说明性文档,包含：<br/>
   - 安装方法
   - 使用方法
      - 抓取全部历史数据
      - 抓取指定时间段内的历史数据
   - 数据存储的域（Date,Open,High,Low,Close,Volume,Market Cap）
   - 数据来源说明
   - 其他程序员对此代码拥有的权限
   - 许可
   ***
10. setup.cfg<br/>
   ***
   提供一种方式，让包的开发者提供命令的默认选项，同时为用户提供修改机会；<br/>
   此处作用为：构建[bdist_wheel]的时候设定universal默认参数为1；<br/>
   在setup.py后、命令行开始执行前解析；<br/>
   ***
11. setup.py<br/>
   ***
   java和python都有类似classpath（pythonpath）的一个概念，即程序查找路径。java虚拟机或者python编译器，会从这些路径中查找你程序中所使用的包/模块。
   java的classpath有一个非常适合项目开发的特性，就是它的classpath包括了项目根目录下的文件和jar包，这样一个项目中使用其它依赖项，只要把这些jar文件放在程序根目录下就可以了。另一方面自己项目中的代码可以无障碍的互相引用。classpath还包含jre相关的一组路径。<br/>
   
  而python的pythonpath概念和java相似，它包含python安装目录相关的一组路径（内置模块和标准库，以及其它第三方模块的共享路径），但是它不支持项目所在根目录这种形式，而是只支持文件所在目录的相对路径。<br/>
  
  setup.py中所记录的就是项目模块添加到pythonpath的规则。
  setup.py中会定义此项目中有哪些模块需要被加入到pythonpath，在这个过程中可以把测试项目过滤掉；setup.py中会定义需要的第三方依赖，使用安装命令可以同时安装这些第三方依赖，等等。这样安装完成之后，本机的其它python项目，也能用到此项目的模块。<br>
  总的来说，可看作是整个程序的基本配置；<br/>
  参考链接：<https://zhidao.baidu.com/question/744963162784611972.html>
   <br/>
   ***
