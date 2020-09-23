class Solution:
    # QUESTION: https://leetcode.com/problems/defanging-an-ip-address
    # APPROACH: trivial, use python replace method...O(N) runtime, constant space
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')