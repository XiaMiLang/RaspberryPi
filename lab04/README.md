## This is a school lesson - CPS(Cyber-Physical Systems, 寰宇實體製造系統)

參考範例程式碼實做以下程式，並以規定介面執行：

1. ./read_ir.py [ir_pin] [led_pin] [key_map]
   * ir_pin, led_pin 以 GPIO.BOARD 為准
   * key_map 為 紅外線的訊號檔案 key_map.json(亦可自行錄製)
   * key_map.json時間請以毫秒為單位，每次接收到的符號請參考符號表
   * 若使用者按下 1 則 LED 燈開啟 0 則關閉
   * 符號表: 0 _
   * 符號表: 1 |
   * 符號表: start <
   * 符號表: end >

執行:

* 1st step: python3 irrecord.py 12 rec1.json
* 先錄製按鈕訊號
* 2nd step: python3 irrecogn.py 12 40 rec1.json
* 再辨識按鈕訊號，並執行 led 明滅的指令



![]( https://github.com/XiaMiLang/RaspberryPi/blob/master/lab04/lab04_IR.JPG ) 