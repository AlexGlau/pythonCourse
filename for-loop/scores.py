students_scores = [
    {'school_grade': '4a', 'scores': [3,4,4,5,2]},
    {'school_grade': '5a', 'scores': [2,5,4,4,3]},
    {'school_grade': '6a', 'scores': [3,3,4,5,5]},
    {'school_grade': '7a', 'scores': [4,4,4,5,4]},
    {'school_grade': '8a', 'scores': [3,5,4,5,5]},
    {'school_grade': '9a', 'scores': [5,5,4,5,5]},
    {'school_grade': '10a', 'scores': [5,5,5,3,4]},
]

def average_score(by_grade=False):
    scores_sum = 0
    grade_score_len = 0

    for grade in students_scores:
        grade_score_len = grade_score_len + len(grade['scores'])
        for score in grade['scores']:
            scores_sum = scores_sum + score

        if by_grade:
            output = scores_sum / grade_score_len
            by_grade_score = round(output, 2)
            print('Average by grade: {score}'.format(score=by_grade_score))

    if by_grade == False:
        score_avg = scores_sum / grade_score_len
        res = round(score_avg, 2)
        print('Average by school: {result}'.format(result=res))

average_score()
