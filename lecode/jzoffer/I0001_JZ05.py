"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。



示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."


限制：

0 <= s 的长度 <= 10000

通过次数125,549提交次数165,000


class Solution:
    def replaceSpace(self, s: str) -> str:

"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")

    @staticmethod
    def check_class(solution=None):
        solution = Solution if solution is None else solution
        assert solution().replaceSpace(s="We are happy.") == "We%20are%20happy."
