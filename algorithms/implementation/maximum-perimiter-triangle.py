from itertools import combinations


def _is_degenerate(triangle: list[int]) -> bool:
    a, b, c = triangle
    return a + b <= c or a + c <= b or b + c <= a


def maximum_perimiter_triagle(sticks: list[int]) -> list[int]:
    triangles = combinations(sticks, 3)
    non_degenerate_triangles = [
        triangle for triangle in triangles if not _is_degenerate(triangle)
    ]

    if len(non_degenerate_triangles) == 0:
        return [-1]

    return sorted(max(non_degenerate_triangles, key=sum))


print(
    maximum_perimiter_triagle(
        [
            9,
            2015,
            5294,
            58768,
            285,
            477,
            72,
            13867,
            97,
            22445,
            48,
            36318,
            764,
            8573,
            183,
            3270,
            81,
            1251,
            59,
            95094,
        ]
    )
)
