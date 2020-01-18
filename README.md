# GitSubModule

该仓库作为主仓库，添加子仓库，并制定依赖特定版本。

主仓库中使用对应`commit id`作为子仓库，`git clone`主仓库不会自动`clone`子仓库，需要手动通过`git submodule update --init --recursive`迁出子仓库，此时子仓库位于未命名分支。

依赖仓库版本发生变化时，使用`git submodule update --init --recursive`迁出的仍然是旧版本的仓库，如果想更新依赖的仓库，需要进入依赖仓库，`git checkout`到对应分支，进入主仓库新建一个commit。

未commit修改，通过`git checkout -f`强制切换分支。

添加`tag`之后，`master`持续提交，当需要`checkout`回到某`tag`处时，若此时分支下文件内容发送改变但未`commit`，会产生错误，`checkout`失败，使用`checkout -f`选项强制切换会丢失变更。

# Git LFS

Git LFS用来管理项目中的大文件
`git lfs install`打开项目LFS功能, 主要通过.gitattributes文件记录信息
`git lfs track *.png`表示当前仓库通过LFS track所有.png文件的更改, 即使文件大小超过100M

# third_party

一些经过编译的第三方库
