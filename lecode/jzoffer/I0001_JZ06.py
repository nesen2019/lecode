"""
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]


限制：

0 <= 链表长度 <= 10000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

"""

from typing import List
from lecode.struc import ListNode, HandleLink


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

    @staticmethod
    def check_class(solution=None):
        solution = Solution if solution is None else solution

        h = HandleLink([1, 3, 2])
        assert solution().reversePrint(head=h.data_root) == [2, 3, 1]

# 作者：Krahets
# 链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5d8831/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    Solution.check_class()
