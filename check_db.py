import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    url = "https://palrocketchat.asia-southeast1.firebasedatabase.app/messages.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    for k, v in data.items():
        if not isinstance(v, dict):
            print(f"Message {k} is not a dictionary! Value: {v}")
            continue
        channel = v.get('channelId')
        sender = v.get('senderName')
        senderId = v.get('senderId')
        content = v.get('content')
        timestamp = v.get('timestamp')
        
        print(f"Key: {k} | Channel: {channel} | Sender: {sender} | SenderId: {senderId} | Timestamp: {timestamp} | Content: {content}")
        
        # Check missing fields
        missing = []
        if not channel: missing.append("channelId")
        if not sender: missing.append("senderName")
        if not senderId: missing.append("senderId")
        if timestamp is None: missing.append("timestamp")
        if content is None: missing.append("content")
        
        if missing:
            print(f"  --> WARNING: Missing fields: {missing}")
            
except Exception as e:
    print("Error:", e)
