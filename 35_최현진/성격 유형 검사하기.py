def solution(survey, choices):
    answer = ''
    survey_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
                   'J': 0, 'M': 0, 'A': 0, 'N': 0}
    scores = [0, 3, 2, 1, 0, 1, 2, 3]

    for i, choice in enumerate(choices):
        if choice < 4:
            survey_dict[survey[i][0]] += scores[choice]
        else:
            survey_dict[survey[i][1]] += scores[choice]
    print(survey_dict)

    answer += 'R' if survey_dict['R'] >= survey_dict['T'] else 'T'
    answer += 'C' if survey_dict['C'] >= survey_dict['F'] else 'F'
    answer += 'J' if survey_dict['J'] >= survey_dict['M'] else 'M'
    answer += 'A' if survey_dict['A'] >= survey_dict['N'] else 'N'

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
