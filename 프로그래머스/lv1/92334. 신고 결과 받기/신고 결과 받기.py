'''
1. 유저가 각각 신고한 아이디를 report 를 통해서 알아낸다.
2. k 이상 신고를 당한 사람의 아이디를 추출
3. 각 유저가 정지된 ID 를 신고한 사람이 결과 메일을 받는 갯수를 출력
'''

def solution(id_list, report, k):
    report_split = []
    problem_people = []
    report_people = []
    count_report = []
    count_reporter = []
    jail = []
    answer = []
    result = []
    
    report = list(set(report))
    for i in range(len(report)):
        report_split.append(report[i].split())
    
    for i in range(len(report_split)):
        problem_people.append(report_split[i][1])
        report_people.append(report_split[i][0])
        
    answer_set = list(set(problem_people))
    
    for i in answer_set:
        count_report.append(problem_people.count(i))
    
    for pair in zip(answer_set, count_report):
        if pair[1] >= k :
            jail.append(pair[0])
    
    for pair in zip(report_people, problem_people):
        
        if pair[1] in jail :
            answer.append(pair)

    for i in range(len(answer)):
        result.append(answer[i][0])

    for i in id_list:
        count_reporter.append(result.count(i))
        
    # for j in id_list:
    #     count_reporter.append(answer.count(j))
    # # print(answer[1])
    return count_reporter









