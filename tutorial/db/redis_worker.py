import redis
import dill
import time
import random

"""工作者进程
工作者进程实际地完成任务。它们就是盯着消息队列，队列中有任务了就抓取下来，把任务完成，然后告诉队列我完成了，删除这个任务
"""

# configure our redis client
r = redis.Redis(
	host='localhost',
	port=6379
)

while True:
	# wait until there is an element in the 'tasks' queue
	key, data = r.brpop('tasks')

	# deserialize the task
	deserialize_fun, deserialize_args = dill.loads(data)

	# run the task
	deserialize_fun(*deserialize_args)
