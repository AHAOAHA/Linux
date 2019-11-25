# GitSubModule

该仓库作为主仓库，添加子仓库，并制定依赖特定版本。

主仓库中使用对应`commit id`作为子仓库，`git clone`主仓库不会自动`clone`子仓库，需要手动通过`git submodule update --init --recursive`迁出子仓库，此时子仓库位于未命名分支。