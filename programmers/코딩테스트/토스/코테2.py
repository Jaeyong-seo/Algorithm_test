def solution(csv_string, keyword):
    teams = [string.split(',') for string in csv_string.split('\n')]
    search_team = []
    answer = 0

    for t_idx,team in enumerate(teams):
        if keyword in team[1]:
            search_team.append(t_idx)

    for t_idx,team in enumerate(teams):
        try:
            if int(team[2]) in search_team:
                search_team.append(int(team[0]))
        except:
            pass

    search_team = list(set(search_team))

    for team in teams:
        try:
            if int(team[0]) in search_team:
                answer += int(team[3])
        except:
            pass
        
    return answer



print(solution("조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11","아웃"))