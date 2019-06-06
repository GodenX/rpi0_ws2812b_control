## rpi0_ws2812b_control
----------------------------------------------------

### Files :
- rpi0_ws2812b
    - app.py --------------------- 执行文件
    - mainwindow.py ---------- 主窗口布局
    - server_config.py --------- 服务器连接窗口
    - help.md -------------------- 使用说明

### Python Version : 
- V3.7.x
- Dependency:
    - PyQt5
    - paho-mqtt


### Description :
- 程序通过MQTT远程连接彩灯内置的服务器
- 使用程序内置选项控制彩灯显示特定效果 

### Change Log:

- v0.4(2019.06.06):
    - 添加模式0
    - 修复部分BUG

- v0.3.02(2019.06.05):
    - 修复部分BUG

- v0.3.01(2019.06.04):
    - 增加照明按钮

- v0.3(2019.05.31):
    - 修改UI界面，简化操作
    - 更新帮助文档
    - 修复部分BUG

- v0.2(2019.05.18):
    - 添加帮助文档
    - 修复部分BUG

- v0.1(2019.05.17):
    - 新增对MQTT通讯的支持
    - 新增说明文档


**Author**         : Jackie Yang  
**Email**          : czyangyinghao@163.com  
**Date**           : 15/05/2019
