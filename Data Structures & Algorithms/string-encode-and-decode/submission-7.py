class Solution:

    '''
    ["Hello", "World:Hi"]
    '5:Hello8:World:Hi' -> 구분자 앞에 숫자 추가 
    '''
    def encode(self, strs: List[str]) -> str:
        text = ''
        for word in strs: 
            text += f'{len(word)}:{word}'
        return text

    def decode(self, s: str) -> List[str]:
        # length에 대한 idx 설정
        l, start = [], 0

        while start < len(s):
            # 구분자 찾기 
            mid = s.find(':', start)
            length = int(s[start:mid])
            l.append(s[mid+1:mid+length+1])
            start = mid+length+1

        return l
