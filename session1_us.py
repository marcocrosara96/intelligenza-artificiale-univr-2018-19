def tree_search(env, fringe):
    """
    Tree search
    
    Args:
        environment: OpenAI Gym environment
        fringe: instance of Fringe data structure
        
    Returns:
        (path, stats): solution as a path and stats.
        The stats are a tuple of (expc, maxnodes): number of explored states, max nodes in memory
    """
    
    #VI E' UNA SORTA DI INNER [[[POSITION] STATE] NODE]
    
    start = env.startstate
    goal = env.goalstate
    explored_states = 0
    
    fringe.add(FringeNode(start))
    
    while not fringe.is_empty():
        currentNode = fringe.remove()
        explored_states += 1
        if(currentNode.state == goal): #?? è giusto fare il controllo in questa posizione? 
                                        ## o devo farlo quando faccio lo scan dei nextNodes di un nodo?
            return build_path(currentNode), (explored_states, len(fringe))
        for action in range(env.action_space.n):
            nextNode = FringeNode(env.sample(currentNode.state, action), currentNode)
            if(nextNode.state != currentNode.state):
                fringe.add(nextNode)
    
    return None, (explored_states, len(fringe))

"""
    explored_node=0;
    if environment.startstate == environment.goalstate :
        return [FringeNode(environment.startstate)],(1,1)
    fringe.add(FringeNode(environment.startstate))
    while True :
        if fringe.is_empty():
            return None,(explored_node,len(fringe))
        else:
            node=fringe.remove()
            explored_node=explored_node+1
            for action in range (environment.action_space.n):
                child = FringeNode(environment.sample(node.state,action),node)
                if node.state == environment.goalstate :
                    return build_path(node), (explored_node,len(fringe)+1)
                fringe.add(child)
"""

####### TEST ########
#environment = gym.make("SmallMaze-v0")
#tree_search(environment, QueueFringe());
