import pyautogui
import time
import keyboard
from pynput.mouse import Controller, Button

# ========== تنظیمات ==========
POINT_1 = (48, 524)
POINT_2 = (129, 414)
POINT_3 = (777, 492)
POINT_4 = (112, 287)
POINT_5 = (53, 457)
POINT_6 = (555, 363)
POINT_7 = (474, 493)

TOTAL_CLICKS = 30
CLICK_DELAY = 0.03
CLICKS_AFTER_1 = 15  # تعداد کلیک بعد از زدن کلید 1

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

mouse = Controller()

def fast_click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)

def click_point(x, y, label=""):
    pyautogui.click(x, y)
    if label:
        print(f"  ✓ {label} → ({x}, {y})")

def farm_sequence():
    """مرحله 4"""
    print("  🔥 شروع مرحله فارم...")

    # --- کلید 1 + 15 کلیک ---
    keyboard.press_and_release('1')
    time.sleep(0.1)
    print("  ✓ کلید 1 زده شد")

    for i in range(CLICKS_AFTER_1):
        fast_click(POINT_4[0], POINT_4[1])
        time.sleep(CLICK_DELAY)
    print(f"  ✓ {CLICKS_AFTER_1} کلیک بعد از کلید 1")

    # --- کلید Z فقط یکبار + یک کلیک ---
    keyboard.press_and_release('z')
    time.sleep(0.1)
    fast_click(POINT_4[0], POINT_4[1])
    time.sleep(0.1)
    print("  ✓ کلید Z + کلیک (فقط یکبار)")

    # --- 5 بار کلید A + کلیک ---
    for a in range(5):
        keyboard.press_and_release('a')
        time.sleep(0.1)
        fast_click(POINT_4[0], POINT_4[1])
        time.sleep(0.1)
    print("  ✓ 5 بار کلید A + کلیک")

    # --- 15 کلیک باقیمانده (تا 30 بشه) ---
    remaining = TOTAL_CLICKS - CLICKS_AFTER_1
    for i in range(remaining):
        fast_click(POINT_4[0], POINT_4[1])
        time.sleep(CLICK_DELAY)
    print(f"  ✓ {remaining} کلیک باقیمانده (مجموع {TOTAL_CLICKS})")

    # --- QWER دو بار ---
    for repeat in range(2):
        print(f"  🔁 دور {repeat + 1} QWER")
        for key in ['q', 'w', 'e', 'r']:
            keyboard.press_and_release(key)
            time.sleep(0.1)
            fast_click(POINT_4[0], POINT_4[1])
            time.sleep(0.1)
            print(f"  ✓ کلید {key.upper()} + کلیک")

def main_loop():
    cycle = 1
    while True:
        print(f"\n{'='*70}")
        print(f"🔁 سیکل شماره {cycle}")
        print(f"{'='*70}")

        print("[مرحله 1]")
        click_point(POINT_1[0], POINT_1[1], "کلیک روی نقطه 1")
        time.sleep(1)

        print("[مرحله 2]")
        click_point(POINT_2[0], POINT_2[1], "کلیک روی نقطه 2")
        time.sleep(1)

        print("[مرحله 3]")
        click_point(POINT_3[0], POINT_3[1], "کلیک روی نقطه 3")
        time.sleep(5)

        print("[مرحله 4]")
        farm_sequence()
        print("  ⏳ صبر 70 ثانیه...")
        time.sleep(70)

        print("[مرحله 5]")
        click_point(POINT_5[0], POINT_5[1], "کلیک روی نقطه 5")
        time.sleep(1)

        print("[مرحله 6]")
        click_point(POINT_6[0], POINT_6[1], "کلیک روی نقطه 6")
        time.sleep(2)

        print("[مرحله 7]")
        click_point(POINT_7[0], POINT_7[1], "کلیک روی نقطه 7")

        print("[مرحله 8] ⏳ صبر 6 ثانیه قبل از تکرار...")
        time.sleep(6)

        cycle += 1

def wait_for_start():
    print("=" * 70)
    print("🤖 اتو کلیکر آماده است")
    print("=" * 70)
    print("▶  شروع: کلید F6")
    print("⏹  توقف: کلید F7 (یا ماوس به گوشه چپ بالا)")
    print("=" * 70)
    print("منتظر F6...")

    keyboard.wait('F6')
    print("✅ شروع شد! برای توقف F7 رو بزن یا ماوس رو به گوشه چپ بالا ببر")
    time.sleep(1)

if __name__ == "__main__":
    try:
        wait_for_start()

        import threading
        def check_stop():
            keyboard.wait('F7')
            print("\n⛔ توقف توسط کاربر")
            import os
            os._exit(0)

        threading.Thread(target=check_stop, daemon=True).start()

        main_loop()

    except pyautogui.FailSafeException:
        print("\n⛔ توقف ایمنی (ماوس به گوشه رفت)")
    except KeyboardInterrupt:
        print("\n⛔ توقف توسط کاربر")