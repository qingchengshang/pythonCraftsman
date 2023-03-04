class AppConfig:
    """程序配置类，使用单例模式"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            inst = super().__new__(cls)
            # 已省略：从外部配置文件读取配置
            ...
            cls._instance = inst
        return cls._instance

    def get_database(self):
        """读取数据库配置"""
        ...

    def reload(self):
        """重新读取配置文件，刷新配置"""
        ...


"""
# 预绑定方法模式 (prebound method pattern) 是一种将对象方法绑定为函数的模式。要实现该模式，只需要一个单例对象----模块(module)
# 当你在 python 中执行 import 语句导入模块时，无论 import 执行了多少次，每个被导入的模块在内存中只会存在一份(保存在sys.modules中)。
# 因此要实现单例模式，只需在模块里创建一个全局对象即可：
"""
class AppConfig:
    """程序配置类，使用单例模式"""

    def __init__(self):
        # 已省略：从外部配置文件读取配置
        ...

    def get_database(self):
        """读取数据库配置"""
        ...

    def reload(self):
        """重新读取配置文件，刷新配置"""
        ...


# 下一步，为了给其它模块提供好用的API，我们需要将单例对象_config的公有方法绑定到config模块上：
# file: project/config.py
_config = AppConfig()
get_database_conf = _config.get_database
reload_config = _config.reload

"""
# 之后，其它模块就可以像调用普通函数一样操作应用配置对象了：
from project.config import get_database_conf, reload_config 
db_conf = get_database_conf()
reload_config()
"""