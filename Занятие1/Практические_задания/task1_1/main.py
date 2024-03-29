def get_distance(point: tuple) -> int:
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


def task(points: list) -> list:
#    return [get_distance(point) for point in points]  # через list comprehension
     return list(map(get_distance, points)) # via map  # через map

if __name__ == "__main__":
    pts = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(task(pts))
