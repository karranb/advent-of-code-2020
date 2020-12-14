input = """67
118
90
41
105
24
137
129
124
15
59
91
94
60
108
63
112
48
62
125
68
126
131
4
1
44
77
115
75
89
7
3
82
28
97
130
104
54
40
80
76
19
136
31
98
110
133
84
2
51
18
70
12
120
47
66
27
39
109
61
34
121
38
96
30
83
69
13
81
37
119
55
20
87
95
29
88
111
45
46
14
11
8
74
101
73
56
132
23"""


def find_diffs(_adapters):
    one_diffs = 0
    three_diffs = 0
    for i, x in enumerate(_adapters[1:]):
        y = _adapters[i]
        diff = x - y
        if diff == 1:
            one_diffs += 1
        elif diff == 3:
            three_diffs += 1
    return one_diffs, three_diffs


# def find_possibilities(_adapters):
#     cache = {}
#     def dp(x):
#         if x == len(_adapters) - 1:
#             return 1
#         if x in cache:
#             return cache[x]
#         answ = 0
#         for i in range(x + 1, len(_adapters)):
#             if _adapters[i] - _adapters[x] <= 3:
#                 answ += dp(i)
#         cache[x] = answ
#         return answ
#     return dp(0)


def find_possibilities2(_adapters):
    cache = {}

    def dp(x):
        if x in cache:
            return cache[x]
        answ = 1
        for i in range(x + 3, len(_adapters)):
            if _adapters[i] - _adapters[i - 3] <= 3:
                answ += dp(i)
            if _adapters[i - 1] - _adapters[i - 3] <= 3:
                answ += dp(i - 1)
        cache[x] = answ
        return answ

    return dp(0)


adapters = list(map(int, input.split("\n")))
adapters = [0] + adapters + [max(adapters) + 3]
adapters.sort()

one_diffs, three_diffs = find_diffs(adapters)

print("part1", one_diffs * three_diffs)
print("part2", find_possibilities2(adapters))
