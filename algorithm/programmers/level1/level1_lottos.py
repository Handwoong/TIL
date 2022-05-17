def solution(lottos, win_nums):
    count = 0
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    # answer = []
    
    # 당첨번호와 대조
    for num in lottos:
        if win_nums.count(num) == 0: # 값이 없을 경우
            pass
        else:
            count += 1
    
    # maxrank = rank[count+lottos.count(0)]
    # minrank = rank[count]

    # answer.append(maxrank)
    # answer.append(minrank)
    # return answer
    return rank[count+lottos.count(0)], rank[count]