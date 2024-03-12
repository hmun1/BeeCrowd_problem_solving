import math

acceleration = 9.80665
pi = 3.14159
flag = 0
while True:
    try:
        height = float(input())
        if 1 <= height <= 150:
            p1, p2 = map(int, input().split())
            test_cases = int(input())
            for _ in range(test_cases):
                angle, speed = map(float, input().split())
                alpha = angle * pi / 180
                u_x = speed * math.cos(alpha)
                u_y = speed * math.sin(alpha)
                time = u_y / acceleration
                H = (u_y * u_y) / (2 * acceleration)
                H = H + height
                v_fy = math.sqrt(2 * acceleration * H)
                t_d = v_fy / acceleration
                time_t = (time + t_d)
                distance = u_x * time_t
                if distance >= p1 and distance <= p2:
                    print(f'{distance:.5f} -> DUCK')
                else:
                    print(f'{distance:.5f} -> NUCK')
        else:
            flag = 1
    except ValueError:
        pass    
    except EOFError:
        break

    if flag == 1:
        break
