"""

문제 푸는 데 걸린 시간: 1시간 28분 39초


note1) y좌표 값이 기본적인 좌표평면을 따르는 게 아니라 위쪽 방향으로 올라가면 값이 감소하고 아래쪽 방향으로 내려가면 값이 증가한다. 즉, 배열처럼 움직이는 형태이지 수학적인 좌표평면의 y좌표와는 달랐다.
이것 때문에 헷갈려서 시간을 좀 더 잡아먹었다.

note2) 좌표의 회전 변환을 몰라서 처음에는 혼자 고민하다가 결국 구글에 검색해서 좌표 변환 수식을 찾아서 적용했다.

note3) 각 세대 별 끝나는 부분의 좌표는 결국 최초 시작 지점의 좌표를 기준점을 중심으로 회전시켜서 도착한 곳의 좌표이다. 굳이 선분을 따라서 이동한다거나 할 필요없다.

note4) 사각형의 개수를 세기 위해 드래곤커브가 이루는 커다란 사각형 내부의 1x1 사각형 개수를 셌다. -> 더 효율적인 방법이 있지 않을까???


"""




import sys


input = sys.stdin.readline


class DragonCurve:
    def __init__(self, init_x: int, init_y: int, init_d: int):
        self.points: set[tuple[int, int]] = set()
        self.points.add((init_x, init_y))
        
        self.d: int = init_d
        self.gen: int = -1
        self.start_point: tuple[int, int] = (init_x, init_y)
        self.end_point: tuple[int, int] = None
    
    
    def _init_gen(self):
        if self.gen == -1:
            if len(self.points) != 1:
                raise Exception("unreachable!")
            
            # d == 0, 1, 2, 3
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            
            # set의 첫 번째 원소 추출하는 방법
            p = None
            for elem in self.points:
                p = elem
                break
            x, y = p
            new_point = (x + dx[self.d], y + dy[self.d])
            self.points.add(new_point)
            
            self.gen += 1
            self.end_point = new_point
            
    
    def _rotate(self, p: tuple[int, int], c: tuple[int, int]) -> tuple[int, int]:
        # c를 기준으로 p를 시계 방향으로 90도 회전시킨다.
        x, y = p
        x_c, y_c = c
        return (y - y_c + x_c, -x + x_c + y_c)
        
    
    def next_gen(self):
        if self.gen == -1:
            self._init_gen()
        else:
            new_points = list()
            for p in self.points:
                if p != self.end_point:
                    new_points.append(self._rotate(p, self.end_point))
            
            for new_p in new_points:
                self.points.add(new_p)
                
            self.end_point = self._rotate(self.start_point, self.end_point)
            self.gen += 1
    
    
    def count_square(self):
        xlist = [x for x, _ in self.points]
        ylist = [y for _, y in self.points]
        
        minx = min(xlist)
        maxx = max(xlist)
        miny = min(ylist)
        maxy = max(ylist)
        
        """
        3 2
        0 1
        """
        dx = [0, 1, 1, 0]
        dy = [0, 0, 1, 1]
        
        cnt = 0
        
        for x in range(minx, maxx):
            for y in range(miny, maxy):
                nxlist = [x + d for d in dx]
                nylist = [y + d for d in dy]
                no_square = False
                for nx, ny in zip(nxlist, nylist):
                    if (nx, ny) not in self.points:
                        no_square = True
                
                if not no_square:
                    cnt += 1
        
        return cnt 
    
    
    def merge_for_counting(self, other: 'DragonCurve') -> 'DragonCurve':
        for p in other.points:
            self.points.add(p)
    
    
    def print_points(self):
        for p in sorted(self.points, key=lambda x: (x[0], x[1])) :
            print(f"({p[0]}, {p[1]})", end=', ')
        print()
        
        

# dc = DragonCurve(0, 0, 0)
# dc.print_points()  # -1 gen
# dc.next_gen()  
# dc.print_points()  # 0 gen
# dc.next_gen()  
# dc.print_points()  # 1 gen
# dc.next_gen()
# dc.print_points()  # 2 gen
# print(dc.count_square()) # 1, 2 gen
# dc.next_gen()
# dc.print_points()  # 3 gen
# print(dc.count_square()) # 3, 3 gen

# print("=========================")
# dc2 = DragonCurve(4, 2, 1)
# for _ in range(3 - dc2.gen):
#     dc2.next_gen()
#     dc2.print_points()



n = int(input())
arr = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr.append((x, -y, d, g))


cur = None

for x, y, d, g in arr:
    dc = DragonCurve(x, y, d)
    for _ in range(g - dc.gen):
        dc.next_gen()
    
    # dc.print_points()
    
    if cur is None:
        cur = dc
    else:
        cur.merge_for_counting(dc)

print(cur.count_square())