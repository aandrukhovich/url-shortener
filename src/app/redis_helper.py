import redis


# https://stackoverflow.com/a/49398879
class Singleton(type):
    """
    An metaclass for singleton purpose. Every singleton class should inherit from this class by 'metaclass=Singleton'.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RedisClient(metaclass=Singleton):
    """Singleton class for sharing redis connection pool puproses

    Usage:
    ```from redis_helper import RedisClient
    ...
    redis_connection = RedisClient().conn
    redis_connection.get(...)
    # or
    RedisClient().conn.get(...)

    Call redis_helper.startup() to initialize this instance before using
    """

    def __init__(self):
        self.pool = redis.ConnectionPool()

    @property
    def conn(self):
        if not hasattr(self, "_conn"):
            self.getConnection()
        return self._conn

    def getConnection(self):
        self._conn = redis.Redis(connection_pool=self.pool, decode_responses=True, charset="utf-8")

    @property
    def startup(self):
        """Initialize connection pool and self._conn"""


def startup():
    RedisClient()
