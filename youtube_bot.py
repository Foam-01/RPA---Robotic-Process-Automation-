import pyautogui
import time

# ระบบหยุดฉุกเฉิน
pyautogui.FAILSAFE = True 
# ลดจังหวะหน่วงพื้นฐานลงเพื่อให้ทำงานต่อเนื่อง
pyautogui.PAUSE = 0.4

# รายชื่อพิกัดทั้งหมด 14 จุด
POINTS = [
    (1781, 144), (1700, 203), (954, 711), (1364, 268), 
    (1478, 268), (1150, 524), (1574, 749), (1503, 914), 
    (1437, 507), (1314, 633), (1496, 922), (1502, 908), 
    (1036, 825), (782, 723)
]

def start_bot():
    
    print("🚀 บอทกำลังจะเริ่มใน 10 วินาที... ")
    time.sleep(10)

    for i, pt in enumerate(POINTS, 1):
        
        # --- ขั้นตอนที่ 4: พิมพ์ Downloads (ปรับให้ไวขึ้น) ---
        if i == 4:
            print(f"⏳ {i}: พิมพ์ Downloads")
            time.sleep(2) 
            pyautogui.moveTo(pt[0], pt[1], duration=0.3)
            pyautogui.click()
            pyautogui.hotkey('alt', 'd')
            pyautogui.press('backspace') 
            pyautogui.write("Downloads", interval=0.05) 
            pyautogui.press('enter')
            time.sleep(1)

        # --- ขั้นตอนที่ 6: คลิกเลือกวิดีโอ (ปรับให้ไวขึ้น) ---
        elif i == 6:
            print(f"📍 {i}: Triple Click")
            pyautogui.moveTo(pt[0], pt[1], duration=0.3)
            pyautogui.click(clicks=3, interval=0.1) 
            time.sleep(3) 

        # --- ขั้นตอนที่ 14: ตั้งเวลา (ปรับให้ไวขึ้น) ---
        elif i == 14:
            print(f"⏳ {i}: ตั้งเวลาสุดท้าย")
            time.sleep(2) 
            pyautogui.moveTo(pt[0], pt[1], duration=0.3)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write("18:00", interval=0.05)
            pyautogui.press('enter')

        # --- ขั้นตอนปกติอื่นๆ (ปรับให้ไวขึ้น) ---
        else:
            print(f"📍 {i}: คลิกที่ {pt}")
            pyautogui.moveTo(pt[0], pt[1], duration=0.3) 
            pyautogui.click()
            time.sleep(2) 

    print("🏁 จบการทำงานครบ 14 จุด!")

if __name__ == "__main__":
    start_bot()