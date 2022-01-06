hand_info = {
        1 : (1,4),
        2 : (2,4),
        3 : (3,4),
        4 : (1,3),
        5 : (2,3),
        6 : (3,3),
        7 : (1,2),
        8 : (2,2),
        9 : (3,2),
        10 : (1,1), # '*'
        0 : (2,1),
        12 : (3,1) # '#'
    }

class Handlocation:
    def left_hand(number, result): # 왼손 현재 위치
        left_info = hand_info[number]
        result += "L"
        return left_info, result

    def right_hand(number, result): # 오른손 현재 위치
        right_info = hand_info[number]
        result += "R"
        return right_info, result

    def hand_distance(number, left_info, right_info): # 2, 5, 8, 0 기준 왼손과 오른손의 거리
        left_distance = abs(hand_info[number][0]-left_info[0]) + abs(hand_info[number][1] - left_info[1])
        right_distance = abs(hand_info[number][0]-right_info[0]) + abs(hand_info[number][1] - right_info[1])
        return left_distance, right_distance

def solution(numbers, hand):
    result = ''
    left_info = hand_info[10]
    right_info = hand_info[12]

    for number in numbers:
        if number in [1, 4, 7]: # 왼손이 누르는 번호
            left_info, result = Handlocation.left_hand(number, result)
        elif number in [3, 6, 9]: # 오른손이 누르는 번호
            right_info, result = Handlocation.right_hand(number, result)
        else: # 2, 5, 8, 0
            left_distance, right_distance = Handlocation.hand_distance(number, left_info, right_info)

            if left_distance < right_distance:
                left_info, result = Handlocation.left_hand(number, result)
            elif left_distance > right_distance:
                right_info, result = Handlocation.right_hand(number, result)
            else: # 두 손의 거리가 같다면
                if hand == "right":
                    right_info, result = Handlocation.right_hand(number, result)
                elif hand == "left":
                    left_info, result = Handlocation.left_hand(number, result)
    return result