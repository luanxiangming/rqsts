import unittest

class PythonOperations(unittest.TestCase):
	 # 数值运算
    def test_number_operations(self):
        self.assertEqual(2 / 4, 0.5)  # 除法(总是返回一个浮点数)，得到一个浮点数0.5
        self.assertEqual(2 // 4, 0) # 除法(总是返回一个整数)，得到一个整数0
        self.assertEqual(17 % 3, 2) # 取余 , 得到2
        self.assertEqual(2 ** 5, 32) # 乘方, 得到32

    # String（字符串）
    def test_string_operations(self):
        str = 'Runoob'
        self.assertEqual(str, 'Runoob')
        self.assertEqual(str[0:-1], 'Runoo')
        self.assertEqual(str[0], 'R')
        self.assertEqual(str[2:5], 'noo')
        self.assertEqual(str[2:], 'noob')
        self.assertEqual(str * 2, 'RunoobRunoob')
        self.assertEqual(str + "TEST", 'RunoobTEST')

    # List（列表）
    def test_list_operations(self):
        list = ['abcd', 786, 2.23, 'runoob', 70.2]
        tinylist = [123, 'runoob']
        self.assertEqual(list, ['abcd', 786 , 2.23, 'runoob', 70.2])
        self.assertEqual(list[0], 'abcd')
        self.assertEqual(list[1:3], [786 , 2.23])
        self.assertEqual(list[2:], [2.23, 'runoob', 70.2])
        self.assertEqual(tinylist * 2, [123, 'runoob',123, 'runoob'])
        self.assertEqual(list + tinylist, ['abcd', 786 , 2.23, 'runoob', 70.2, 123, 'runoob'])

    # Tuple（元组）
    def test_tupel_operations(self):
        tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
        tinytuple = (123, 'runoob')
        self.assertEqual(tuple, ('abcd', 786 , 2.23, 'runoob', 70.2))
        self.assertEqual(tuple[0], 'abcd')
        self.assertEqual(tuple[1:3], (786, 2.23))
        self.assertEqual(tuple[2:], (2.23, 'runoob', 70.2))
        self.assertEqual(tinytuple * 2, (123, 'runoob', 123, 'runoob'))
        self.assertEqual(tuple + tinytuple, ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob'))

    # Set（集合）
    def test_set_operations(self):
        student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
        print(student) # 输出集合，重复的元素被自动去掉
        # set可以进行集合运算
        a = set('abcdcd')
        b = set('cdefef')
        self.assertEqual(a, {'a', 'b', 'c', 'd'}) 
        self.assertEqual(b, {'c', 'd', 'e', 'f'})
        self.assertEqual(a - b, {'a', 'b'}) # a和b的差集
        self.assertEqual(a | b, {'a', 'b', 'c', 'd', 'e', 'f'}) # a和b的并集
        self.assertEqual(a & b, {'c', 'd'}) # a和b的交集
        self.assertEqual(a ^ b, {'a', 'b', 'e', 'f'}) # a和b中不同时存在的元素

    # Dictionary（字典）
    def test_dict_operations(self):
        new_dict = {}
        new_dict['one'] = "1 - 菜鸟教程"
        new_dict[2] = "2 - 菜鸟工具"
        tiny_dict = {'name': 'runoob', 'code': '1', 'site': 'www.runoob.com'}
        self.assertEqual(new_dict['one'], '1 - 菜鸟教程')
        self.assertEqual(new_dict[2], '2 - 菜鸟工具')
        self.assertEqual(sorted(tiny_dict.keys()), ['code', 'name', 'site'])
        self.assertEqual(sorted(tiny_dict.values()), ['1', 'runoob', 'www.runoob.com'])
        # 构造函数 dict() 可以直接从键值对序列中构建字典如下：
        new_dict2 = dict([('google', '1'), ('baidu', '2'), ('bing', '3')])
        self.assertEqual(new_dict2, {'baidu': '2', 'bing': '3', 'google': '1'})
        new_dict3 = {x: x**2 for x in range(1,5)}
        self.assertEqual(new_dict3, {1:1, 2:4, 3:9, 4:16})
        new_dict4 = dict(google=1, baidu=2, bing=3)
        self.assertEqual(new_dict4, {'baidu': 2, 'bing': 3, 'google': 1})

if __name__ == '__main__':
	unittest.main()