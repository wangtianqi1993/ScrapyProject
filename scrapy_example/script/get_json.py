# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

import json
import os

def get_json(in_path, out_path):
    """

    :param path:
    :return:
    """
    with open(in_path, 'r') as file1:
        result = file1.read()
        content = json.loads(result)
        # content_decode = content.decode('utf-8')
        # with open(out_path, 'w') as file2:
        for item in content:
            print 'usrname', item['username']
            print 'text', item['text'].encode('utf-8')
            # file2.write(item['username'])
            # file2.write(item['text'].decode('utf-8'))


if __name__ == "__main__":
    get_json("/home/wtq/develop/workspace/github/ScrapyProject/scrapy_example/xiaobaihe/result.json", '/home/wtq/zhihu.txt')
    print os.getcwd()
