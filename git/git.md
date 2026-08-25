# GIT


### git与svn区别
Git 不仅仅是个版本控制系统，它也是个内容管理系统(CMS)，工作管理系统等。

如果你是一个具有使用 SVN 背景的人，你需要做一定的思想转换，来适应 Git 提供的一些概念和特征。

Git 与 SVN 区别点：

1、Git 是分布式的，SVN 不是：这是 Git 和其它非分布式的版本控制系统，例如 SVN，CVS 等，最核心的区别。

2、Git 把内容按元数据方式存储，而 SVN 是按文件：所有的资源控制系统都是把文件的元信息隐藏在一个类似 .svn、.cvs 等的文件夹里。

3、Git 分支和 SVN 的分支不同：分支在 SVN 中一点都不特别，其实它就是版本库中的另外一个目录。

4、Git 没有一个全局的版本号，而 SVN 有：目前为止这是跟 SVN 相比 Git 缺少的最大的一个特征。

5、Git 的内容完整性要优于 SVN：Git 的内容存储使用的是 SHA-1 哈希算法。这能确保代码内容的完整性，确保在遇到磁盘故障和网络问题时降低对版本库的破坏。

### git 命令
1. git init
2. git clone <url>
3. git add <filename>
4. git comit -m "代码提交信息"
5. git push origin master
6. git show     查看最近修改

### git 基本配置
```bash
1. 设置用户的名字和email
$ git config --global user.name "xx"`
$ git config --global user.email "xx@xx.com"

2. 编辑commit message时,需要一个文本编辑器,具体可以由用户指定
$ git config --global core.editor vi

3. 如果工作区有一些文件或目录不希望被git管理,可以在工作区的根目录创建文件.gitignore 并写上它们的路径

--global  表示全局配置,没有这个参数就只是对当前仓库生效.

查看配置信息
$ git config --list
$ git config --global --list
```
### git 目录结构
- Working Directory: 工作区
- Staging Area     : 暂存区,又称index, cache
- Local Repository : 仓库区,或本地repo

### git  重置版本
``` bash
- reset
$ git reset HEAD~n              撤销n个版本.重置后,被撤销的版本会从暂存区回滚到工作区
$ git reset --hard HEAD~n       硬重置,撤销n个版本.重置后,被撤销的版本*不会*从暂存区回滚到工作区
$ git reflog                    历史记录, 可以找到软重置或硬重置的历史记录
```
### git 分支
```bash
- 查看当前分支列表,其中带*的表示当前所在分支
$ git branch
- 创建分支并切换到新分支
$ git checkout -b <new branch>
- 切换分支
$ git checkout <branch name>
- 重命名分支
$ git branch --move <new branch name>
- 删除分支
$ git branch -d <branch name>
- 同步
$ git merge
HEAD 指向目标分支,即要合并别的分支的分支.如果合并失败,出现冲突(Resolve Conflicts),可以在master上手动修改文件,再在master上提交
或加入暂存区执行git merge --continue.
如果需要中止操作,执行 git merge --abort.

- 变基(rebase)
本来是这样:
   v1---v2---v3---v4---v5         master
  root        \
               v6---v7            feature

想改成这样:
   v1---v2---v3---v4---v5           master
  root                  \
                         v6---v7    feature
我们从V3开始,创建了新的分支feature,这个feature就是以V3为基(base)的.
我们新增两个commit之后, 想把feature分支改成(re)以V5为基(base),这就是变基.

$ git checkout feature
$ git rebase master

- cherry-pick
合并(merge)会把一个分支的全部改动引入当前分支,但有时我们只需要某个分支的几个commit,此时我们需要这样的操作:将对方commit抓过来,并接在当前分支上.这种从其他分支挑选commit,抓取并接入当前分支的操作,就叫做cherry-pick.

$ git checkout master
$ git cherry-pick commit id<>
```
### 远程交互
```bash
- 查看分支
$ git remote -v

先创建本地分支,再创建远程分支.关联本地和远程分支.
$ git push --set-upstream origin main
```

### HTTPS 下 git pull 的方法步骤（需要用户名/密码）

当 `git remote -v` 显示 `https://github.com/username/repo.git` 时，执行 `git pull` 会要求输入用户名和密码。

1. 确认远程地址是 HTTPS 格式

```bash
$ git remote -v
# 显示：https://github.com/username/repo.git
```

2. 生成 Personal Access Token（个人访问令牌）

GitHub 自 2021 年 8 月 13 日起停用了 HTTPS 的账号密码认证，所以"密码"栏不能填登录密码，必须填 Token。

生成步骤：
1. GitHub → 右上角头像 → Settings
2. 左侧最底部 → Developer settings
3. → Personal access tokens → Tokens (classic) 或 Fine-grained tokens
4. → Generate new token
5. 勾选 repo 权限（拉取私有仓库需要）
6. 生成后复制保存（页面只显示这一次）

3. 执行 git pull 并输入凭据

```bash
$ git pull
Username for 'https://github.com': 你的GitHub用户名
Password for 'https://你的用户名@github.com': 粘贴 Token（屏幕不显示，直接回车）
```

4. （可选）把 Token 存进远程地址，避免每次输入

```bash
$ git remote set-url origin https://<用户名>:<Token>@github.com/username/repo.git
```

5. （可选）改用 SSH，彻底免密码

```bash
$ git remote set-url origin git@github.com:username/repo.git
```

注意：
- Token 权限 = 账号本身的权限，不扩大也不缩小
- 拉取公开仓库不需要 Token，任何人都能 pull
- 拉取别人的私有仓库，需要对方把你加成 Collaborator（协作者）

## 问题
- push时需要输入用户名密码
   1. 检查远程仓库地址是不是 SSH 格式
   ```bash
    git remote -v
    应该看到类似：git@github.com:username/repo.git
    如果是https://github.com/username/repo.git
    如果是 HTTPS，Git 会要求用户名和密码。
    如果是 HTTPS，可以用下面命令切换到 SSH：
    git remote set-url origin git@github.com:username/repo.git
   ```
   2. SSH key 是否正确配置和加载
```bash
	确认你生成了 SSH key（通常是 ~/.ssh/id_rsa 和 ~/.ssh/id_rsa.pub）
	钥已添加到对应 Git 服务器（GitHub、GitLab 等）账户中
	SSH agent 已加载私钥：

	ssh-add -l
	如果没看到你的 key，执行：

	ssh-add ~/.ssh/id_rsa
```
   3. 确认 Git 使用的是 SSH 而非 HTTPS 代理
```
	用下面命令测试 SSH 连接
	正常情况下，会显示欢迎信息，不会要密码
	ssh -T git@github.com
```
   4. 缓存凭据
```
	如果你之前用 HTTPS 访问过仓库，Git 可能缓存了旧凭据，建议清理凭据缓存。

	Windows Credential Manager 中清理对应条目

	Linux/macOS 可尝试清理 .git-credential 缓存
```

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

- git diff

    ```git
    git diff # 用来查看工作区文件和暂存区文件的区别
    git diff HEAD 用来查看工作区和仓库区文件的区别
    git diff --cached或者git diff --staged用来查看暂存区和仓库区文件的区别
    git diff commit-id-old commit-id-new
    git diff file_name 获取指定文件的修改
    --stat 统计哪些文件被改动,有多少行被改动
    ```

     ![img](https://raw.githubusercontent.com/PandPirate/TyporaImages/main/typora/202212182047076.png)

![image-20221218204750423](https://raw.githubusercontent.com/PandPirate/TyporaImages/main/typora/202212182047178.png)

- git stash

    在本地代码有修改情况下,不能进行git pull操作.需要把修改放到栈里 git stash.代码更新后在git stash pop 把放到栈里的修改拿出来

- ### git常用命令以及如何与fork别人的仓库保持同步

    ![image-20230107171739584](https://raw.githubusercontent.com/PandPirate/TyporaImages/main/typora/202301071718237.png)
