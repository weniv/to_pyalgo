## 해당 정답은 정확하지 않은 정답일 수 있습니다. 추후 주피터 노트북을 함께 올리도록 하겠습니다.


# 1
# chr(int("1010101", 2))


def solution(data):
    if data[0] == "":
        return "welcome"
    answer = ""
    for i in data:
        answer += chr(int(i.replace(" ", "").replace("+", "1").replace("-", "0"), 2))
    return answer


testcase = [
    ["   + -- + - + -   "],
    ["   + --- + - +   ", "   + - + - + - +   "],
    [
        "   + -- + - + -   ",
        "   + --- + - +   ",
        "   + -- + - + -   ",
        "   + --- + - +   ",
    ],
    [""],
    [
        "   + -- + - + -   ",
        "   + --- + - +   ",
        "   + -- + - + -   ",
        "   + - + - + - +   ",
    ],
]

for t in testcase:
    print(solution(t))
