import pyautogui
import keyboard
import time

print("=" * 50)
print("🎯 ابزار گرفتن مختصات")
print("=" * 50)
print("ماوس رو روی نقطه مورد نظر ببر و F2 رو بزن")
print("برای خروج ESC رو بزن")
print("=" * 50)

point_number = 1
while True:
    if keyboard.is_pressed('F2'):
        x, y = pyautogui.position()
        print(f"نقطه {point_number}: ({x}, {y})")
        point_number += 1
        time.sleep(0.5)
    
    if keyboard.is_pressed('esc'):
        print("خروج...")
        break
    
    time.sleep(0.05)