import schedule
import time
from playsound import playsound
from datetime import datetime
from pytube import YouTube
import os

def download_youtube_audio():
    # YouTube 동영상 URL
    url = "https://www.youtube.com/shorts/00iRFdVIlYQ"
    
    try:
        # 아직 벨소리가 없는 경우에만 다운로드
        if not os.path.exists("bell.mp3"):
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()
            # 오디오 다운로드
            audio.download(filename="bell.mp3")
            print("벨소리 다운로드 완료!")
    except Exception as e:
        print(f"다운로드 중 오류 발생: {e}")

def play_alarm():
    try:
        playsound("bell.mp3")
        print(f"알람 실행: {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"알람 재생 중 오류 발생: {e}")

# 수업 시간표 설정 (1교시 ~ 8교시)
schedule.every().day.at("09:30").do(play_alarm)  # 1교시
schedule.every().day.at("10:10").do(play_alarm)  # 2교시
schedule.every().day.at("11:10").do(play_alarm)  # 3교시
schedule.every().day.at("12:10").do(play_alarm)  # 4교시
schedule.every().day.at("13:10").do(play_alarm)  # 5교시
schedule.every().day.at("14:10").do(play_alarm)  # 6교시
schedule.every().day.at("15:10").do(play_alarm)  # 7교시
schedule.every().day.at("16:10").do(play_alarm)  # 8교시

print("알람 시스템이 시작되었습니다...")

# 프로그램 시작 시 벨소리 다운로드
download_youtube_audio()

# 나머지 스케줄링 코드는 동일하게 유지