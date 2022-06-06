# 파일 내용 불러와 공백 문자, 줄 바꿈 문자 없애기
with open("파일 이름", "r") as f:
    data = f.readlines()
    for i in len(data):
        data[i] = data[i].strip()
# 예외처리
try:
    pass
except FileNotFoundError:
    pass
# 문자열에 문자 찾기
def finding(data, lines):
    result_data = []
    cnt = []
    counting = 0 # 몇 번째 문자열인지 카운트
    for i in data: # 전체 문장을 하나씩 꺼냄
        counting += 1
        new_data = str(i)
        locate_word = []
        startPos = 0
        if new_data.find(lines) != -1: # 찾지못하면 넘기기
            while True:
                if new_data.find(lines, startPos) != -1: # 찾으면
                    locate_word.append(new_data.find(lines, startPos)+1) # 단어 위치 추가
                    startPos += new_data.find(lines, startPos)+1 # 그 다음 위치에서 찾기
                else:
                    locate_word = tuple(locate_word) # 못찾으면 찾았던 위치들 튜플로 리턴
                    break
            result_data.append(locate_word) # 한 문자열에서 찾았던 단어 위치들 추가
            result_data.append(new_data) # 문자열 저장
            cnt.append(counting) # 몇 번째 문자열인지 저장
    return cnt, result_data, lines