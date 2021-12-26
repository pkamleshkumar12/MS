import logging
import logging.config

logging.config.fileConfig('logging.conf')
# like fileConfig there is dictConfig

logger = logging.getLogger('simpleExample')

logger.debug('this is a debug message')