import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import pygame

pygame.mixer.init()
app = tk.Tk()
app.title("Часы и будильник")
alarm_hour = None
alarm_minute = None
alarm_window = None
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    check_alarm()
    app.after(1000, update_time)
def set_alarm():
    global alarm_hour, alarm_minute
    alarm_time = simpledialog.askstring("Установка будильника", "Введите время будильника (чч:мм):")
    if alarm_time:
        alarm_time = alarm_time.strip()
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            alarm_label.config(text=f"Будильник установлен на {alarm_time}")
        except ValueError:
            alarm_label.config(text="Неверный формат времени")
    else:
        alarm_hour = None
        alarm_minute = None
        alarm_label.config(text="Будильник не установлен")
def check_alarm():
    current_hour, current_minute, _ = map(int, time.strftime("%H:%M:%S").split(':'))
    if alarm_hour is not None and alarm_minute is not None and current_hour == alarm_hour and current_minute == alarm_minute:
        play_alarm()
def play_alarm():
    pygame.mixer.music.load("other/alarm.mp3")
    pygame.mixer.music.play()
    show_alarm_window()
def show_alarm_window():
    global alarm_window
    if alarm_window is None:
        alarm_window = tk.Toplevel(app)
        alarm_window.title("Будильник!")
        alarm_label = tk.Label(alarm_window, text="Пора просыпаться!")
        alarm_label.pack()
        stop_button = tk.Button(alarm_window, text="Стоп", command=stop_alarm)
        stop_button.pack()
def stop_alarm():
    pygame.mixer.music.stop()
    if alarm_window:
        alarm_window.destroy()
time_label = tk.Label(app, text="", font=("Helvetica", 48))
time_label.pack()
set_alarm_button = tk.Button(app, text="Установить будильник", command=set_alarm)
set_alarm_button.pack()
alarm_label = tk.Label(app, text="Будильник не установлен", font=("Helvetica", 18))
alarm_label.pack()
update_time()
app.mainloop()
