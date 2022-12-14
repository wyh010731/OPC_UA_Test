from flask import Flask, render_template, request  # 引用 后端通讯包
from flask_cors import CORS  # 导入模块
from pickle import TRUE
from opcua import Client
from opcua import ua

BL1 = 'ns=3;s="数据块_1"."BL1"'
BL2 = 'ns=3;s="数据块_1"."BL2"'
BL3 = 'ns=3;s="数据块_1"."BL3"'
BL4 = 'ns=3;s="数据块_1"."BL4"'

app = Flask(__name__)  # 实例化一个Flask对象

CORS(app, supports_credentials=True)


# 设置函数 index的路由 访问函数的网址为 http://127.0.0.1:8987/index
@app.route("/index", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':  # 判断POST方式，获取参数
    person = str(request.values.get("person"))
    res = opc_read(person)
    return {'person': res}
  elif request.method == "GET":  # 判断GET方式获取参数
    return request.args.get("person")


# 设置函数 index的路由 访问函数的网址为 http://127.0.0.1:8987/index
@app.route("/index1", methods=['GET', 'POST'])
def index1():
  if request.method == 'POST':  # 判断POST方式，获取参数
    node = request.values.get("node")
    value = request.values.get("value")
    res1 = opc_write(str(node), value)
    return res1
  elif request.method == "GET":  # 判断GET方式获取参数
    return request.args.get("person1")


plc1 = Client("opc.tcp://192.168.0.1:4840/")


# plc1.connect()
# print("PLC connect")
# valuetemp = plc1.get_node(BL1).get_value()
# print(valuetemp)


def opc_init():
  try:
    plc1.connect()
    print("PLC connect")
  except Exception as e:
    print(e)
    return


# OPC读数据
def opc_read(node):
  try:
    if str(node) == '1':
      var = plc1.get_node(BL1)
    elif str(node) == '2':
      var = plc1.get_node(BL2)
    elif str(node) == '3':
      var = plc1.get_node(BL3)
    elif str(node) == '4':
      var = plc1.get_node(BL4)
    valuetmp = var.get_value()
    print(valuetmp)
    return valuetmp
  except Exception as e:
    print(e)
    return


# OPC写数据
def opc_write(node, value):
  try:
    if str(node) == '5':
      var = plc1.get_node(BL1)
      value = ua.DataValue(int(value))
    elif str(node) == '6':
      # if value == "True":
      var = plc1.get_node(BL2)
      value = ua.DataValue(int(value))
    elif str(node) == '7':
      var = plc1.get_node(BL3)
      value = ua.DataValue(int(value))
    elif str(node) == '8':
      var = plc1.get_node(BL4)
      value = ua.DataValue(int(value))
    var.set_value(value)
    return "ok"

  except Exception as e:
    print(e)
    return


# 初始化函数
opc_init()

# 运行FLASK服务器
app.run(host='0.0.0.0', port=8987, debug=True)
