class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '}':'{',']':'[',')':'('
        }

        for char in s:
            # 여는 괄호인 경우 추가
            if char in table.values():
                stack.append(char)
            # stack이 비어있지 않고 닫는 괄호 왼쪽에 여는 괄호가 있는 경우
            elif stack and table[char] == stack[-1]:
                stack.pop()
            # 닫는 괄호 옆에 여는 괄호가 없다면 Flase
            else:
                return False
        
        # stack에 여는 괄호가 남아있다면 
        if stack:
            return False
        return True