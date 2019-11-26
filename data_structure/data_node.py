#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File   : data_node.py
@Author : nlpqs-George
@Time   : 2019/11/26 22:17
@Todo   : 数据节点
"""

__all__ = ["DataNode"]


class DataNode(object):
    """
    数据节点
    """

    # 节点名称
    __name = None
    # 节点数据
    __data = None
    # 前驱节点
    __previous_node = None
    # 后续节点
    __next_node = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=None):
        self.__name = name
        pass

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data=None):
        self.__data = data
        pass

    @property
    def previous_node(self):
        return self.__previous_node

    @previous_node.setter
    def previous_node(self, previous_node=None):
        self.__previous_node = previous_node
        pass

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node=None):
        self.__next_node = next_node
        pass

    def __init__(self, name=None, data=None, previous_node=None, next_node=None):
        self.__name = name
        self.__data = data
        self.__previous_node = previous_node
        self.__next_node = next_node
        pass

    def has_previous(self):
        return True if self.previous_node is not None else False

    def has_next(self):
        return True if self.next_node is not None else False

    def is_empty(self):
        return True if self.data is None else False

    pass


def app():
    pass


if __name__ == '__main__':
    app()
