from collections import deque

def person_is_seller(name):
    #This function checks whether the person's name ends with the letter m. If it does, they're a mango seller. Kind of a silly way to do it, but it'll do for this example.
    return name[-1]== 'm'


def search(name):
        #Creates a new Queue
    search_queue = deque()
    search_queue += graph[name]
        #This array is how you keep track of which people you've searched before
    searched = []

    #While the queue isn't empty
    while search_queue:
        #grabs the first person off the queue
        person = search_queue.popleft()
        if not person in searched:
            #checks wheter the person is a mango seller
            if person_is_seller(person):
                print ( person + " is a mango seller!")
                return True
            else:
                #No, they aren't. add all of this person friends to the search queue
                search_queue += graph[person]
                searched.append(person)
    return False

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["throm"]= []
graph["johnny"]= []
graph["claire"] = ["thom", "jonny"]


search("you")
