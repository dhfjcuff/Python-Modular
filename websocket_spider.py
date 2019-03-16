# -*- coding：utf-8 -*-

import websocket

url = 'ws://demos.kaazing.com/echo'
ws = websocket.create_connection(url=url, timeout=15)

ws.send("以字符串发送数据")     # 以字符串发送消息
ws.recv()      # 接收消息，如果无消息将会堵塞,直到15s超时等待结束

ws.send_frame("以帧形式发送数据")   # 以帧形式发送数据
ws.recv_data_frame()    # 接收以帧发送的数据

ws.send_binary("以二进制格式发送数据".encode())   # 以二进制格式发送数据

ws.send_close()  # 向服务器发送关闭连接请求，传入状态码及其原因

ws.close()  # 关闭连接

if __name__ == '__main__':
    ws