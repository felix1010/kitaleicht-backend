虚拟环境
安装
pip install virtualenv

创建
virtualenv venv

启动
venv\Scripts\activate

依赖
安装 flask
pip install flask

安装 flask-cors
pip install flask-cors

安装 psycopg2 (连接 postgre)
pip install psycopg2-binary

安装 pip install mysql-connector-python （连接 mysql）
pip install mysql-connector-python

Port: 5000

数据库初始化工具
Flask-Migrate

构建
如果发现了已经有的服务镜像已经过期或者需要更新，它会自动按照你的 Dockerfile 来重新构建这些镜像，确保它们是最新的
docker-compose up --build
