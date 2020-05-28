import logging.config

# load my module
import foo

# load the logging configuration
logging.config.dictConfig({
    'version': 1,
    # 是否禁用之前logging配置之前，已经存在的logger，默认为True
    # 并刷新为变更为当前
    'disable_existing_loggers': False,  # this fixes the problem
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'foo': {
            'format': 'foo format: %(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            "formatter": "standard",
            'class':'logging.StreamHandler',
        },
        'foo': {
            'level':'INFO',
            "formatter": "foo",
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        # 可以刷新foo的logger的配置
        'foo': {
            'handlers': ['foo'],
            'level': 'INFO',
            # 是否往父级传
            'propagate': True
        }
    }
})

# 会经过foo和root，两个层级，一次的打日志所以输出两次
foo.foo()
bar = foo.Bar()
bar.bar()

logger = logging.getLogger(__name__)
logger.info('-----')
