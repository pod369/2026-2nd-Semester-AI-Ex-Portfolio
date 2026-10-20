
print(type(1))                     # <class 'int'>
print(type("1"))                   # <class 'str'>
print(type("하나 One"))            # <class 'str'>
print(type(["파이썬", "Python"]))  # <class 'list'>



print("문자열은 큰따옴표나 작은따옴표로 표현할 수 있다.")
print('문자열은 큰따옴표나 작은따옴표로 표현할 수 있다.')
print("작은따옴표 안에 '작은따옴표'를 쓰면 오류가 발생한다. (원래는 SyntaxError)")

print("그래서 문자열을 구현할 때 '작은따옴표'가 문자열 안에 들어있다면 문장을 큰따옴표로 감싸주고 사용한다.")



print('작은따옴표로만 구현할 때 \'역슬래시\'를 통해 예외 처리를 할 수도 있다.')
print("작은따옴표로만 구현할 때 '역슬래시'를 통해 예외 처리를 할 수도 있다.")

multi = """
줄바꿈
문자를
표현한다.
"""
print(multi)

print('Py' 'thon')  # Python



print(1 + 1)                # 2
print("1" + "1")            # 11
print("파이썬" + "좋아요")    # 파이썬좋아요
print("파이썬좋아요" * 3)     # 파이썬좋아요 x3


print('"문자는 숫자와 더할 수 없다." + 1  # 실행하면 TypeError 발생')

print(f"1+{1}")  # 1+1
num = 0
print(f"오늘의 코로나 확진자는 {num}명 입니다.")  # 오늘의 코로나 확진자는 0명 입니다.



address = "서울특별시 강서구 방화3동 827 국립국어원"
print(address)

from keyword import kwlist
print(kwlist)  # 예약어 목록



print(address[:])     # 전체
print(address[:5])    # 서울특별시
print(address[6:9])   # 강서구
print(address[::2])   # 2칸씩 건너뛴 문자열
print(address[::-1])  # 역순



print(len('국립 국어원'))                          # 6
print(len(set("서울 강서구 서울 국립국어원".split())))  # 3
print(len("서울 강서구 서울 국립국어원".split()))       # 4



use_python = " 인생은 짧아요. Python을 쓰세요! "
print(use_python.lower())   # 소문자 변환
print(use_python.upper())   # 대문자 변환
print(use_python.strip())   # 공백 제거
print(len(use_python))      # 23
print(len(use_python.strip()))  # 21


address_words = ['서울특별시', '강서구', '방화동', '국립국어원']
address_words.append('1층')
print(address_words)

address = "서울특별시 강서구 방화동 국립국어원"
words = address.split()
print(words)

address_words = ['서울특별시', '강서구', '방화동', '국립국어원']
address_words.sort()
print(address_words)


address_words = ['서울특별시', '강서구', '방화동', '국립국어원']
address_words.reverse()
print(address_words)

print(address_words[::-1])        # 슬라이싱 역순
print(" ".join(address_words))    # 공백 join
print("-".join(address_words))    # - join


for i in range(3):
    print("사랑해")

for i in range(1, 10, 3):
    print(i)



def text_preprocessing(txt):
    """
    문자열에 포함된 영문자를 소문자로 만들고
    문자열 양끝 공백을 제거하며
    구두점(.)을 제거하는 사용자 정의 함수
    """
    txt = txt.lower()
    txt = txt.strip()
    txt = txt.replace(".", "")
    return txt

txt = " Python 문자열 전처리 함수를 만들면 전처리 함수를 호출해서 여러 텍스트에 적용할 수 있습니다. "
print(text_preprocessing(txt))
