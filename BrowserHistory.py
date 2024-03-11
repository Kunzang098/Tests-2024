from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

#visit function
NonfVisits = int(input("Enter the number of url history:"))
print("Enter url to visit:")
for i in range(NonfVisits):
    url=input("URL:")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url
    #display current page
print(f"Current page: {current_page}")  
# go back
while input("Do you want to go back? (yes/no):").lower() == "yes" :
    if not forward_history.empty() :
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")
            