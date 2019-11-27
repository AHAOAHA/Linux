# GitSubModule

该仓库作为主仓库，添加子仓库，并制定依赖特定版本。

主仓库中使用对应`commit id`作为子仓库，`git clone`主仓库不会自动`clone`子仓库，需要手动通过`git submodule update --init --recursive`迁出子仓库，此时子仓库位于未命名分支。

依赖仓库版本发生变化时，使用`git submodule update --init --recursive`迁出的仍然是旧版本的仓库，如果想更新依赖的仓库，需要进入依赖仓库，`git checkout`到对应分支，进入主仓库新建一个commit。

未commit修改，通过`git checkout -f`强制切换分支。

添加tag之后，master分支持续开发。
