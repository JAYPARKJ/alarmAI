from playsound import playsound
import os

def test_audio():
    try:
        file_path = os.path.join(os.getcwd(), "Alram_1.mp3")
        print(f"테스트 파일 경로: {file_path}")
        print(f"파일 존재?: {os.path.exists(file_path)}")
        playsound(file_path)
        print("재생 성공!")
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    test_audio()