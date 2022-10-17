def solution(numbers, hand):
    answer = ''
    left_hand = 10
    right_hand = 12
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_hand = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right_hand = i
        else:
            
            if i == 0:
                i = 11
            
            abs_left_hand = abs(i-left_hand)
            abs_right_hand = abs(i-right_hand)
                
            if abs_left_hand%3 + abs_left_hand//3  > abs_right_hand%3 + abs_right_hand//3:
                answer += 'R'
                right_hand = i
            elif abs_left_hand%3 + abs_left_hand//3  < abs_right_hand%3 + abs_right_hand//3:
                answer += 'L'
                left_hand = i
            
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = i
                else:
                    answer += 'L'
                    left_hand = i
                
    return answer