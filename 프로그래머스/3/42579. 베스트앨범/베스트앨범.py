def solution(genres, plays):
    # 장르별로 가장 많이 재생된 노래 두개씩 모아 베스트 앨범 출시
    # 노래 고유 번호로 구분
    # 장르 > 노래 > 낮은 고유 번호
    
    # 장르별로 카운팅
    gdict = {} # 장르별 플레이 횟수를 카운팅할 딕셔너리
    gsdict = {} # 장르와 노래 번호를 저장할 딕셔너리
    for i in (set(genres)): 
        gdict[i] = 0 # 장르별 플레이 횟수 0으로 초기화
        gsdict[i] = []
    for i in range(len(plays)): # 노래별 play
        gdict[genres[i]] += plays[i] # i번째 곡이 속한 장르에 플레이 횟수 더하기
        gsdict[genres[i]].append([i, plays[i]]) # 장르별 곡 정보(번호, 플레이횟수)
    
    # 장르별 정렬
    gdict = dict(sorted(gdict.items(),  key = lambda x:x[1], reverse = True))
    # 장르별 노래 플레이 횟수 정렬
    for g in gdict:
        gsdict[g].sort(key= lambda x:x[1], reverse = True)
        
    answer = []
    for g in gdict:
        if len(gsdict[g]) == 1:
            answer.append(gsdict[g][0][0])
        else:
            for i in range(2):
                answer.append(gsdict[g][i][0])
    return answer