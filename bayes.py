
def total(prob_A, prob_A_inter_C, prob_B, prob_B_inter_C):
    return (prob_A*prob_A_inter_C) + (prob_B*prob_B_inter_C)


def bayes(prior_A, prob_B_inter_A, prob_B):
    return (prior_A * prob_B_inter_A) / prob_B


if __name__ == "__main__":
    # ejercicio_1
    men = 0.4
    men_workout = 0.8
    women = 0.6
    women_workout = 0.5
    total_people_workout = total(men, men_workout, women, women_workout)
    print('Ejercicio 1')
    print('probabilidad que la persona haga ejercicio =', round(total_people_workout,2))
    workout_men = bayes(men, men_workout, total_people_workout)
    print('probabilidad de escojer un hombre en el grupo de personas que se ejercitan =', round(workout_men, 2))
    print('-------------------')
    #ejercicio_2
    can_25 = 0.5
    can_40 = 0.5
    defective_can_25 = 0.01
    defective_can_40 = 0.04
    total_defective_cans = total(can_25, defective_can_25, can_40, defective_can_40)
    print('Ejercicio 2')
    print('Probabilidad de que salgan latas defectuosas =', round(total_defective_cans, 2))
    prob_defective_can40 = bayes(can_40, defective_can_40, total_defective_cans)
    print('Probabilidad de que una lata defectuosa sea de 40ml =', round(prob_defective_can40, 2))
    print('-------------------')
    #ejercicio_3
    middle_lower_class = 0.75
    upper_class = 0.25
    candidate_votes_middle = 0.5
    candidate_votes_upper = 0.9
    total_votes_candidate = total(middle_lower_class, candidate_votes_middle, upper_class, candidate_votes_upper)
    print('Ejercicio 3')
    print('Probalidad de que se vote por el candidato A =', round(total_votes_candidate, 2))
    prob_candidate_vote_middle = bayes(middle_lower_class, candidate_votes_middle, total_votes_candidate)
    print('Probabilidad que el voto del candidato A sea de clase media o baja =', round(prob_candidate_vote_middle, 2))
