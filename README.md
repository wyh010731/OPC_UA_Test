# OPC_UA_Test
---
## 1.Client & Server side
-  前端与后端实现程序
-  前端使用HTML
-  后端使用python
- ```python 
    #后端与PLC连接代码
    plc1 = Client("opc.tcp://192.168.0.1:4840/")
    
## 2.io_link
- 此文件夹为西门子1500PLC程序
- 需使用TIA16打开项目文件
- 需要使用西门子**S7-PLCSIM Advanced V3.0**软件进行仿真
- PLC中需要设置PLC为服务器并开启OPC_UA服务
