import logging
import random
import time
import redis
import dill

"""
客户端部分: 客户端把消息发送到任务队列中, 定义要发送给worker（工作者进程）的任务
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wait_random_amount_time(arg1, arg2):
	logger.info("Do something random using %s and %s" % (arg1, arg2))
	time.sleep(random.uniform(1, 3))


r = redis.Redis(
	host='localhost',
	port=6379
)

""" 开始生产一些任务，并且把它推送到任务队列中 """
NUM_TASKS = 20
logger.info("Generating %s tasks", NUM_TASKS)

for i in range(NUM_TASKS):
	"""About Dill
	dill extends python’s pickle module for serializing 
	and de-serializing python objects to the majority of the built-in python types
	"""
	r1 = random.randrange(10)
	r2 = random.randrange(10)

	# Serialize the task and its arguments
	data = dill.dumps((wait_random_amount_time, [r1, r2]))
	r.lpush('tasks', data)
