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


# 3
def solution(data):
    date, waiting = data
    # print(date, waiting)
    days_in_month = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]
    boats = [25, 15, 15, 15, 15, 15]

    def add_days(year, month, day, days):
        while days > 0:
            if day + days <= days_in_month[month - 1]:
                day += days
                break
            days -= days_in_month[month - 1] - day + 1
            day = 1
            month += 1
            if month > 10:
                year += 1
                month = 1
        return year, month, day

    year, month, day = map(int, date.split("."))

    people_per_day = 1200  # 하루 탑승할 수 있는 인원
    days = waiting // people_per_day
    remaining = waiting % people_per_day

    # 출발해야하는연도, 출발해야하는월, 출발해야하는일 = 함수(입력 연도, 입력 월, 입력일, 남은일)
    year, month, day = add_days(year, month, day, days)
    # print(year, month, day)

    hour, minute = 9, 0
    if remaining > 0:
        hour = remaining // 100 + 9
        # print(hour)
        minute = remaining % 100

        if minute == 0 or minute == 99:
            hour += 1
        if hour == 21:
            hour = 9
            day += 1
            if day == days_in_month[month - 1] + 1:
                day = 1
                month += 1
                if month > 10:
                    year += 1
                    month = 1

        if 23 >= minute > 0:
            minute = 0
        elif 38 >= minute:
            minute = 10
        elif 53 >= minute:
            minute = 20
        elif 68 >= minute:
            minute = 30
        elif 83 >= minute:
            minute = 40
        elif 98 >= minute:
            minute = 50

    return f"{year:04d}.{month:02d}.{day:04d} {hour:02d}:{minute:02d}"


# 테스트
test_cases = [
    ["2025.09.0001", 1],
    ["2025.09.0001", 1200],
    ["2025.09.0001", 1201],
    ["2025.09.0001", 2400],
    ["2025.09.0001", 4800],
    ["2025.09.0001", 14000605],
    ["2025.10.0001", 2046],
    ["2025.10.0002", 1],
]

for testcase in test_cases:
    # print(f"Input: {case}")
    # print(f"Output: {solution(*case)}\n")
    print(solution(testcase))


# 4
def solution(animals):
    chairs = []
    time = 0

    for animal in animals:
        if animal in chairs:
            # 이미 의자에 앉아있는 경우 (hit)
            chairs.remove(animal)
            chairs.append(animal)
            time += 1
        else:
            if len(chairs) < 3:
                # 빈 의자가 있는 경우
                chairs.append(animal)
                time += 60  # 1분 추가
            else:
                # 의자가 모두 차있는 경우
                chairs.pop(0)
                chairs.append(animal)
                time += 60  # 1분 추가

    minutes = time // 60
    seconds = time % 60

    return f"{minutes}분 {seconds}초"


# 테스트
test_cases = [
    [
        "척추동물",
        "어류",
        "척추동물",
        "무척추동물",
        "파충류",
        "척추동물",
        "어류",
        "파충류",
    ],
    ["척추동물", "어류", "무척추동물", "척추동물", "어류", "무척추동물"],
    ["무척추동물", "척추동물", "어류", "양서류", "파충류", "조류", "포유류"],
    ["척추동물", "척추동물", "척추동물", "척추동물"],
    ["어류", "파충류"],
    [
        "무척추동물",
        "척추동물",
        "어류",
        "양서류",
        "파충류",
        "조류",
        "포유류",
        "척추동물",
        "어류",
        "양서류",
        "파충류",
        "조류",
        "포유류",
        "무척추동물",
    ],
]

for i, case in enumerate(test_cases, 1):
    print(f"테스트 케이스 {i}:")
    print(f"입력: {case}")
    print(f"출력: {solution(case)}")
    print()


# 5
def solution(graph):
    visited = []
    stack = [100]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            subset = graph[n] - set(visited)
            if len(subset) == 0:
                visited += stack
                break
            stack.append(min(subset))
            print(stack)
            print(visited)

    small_chars = "".join([chr(num) for num in visited[1:]])

    visited = []
    stack = [100]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            subset = graph[n] - set(visited)
            if len(subset) == 0:
                visited += stack
                break
            stack.append(max(subset))
            print(stack)
            print(visited)

    large_chars = "".join([chr(num) for num in visited[1:]])

    print(f"{large_chars} {small_chars}")

    return f"{large_chars} {small_chars}"


# 테스트
test_graph = {
    100: set([67, 66]),
    67: set([100, 82, 63]),
    66: set([100, 73, 69]),
    82: set([67, 61, 79]),
    63: set([67]),
    73: set([66]),
    69: set([66, 65, 81]),
    61: set([82]),
    79: set([82, 87, 77]),
    65: set([69, 84, 99]),
    81: set([69]),
    87: set([79, 31, 78]),
    77: set([79]),
    84: set([65]),
    99: set([65]),
    31: set([87]),
    78: set([87]),
}

print(solution(test_graph))


# 6
def solution(data):
    import numpy as np

    farm1, farm2 = data
    farm1 = np.array(farm1)
    farm2 = np.rot90(farm2, 1)

    sum_farm = farm1 + farm2

    def row_to_unicode(row):
        num = int("".join(map(str, row)), 8)
        return chr(num) if 65 <= num <= 90 else str(num)

    result = "".join(row_to_unicode(row) for row in sum_farm)
    return result


# 테스트
test_cases = [
    (
        [
            [1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1],
        ],
        [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 3],
            [0, 0, 0, 0, 4],
            [0, 2, 0, 0, 2],
            [4, 5, 0, 2, 0],
        ],
    ),
    (
        [[0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]],
    ),
]

for i, data in enumerate(test_cases, 1):
    print(f"테스트 케이스 {i}:")
    print(f"출력: {solution(data)}")
