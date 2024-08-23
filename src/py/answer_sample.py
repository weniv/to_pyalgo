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


# 2
def solution(data):
    stones = data["돌의내구도"]
    dogs = data["독"]
    survivors = []
    print(stones)

    for dog in dogs:
        name = dog["이름"]
        jump = int(dog["점프력"])
        weight = int(dog["몸무게"])
        position = jump - 1
        alive = True

        while position < len(stones):
            print(name, stones, jump, weight)
            stones[position] -= weight

            if stones[position] < 0:
                alive = False
                break

            position += jump

            if position >= len(stones):
                survivors.append(name)
                break

    if survivors:
        return f"생존자: {', '.join(survivors)}"
    else:
        return "아무도 못건넜습니다."


# 테스트
test_cases = [
    {
        "돌의내구도": [1, 2, 1, 4],
        "독": [
            {"이름": "루비독", "나이": "95년생", "점프력": "3", "몸무게": "4"},
            {"이름": "피치독", "나이": "95년생", "점프력": "3", "몸무게": "3"},
            {"이름": "씨-독", "나이": "72년생", "점프력": "2", "몸무게": "1"},
            {"이름": "코볼독", "나이": "59년생", "점프력": "1", "몸무게": "1"},
        ],
    },
    {
        "돌의내구도": [5, 3, 4, 1, 3, 8, 3],
        "독": [
            {"이름": "루비독", "나이": "95년생", "점프력": "3", "몸무게": "4"},
            {"이름": "피치독", "나이": "95년생", "점프력": "3", "몸무게": "3"},
            {"이름": "씨-독", "나이": "72년생", "점프력": "2", "몸무게": "1"},
            {"이름": "코볼독", "나이": "59년생", "점프력": "1", "몸무게": "1"},
        ],
    },
    {
        "돌의내구도": [5, 3, 4, 1, 3, 8, 3],
        "독": [{"이름": "루비독", "나이": "95년생", "점프력": "2", "몸무게": "10"}],
    },
]

for i, case in enumerate(test_cases, 1):
    print(f"테스트 케이스 {i} 결과:", solution(case))
