from websocket import create_connection
import json
def stream_websocket_data(is_8_digit):
    ws = create_connection("ws://localhost:4001")
    # ws.send("plate",1)
    message={"command":"plate","is_8_digit":str(is_8_digit)}
    print(message)
    ws.send(json.dumps(message))
    print('ssend')
    result =  ws.recv()
    print(result)
    x=json.loads(result)
    print("????????????????////",len(x["data_plate"]))
    #ws.close()
# print(stream_websocket_data())
def stream_websocket_parking_object(is_8_digit=True):
    print("FFFFFFFFF",is_8_digit)
    ws = create_connection("ws://localhost:4001")
    message={"command":"parkingObject","is_8_digit":str(is_8_digit)}
    ws.send(json.dumps(message))
    result =  ws.recv()
    x=json.loads(result)
    print("????????????????////",x)
    ws.close()
if __name__=="__main__":
    # stream_websocket_data(is_8_digit=True)
    # stream_websocket_data(is_8_digit="k")
    stream_websocket_parking_object()
    # while(True):
    #     x=stream_websocket_data()
    #     if x :
    #         exit
    #     # print(type(x))
    