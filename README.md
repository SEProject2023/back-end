# back-end


### 开发环境配置方法

首先，要创建一个conda环境，之后的开发都在这个虚拟环境中进行：

`conda create -n django python==3.7.*`

安装好conda环境后，**每次**使用这份代码都要预先激活虚拟环境：

`conda activate django`

首次安装好虚拟环境时，要安装依赖包：

`pip install -r requirements.txt`

之后就可以正常开发了。

### 项目结构说明及开发进度
#### Abandoned:

`./mysite/testapp/`是练手用的测试模块，已废弃


`./mysite/templates/`下面的模板未前后端分离，已废弃



#### Finished:

user_auth：用户注册、登陆、登出模块

questions：创建问题、查看问题模块

answers：创建回答、查看回答模块、大模型解答模块

homepage：首页模块（获取最新的10个问题、最新的10个用户答案、最新的10个大模型答案）

user_details：简单的个人主页模块（获取用户的基本信息、用户的所有问题、回答）

search：搜索模块（从问题、回答、用户名等多个位置进行搜索）
#### Todo:


用户信息管理模块

标签分类模块
