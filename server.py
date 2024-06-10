
from simple_websocket_server import WebSocketServer, WebSocket
from pymongo import MongoClient,DESCENDING
import json 
# db_connection = MongoClient("mongodb://adminUser:123456@localhost:27017")
db_connection = MongoClient("mongodb://localhost:27017/")

db_plate = db_connection.mini_hplate
EventPlate = db_plate["event"]

parking_object_collection=db_plate["parking_object"]

class SimpleEcho(WebSocket):
  
    def handle(self):
        print(self.data , type(self.data))
       
        message=json.loads(self.data)
        print(message)
        print("WWWWWWWWWWWWWW")
        # counter=0
        if message["command"]=='plate' and message["is_8_digit"]=="True":
            for client in self.server.connections.values():
                print("                printis_8_digit     True")
                # print(list(EventPlate.find().sort('_id',DESCENDING).limit(5)))
                # whole_data={"data_plate":list(EventPlate.find({},{'_id':0}).sort('_id',DESCENDING).limit(5)) ,
                #  "data_confirmed":list(parking_object_collection.find({},{'_id':0}).sort('_id',DESCENDING).limit(5))}
                # client.send_message(json.dumps(whole_data))
                print(json.dumps({'data_plate':list(EventPlate.find({},{'_id':0}).sort('_id',DESCENDING).limit(5))}))
                client.send_message(json.dumps({'data_plate':list(EventPlate.find({},{'_id':0}).sort('_id',DESCENDING).limit(5))}))
                # print(counter)
                # counter+=1
                # client.send_message(json.dumps({'data_confirmed':list(parking_object_collection.find({},{'_id':0}).sort('_id',DESCENDING).limit(5))}))
        if message["command"]=='plate' and message["is_8_digit"]=="False":
            print("                printis_8_digit     False")
            for client in self.server.connections.values():
                
                print("now front you should make a request to api: ")
                
                client.send_message(json.dumps({"data_plate":"now front you should make a request to api: "}))
        if message["command"]=='plate' and message["is_8_digit"]=="k":
            for client in self.server.connections.values():
                print("passsss")
                client.send_message(json.dumps({"data_plate":"First time do not have answer"}))
            
                
                # print("now front you should make a request to api: ")
                
                # client.send_message(json.dumps({"data_plate":"now front you should make a request to api: "}))
        print("YYYYYYYYYYy")       
        if message["command"]=="parkingObject":
            print("**************************8")
            for client in self.server.connections.values():
                client.send_message(json.dumps({'data_confirmed':list(parking_object_collection.find({},{'_id':0}).sort('_id',DESCENDING).limit(5))}))
            print("77777777777777777777777")
        #if self.data!="parkingObject" or self.data!='plate' :
            #self.send_message(self.data)
    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('', 4001, SimpleEcho)


server.serve_forever()
