# 캠 연결하기
import cv2
import mediapipe as mp
import time

def get_ready_gadgets(gadget_inventory, target_status):
    result = []
    for gadget in gadget_inventory:
        if gadget['status'] == target_status:
            result.append(gadget['name'])
    return result

batman_gadgets = [
    {'name': '배터랭', 'status': '준비완료'},
    {'name': '갈고리총', 'status': '충전중'},
    {'name': '연막탄', 'status': '준비완료'},
    {'name': '박쥐 시그널', 'status': '고장'}
]

# mediapipe 사용하기
# 손찾디 관련 기능 불러오기
mp_hands = mp.solutions.hands
# 손 그려주는 기능 불러오기
mp_drawing = mp.solutions.drawing_utils
# 손 찾기 관연 세부 설정
hands = mp_hands.Hands(
    max_num_hands=2,  # 탐지할 최대 손의 객수
    min_detection_confidence=0.5,  # 표시할 손의 최소 정확도
    min_tracking_confidence=0.5  # 표시할 관잘의 최소 정확도

)
# video에 opencv를 통해 웹 캠을 불러옴
video = cv2.VideoCapture(0)

#video(웹캡이 불러와서  열려 있는)가 열러 있는 동안에
while video.isOpened():
    #변수 ,ret , img에 video에서 읽은 값을 저장
    #변수 img  프레임을 저장
    ret, img = video.read()
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)  # 손 탐지하기

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if not ret:
        break
    # 찾은 손 표시하기
    if result.multi_hand_landmarks is not None:
        time.sleep(0.5)
        for hand_idx, res in enumerate(result.multi_hand_landmarks):
            print(f"\n[손 {hand_idx + 1}]")
            for i, lm in enumerate(res.landmark):
                x, y, z = lm.x, lm.y, lm.z
                # print(f"  랜드마크 {i}: x={x:.4f}, y={y:.4f}, z={z:.4f}")
                if x >0.2 and x < 0.4 :
                    print("정확한 암호 입니다. 실행합니다.")
                    str1 = input("선택하세요 1 : 준비완료  2: 고장  3: 분실  4: 충전중")
                    print(get_ready_gadgets(batman_gadgets,str(str1)))
                else:
                    print("암호가 틀렸습니다..")

            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)



        # print(result.multi_hand_landmarks)
        # for res in result.multi_hand_landmarks:
        #     mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

    k = cv2.waitKey(30)
    if k == 49:
        break
    cv2.imshow('hand', img)
video.release()
cv2.destroyAllWindows()