import tkinter as tk
from tkinter import ttk
import schedule
import time
from playsound import playsound
from datetime import datetime
import os
from PIL import Image, ImageTk
import threading

class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("알람 종소리")
        self.root.geometry("380x700")
        self.root.configure(bg="#2D2F36")
        self.root.resizable(False, False)

        # 스타일 설정
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#2D2F36")
        
        # 메인 컨테이너
        self.container = ttk.Frame(root, style="Custom.TFrame")
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 시계 영역
        self.create_clock_section()
        
        # 알람 목록 영역
        self.create_alarm_list()
        
        # 컨트롤 버튼
        self.create_control_section()
        
        # 초기 상태
        self.running = False
        
        # 시계 업데이트 시작
        self.update_clock()

    def create_clock_section(self):
        clock_frame = ttk.Frame(self.container, style="Custom.TFrame")
        clock_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.time_label = tk.Label(
            clock_frame,
            font=("Helvetica", 48, "bold"),
            fg="#FFFFFF",
            bg="#2D2F36"
        )
        self.time_label.pack()
        
        self.date_label = tk.Label(
            clock_frame,
            font=("Helvetica", 14),
            fg="#8A8D95",
            bg="#2D2F36"
        )
        self.date_label.pack()

    def create_alarm_list(self):
        self.alarm_frame = ttk.Frame(self.container, style="Custom.TFrame")
        self.alarm_frame.pack(fill=tk.BOTH, expand=True)
        
        self.times = [
            ("1교시", "09:00"),
            ("2교시", "10:00"),
            ("3교시", "11:00"),
            ("4교시", "12:00"),
            ("5교시", "13:00"),
            ("6교시", "14:00"),
            ("7교시", "15:00"),
            ("8교시", "16:00"),
            ("9교시", "17:00"),
            ("10교시", "18:00")

        ]
        
        for period, time in self.times:
            self.create_alarm_item(period, time)

    def create_alarm_item(self, period, time):
        frame = tk.Frame(self.alarm_frame, bg="#373A41")
        frame.pack(fill=tk.X, pady=5)
        frame.bind("<Enter>", lambda e: frame.configure(bg="#424752"))
        frame.bind("<Leave>", lambda e: frame.configure(bg="#373A41"))
        
        # 왼쪽 - 교시
        period_label = tk.Label(
            frame,
            text=period,
            font=("Helvetica", 12, "bold"),
            fg="#FFFFFF",
            bg="#373A41"
        )
        period_label.pack(side=tk.LEFT, padx=15, pady=12)
        
        # 중앙 - 시간
        time_label = tk.Label(
            frame,
            text=time,
            font=("Helvetica", 12),
            fg="#8A8D95",
            bg="#373A41"
        )
        time_label.pack(side=tk.LEFT, padx=5)
        
        # 오른쪽 - 테스트 버튼
        test_btn = tk.Button(
            frame,
            text="테스트",
            font=("Helvetica", 10),
            fg="#FFFFFF",
            bg="#4CD964",
            command=self.play_alarm,
            relief=tk.FLAT,
            cursor="hand2"
        )
        test_btn.pack(side=tk.RIGHT, padx=5)
        
        # 상태 표시
        status_label = tk.Label(
            frame,
            text="ON",
            font=("Helvetica", 11),
            fg="#4CD964",
            bg="#373A41"
        )
        status_label.pack(side=tk.RIGHT, padx=15)

    def create_control_section(self):
        control_frame = ttk.Frame(self.container, style="Custom.TFrame")
        control_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.toggle_btn = tk.Button(
            control_frame,
            text="알람 시작",
            font=("Helvetica", 12, "bold"),
            fg="#FFFFFF",
            bg="#007AFF",
            command=self.toggle_alarm,
            height=2,
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.toggle_btn.pack(fill=tk.X)

    def update_clock(self):
        current_time = datetime.now()
        self.time_label.config(text=current_time.strftime("%H:%M"))
        self.date_label.config(text=current_time.strftime("%Y년 %m월 %d일"))
        self.root.after(1000, self.update_clock)

    def play_alarm(self):
        try:
            alarm_path = os.path.join(os.path.dirname(__file__), "Alram_1.mp3")
            print(f"알람 파일 경로: {alarm_path}")
            print(f"파일 존재여부: {os.path.exists(alarm_path)}")
            playsound(alarm_path)
            print(f"알람 실행: {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"알람 재생 오류: {str(e)}")

    def toggle_alarm(self):
        if not self.running:
            self.running = True
            self.toggle_btn.config(text="알람 중지", bg="#FF3B30")
            threading.Thread(target=self.run_schedule, daemon=True).start()
        else:
            self.running = False
            self.toggle_btn.config(text="알람 시작", bg="#007AFF")

    def run_schedule(self):
        for _, time in self.times:
            schedule.every().day.at(time).do(self.play_alarm)
        
        while self.running:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()