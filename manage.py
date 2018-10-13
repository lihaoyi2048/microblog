from flask_migrate import Migrate, MigrateCommand
from exts import db
from flask_script import Manager
from flask import Flask
from config import Config
import app_name.models


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


# 初始化数据库：python manage.py db init
# 把当前的模型添加到迁移文件中：python manage.py db migrate
# 将映射文件真正的映射到数据库中：python manage.py db upgrade
