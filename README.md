# [使用]()
### 1、测试数据
* 将待测男女声分别放入以下两个文件夹/testdata/male /testdata/female
* 测试文件文件名过长调用接口易出现链接拒绝问题，可以使用renamefiles脚本进行重命名

### 2、安装requests
* sudo pip install requests

### 3、测试策略
* 根据接口返回结果统计正确率
* 可以自定义测试数据比例
