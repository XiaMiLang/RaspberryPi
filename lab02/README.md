以規定介面執行：

1. lab2_buzzer_1.py \[pin] [freq:freq]
   * 程式第一個參數為 pin，即輸出訊號之針腳，程式必須能根據傳入的 pin 動態決定輸出的針腳
   * Pin 編號以 GPIO.BOARD 為准
   * 程式第二個參數為頻率序列，為一正整數序列，以冒號 : 分割，程式需以一個頻率 0.1 秒的速度由左而右播放。
   * Ex. ./buzzer_mkvoice.py 2 523:589:659:698:784:880:988:1047
2. lab2_buzzer_2.py \[pin] [freq_sequence.json]
   * 程式讀入頻率序列方法轉換為讀取一個序列描述檔案，並根據其內描述的時長播放。
   * Ex. ./buzzer_play.py 2 bee.json



![](https://github.com/XiaMiLang/RespberryPi/blob/master/lab02/lab02_buzzer.png)