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