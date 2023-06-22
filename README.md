# back-end



### 开发环境配置方法

最开始，要创建一个conda环境，之后的开发都在这个虚拟环境中进行：

`conda create -n django python==3.7.*`

安装好conda环境后，每次使用要预先激活：

`conda activate django`

安装好虚拟环境后，要安装依赖包：

`pip install -r requirements.txt`

之后就可以正常开发了

### 项目结构说明

`./testapp/`是练手用的测试模块，已废弃


`./mysite/templates/`下面的模板未前后端分离，已废弃






#### Finished:

user_auth：用户注册、登陆、登出模块
questions：创建问题、查看问题模块
answers：创建回答、查看回答模块

#### Todo:
大模型解答模块
首页模块
个人主页模块
标签分类模块

