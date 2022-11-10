- ### git status 不显示中文显示八进制数字

  ![3f6f41a20f3da19933ec07a71951c12f](https://raw.githubusercontent.com/PandPirate/TyporaImages/main/typora/202210312255916.png)

**解决办法** 

将git 配置文件 `core.quotepath`项设置为false。
quotepath表示引用路径
加上`--global`表示全局配置

``` git
git config --global core.quotepath false
```

引用 https://blog.csdn.net/u012145252/article/details/81775362



- 配置.gitignore忽略文件

​	git设置忽略文件和目录有两种方式，一种是项目所有人员共用的的，一种是开发自己使用的

第一种，所有开发者共用的需要把设置设定在**.gitignore**该文件中

第二种，开发者个人使用的忽略配置，许雅设定在**.git/info/exclude** 该文件中

例子:

```git
# 忽略*.o和*.a文件,不忽略my.o文件
*.[oa]
!my.o

# 忽略*.b和*.B文件，不忽略my.b文件
*.[bB]
!my.b

# 忽略dbg文件和dbg目录
dbg

# 只忽略dbg目录，不忽略dbg文件
dbg/

# 只忽略dbg文件，不忽略dbg目录
dbg
!dbg/

# 只忽略当前目录下的dbg文件和目录，子目录的dbg不在忽略范围内
/dbg

#忽略所有.svn目录
.svn/
#忽略所有target目录
target/
#忽略所有.idea目录
.idea/
#忽略所有.iml文件
*.iml

# 以'#'开始的行，被视为注释.

 * ？：代表任意的一个字符
    * ＊：代表任意数目的字符
    * {!ab}：必须不是此类型
    * {ab,bb,cx}：代表ab,bb,cx中任一类型即可
    * [abc]：代表a,b,c中任一字符即可
    * [ ^abc]：代表必须不是a,b,c中任一字符

```

引用 https://blog.csdn.net/zxlyx/article/details/124237977