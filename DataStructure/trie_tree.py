#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
    python 实现字典树

Trie树，又称单词查找树、字典树，是一种树形结构，是一种哈希树的变种，是一种用于快速检索的多叉树结构。
典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。
     Trie的核心思想是空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
Trie树也有它的缺点,Trie树的内存消耗非常大.当然,或许用左儿子右兄弟的方法建树的话,可能会好点.
"""
class TrieNode(object):
    def __init__(self):
        # 是否构成一个完成的单词
        self.is_word = False
        self.children = [None] * 26
 
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, s):
        """Add a string to this trie."""
        p = self.root
        n = len(s)
        for i in range(n):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TrieNode()
                if i == n - 1: 
                    new_node.is_word = True
                p.children[ord(s[i]) - ord('a')] = new_node
                p = new_node
            else:
                p = p.children[ord(s[i]) - ord('a')]
                if i == n - 1:
                    p.is_word = True
                    return
    
    def search(self, s):
        """
            判断字符串s 是否在 字典树 trie中.
        """
        p = self.root
        for c in s:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False   
    
if __name__ == '__main__':
    trie = Trie()
    trie.add('str')
    trie.add('acb')
    trie.add('acblde')
    print trie.search('acb')
    print trie.search('ac')
    trie.add('ac')
    print trie.search('ac')
