import json, unittest

class PythonJson(unittest.TestCase):

	def test_dict_to_json(self):
		print('module jsons: ')
		print(dir(json))
		data = {
			'no': 1,
			'name': 'Runoob',
			'url': 'http://www.runoob.com'
		}
		# Python字典类型转换为 JSON 对象
		json_obj = json.dumps(data)

		print('Python Dict: ' + repr(data))
		print('Json Object: ' + json_obj)

	def test_json_to_dict(self):
		data = {
			'no': 2,
			'name': 'Google',
			'url': 'http://www.google.com'
		}
		# Python 字典类型转换为 JSON 对象
		json_str = json.dumps(data)
		print('Json Object: ' + json_str)

		# 将 JSON 对象转换为 Python 字典
		dict_str = json.loads(json_str)
		print('Dict name: ' + repr(dict_str['name']))
		print('Dict url: ' + repr(dict_str['url']))

	''' 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据 '''
	def test_load_json_file(self):
		with open('example_for_load.json', 'r') as f:
			dict_str = json.load(f)
		print('Load JSON file: ' + repr(dict_str))

	def test_dump_json_file(self):
		data = {
			'no': 3,
			'name': 'Baidu',
			'url': 'http://www.baidu.com'
		}
		with open('example_for_dump.json', 'w') as f:
			json.dump(data, f)
		print('Dump JSON file: ' + repr(data))

if __name__ == '__main__':
	unittest.main()