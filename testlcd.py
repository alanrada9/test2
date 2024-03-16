import Adafruit_CharLCD as LCD
import time

LCD_RS = 21
LCD_EN = 20
LCD_D4 = 16
LCD_D5 = 12
LCD_D6 = 7
LCD_D7 = 8
LCD_COLS = 16
LCD_ROWS = 2

lcd = LCD.Adafruit_CharLCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7, LCD_COLS, LCD_ROWS)

try:
    lcd.clear()
    lcd.message('Hola, LCD!')
    time.sleep(5)  # Mostrar durante 5 segundos
    lcd.clear()
except KeyboardInterrupt:
    lcd.clear()
    lcd.message('Saliendo...')
    time.sleep(2)
    lcd.clear()
