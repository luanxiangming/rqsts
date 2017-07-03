import zlib


def try_zlib():
    """
    在Python中可以压缩长字符，不涉及任何档案文件
    """
    print('*****module zlib*****')
    print(dir(zlib))

    long_string = """Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Nunc ut elit id mi ultricies
        adipiscing. Nulla facilisi. Praesent pulvinar,
        sapien vel feugiat vestibulum, nulla dui pretium orci,
        non ultricies elit lacus quis ante. Lorem ipsum dolor
        sit amet, consectetur adipiscing elit. Aliquam
        pretium ullamcorper urna quis iaculis. Etiam ac massa
        sed turpis tempor luctus. Curabitur sed nibh eu elit
        mollis congue. Praesent ipsum diam, consectetur vitae
        ornare a, aliquam a nunc. In id magna pellentesque
        tellus posuere adipiscing. Sed non mi metus, at lacinia
        augue. Sed magna nisi, ornare in mollis in, mollis
        sed nunc. Etiam at justo in leo congue mollis.
        Nullam in neque eget metus hendrerit scelerisque
        eu non enim. Ut malesuada lacus eu nulla bibendum
        id euismod urna sodales. 
        """

    print("long_string length: {}".format(len(long_string)))

    compressed_string = zlib.compress(bytes(long_string, 'UTF-8'))
    print("compressed_string size: {}".format(len(compressed_string)))

    decompressed_string = zlib.decompress(compressed_string)
    print('decompressed_string size: {}'.format(len(decompressed_string)))


if __name__ == '__main__':
    try_zlib()
