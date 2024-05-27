from websocket import create_connection
def stream_websocket_data():
    ws = create_connection("ws://localhost:4001")
    ws.send("face")
    result =  ws.recv()
    ws.close()
print(stream_websocket_data())
