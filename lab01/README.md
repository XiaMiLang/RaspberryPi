以規定介面執行:

1. lab01_led_1.py [led_pin:value]...
   * 得以根據輸入的針腳與 value 的多個配對，適當點亮 led
   * led_pin 以 GPIO.BOARD 為准
   * value 只可以是 True 或  Flase ，並對應程式內之 True 及 False

2. lab01_led_2.py [led_pin:value:freq]...
   * 擴充 setup_led.py 使其得以讀入 針腳、value、freq 三種數據之配對，並根據所輸入之資訊適當點亮 led
   * value 可以是 0~100 任一正整數
   * freq 可以是任意正整數。

![](https://github.com/XiaMiLang/RespberryPi/blob/master/lab01/lab01_led.JPG)