import pyautogui
import time
import dc3
import acc_data

def clear_input(input_text_x, input_text_y):
    time.sleep(0.3)
    pyautogui.doubleClick(input_text_x, input_text_y)

    pyautogui.typewrite('')
    time.sleep(0.3)


def click_button(window_title, account):
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        # window.maximize()

        time.sleep(1)  # Wait for the window to be fully activated and maximized

        input_text = pyautogui.locateCenterOnScreen(image='C:\\Users\\User\\Desktop\\bot\python\\input-text.png')
        if input_text is None:
            print("Text input not found.")
            return
        input_text_x, input_text_y = input_text
        pyautogui.click(input_text_x, input_text_y)
        time.sleep(1)
        pyautogui.typewrite(account)
        time.sleep(3)

        # button_position = pyautogui.locateCenterOnScreen(image='C:\\Users\\User\\Desktop\\bot\python\\btn_find.png')
        # if button_position is None:
        #     clear_input(input_text_x, input_text_y)
        #     print("Button not found.")
        #     return
        # time.sleep(1)
        # button_x, button_y = button_position
        # pyautogui.click(button_x, button_y)

        time.sleep(1)
        account_position = pyautogui.locateCenterOnScreen(image='C:\\Users\\User\\Desktop\\bot\python\\account_tag.png')
        if account_position is None:
            clear_input(input_text_x, input_text_y)
            print("Account position not found.")
            return
        account_position_x, account_position_y = account_position
        print(account_position_x, account_position_y)
        time.sleep(1)
        pyautogui.doubleClick(account_position_x + 60, account_position_y)

        time.sleep(1)
        function_button_position = pyautogui.locateCenterOnScreen(image='C:\\Users\\User\\Desktop\\bot\python\\function_button.png')
        if function_button_position is None:
            clear_input(input_text_x, input_text_y)
            print("function_button_position not found.")
            return
        time.sleep(1)
        function_button_position_x, function_button_position_y = function_button_position
        pyautogui.click(function_button_position_x, function_button_position_y)



        time.sleep(3)
        function_button_position = pyautogui.locateCenterOnScreen(image='C:\\Users\\User\\Desktop\\bot\python\\reload_button.png')
        if function_button_position is None:
            clear_input(input_text_x, input_text_y)
            print("reload_button not found.")
            return
        time.sleep(1)
        function_button_position_x, function_button_position_y = function_button_position
        pyautogui.click(function_button_position_x, function_button_position_y)

        acc_json = acc_data.get_settings_txt_by_account_id(account)
        jj = acc_data.get_settings_like_object(acc_json)
        print(jj)
        # dc3.close_settings_window('')


    except IndexError:
        print("Window not found.")

# Usage example
click_button("Lords Mobile Bot 4.9.9.0", "1625103499")