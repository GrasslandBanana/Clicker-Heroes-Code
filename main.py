import pyautogui
import win32api
import keyboard
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Upgrade:
# 216 Y:  312 RGB: (255, 204,   0)

# Attack:
# X: 1183 Y:  507 RGB: (245, 202,  62)

# Next Stage:
# X: 1289 Y:   33 RGB: (255, 241,  17)

# Abilities:
# X:  280 Y:  349 RGB: (119,  22, 165) and X:  272 Y:  333 RGB: ( 58, 216,  14)
# X:  331 Y:  344 RGB: (186, 125,   0) and X:  323 Y:  328
# X:  376 Y:  347 RGB: ( 50,  50,  50) and X:  375 Y:  331

# powers:
# (Boss Timer): X: 1305 Y:  239 RGB: (254, 254, 254)
# X:  857 Y:  239 RGB: (255, 255, 219)

# menu Paper background color
# RGB: (236, 214, 138)

ability1 = 0
ability2 = 0
ability3 = 0

while not keyboard.is_pressed('q'):
    #   Next Stage:
    if pyautogui.pixel(1289, 35)[2] == 17:
        click(1269, 58)
    #   Abilities:
    elif ability1 == 0:
        if pyautogui.pixel(280, 349)[0] == 119 and pyautogui.pixel(272, 333)[0] != 58:
            click(280, 349)
            ab1 = 1
    elif ability2 == 0 and ability1 == 1:
        if pyautogui.pixel(331, 344)[0] == 186 and pyautogui.pixel(323, 328)[0] != 58:
            click(331, 344)
            ab2 = 1
    elif ability3 == 0 and ability2 == 1:
        if pyautogui.pixel(376, 347)[0] >= 250 and pyautogui.pixel(375, 331)[0] != 58:
            click(376, 347)
            ab3 = 1
    #   powers:
    elif pyautogui.pixel(1305, 239)[0] >= 250 and pyautogui.pixel(857, 239)[0] >= 250:
        click(1305, 239)
    #   Upgrade:
    elif ability1 == 0:
        if pyautogui.pixel(190, 312)[2] == 255 and pyautogui.pixel(280, 349)[0] == 236:
            click(190, 312)
    elif ability2 == 0:
        if pyautogui.pixel(190, 312)[2] == 255 and pyautogui.pixel(331, 344)[0] == 236:
            click(190, 312)
    elif ability3 == 0:
        if pyautogui.pixel(190, 312)[2] == 255 and pyautogui.pixel(376, 347)[0] == 236:
            click(190, 312)
    #   Attack:
    else:
        click(1183, 507)
