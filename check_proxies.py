import requests 
import threading 

import queue 
q=queue.Queue() 

valid_proxies=[] 

with open('proxies.txt','r') as f : 
    proxies=f.read().split('\n')

    for p in proxies : 
        q.put(p)

def chec_proxies(): 
    global q 
    while not q.empty() : 
        proxy=q.get() 
        test_url = "http://httpbin.org/ip"
        try : 
            res = requests.get(test_url,
                               proxies={'http':proxy
                                        ,'https':proxy},timeout=5)
            
        except : 
            continue 
        if res.status_code==200: 
            print(proxy)        

for _ in range(10): 
    threading.Thread(target=chec_proxies).start()   