'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''    
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
inputFrom = input(str("Input from member: "))
inputTo = input(str("Input to member: "))
def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    fromFollow = social_graph[from_member]['following']
    toFollow = social_graph[to_member]['following']
    if from_member in toFollow and to_member in fromFollow:
        relationship = 'friends'
    elif from_member in toFollow:
        relationship = 'followed by'
    elif to_member in fromFollow:
        relationship = 'follower'
    else:
        relationship = 'no relationship'
    return(str(relationship))
relationship_status(inputFrom, inputTo, social_graph)

board = [
['X','X','O'],
['','O','X'],
['X','X','O'],
]
import numpy as np
def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.    
    SIZE = len(board)

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == "X":
                board[i][j] = 1
            elif board[i][j] == "O":
                board[i][j] = -1
            else:
                board[i][j] = 0


    board = np.array(board)
    col_sums = np.sum(board, axis=1)

    #Horizontal check
    for col_sum in col_sums:
        if col_sum == SIZE:
            return "X"
        elif col_sum == -SIZE:
            return "O"

    #Vertical check
    row_sums = np.sum(board, axis=0)
    for row_sum in row_sums:
        if row_sum == SIZE:
            return "X"
        elif row_sum == -SIZE:
            return "O"

    #Diagonal check
    primary_diag_sum = 0 #going down to the right diagonal
    for i in range(SIZE):
        primary_diag_sum += board[i][i]
    if primary_diag_sum == SIZE:
        return "X"
    elif primary_diag_sum == -SIZE:
        return "O"

    #Inverse diagonal check
    secondary_diag_sum = 0
    for i in range(SIZE):
         secondary_diag_sum += board[i, (SIZE - 1) - i]
    if secondary_diag_sum == SIZE:
        return "X"
    elif secondary_diag_sum == -SIZE:
        return "O"
    else:
        return "No Winner"
tic_tac_toe(board)
    
inputFirst = input(str("Stop where shuttle leaves: "))
inputSecond = input(str("Stop where shuttle arrives: "))
route_map = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     },
     
     ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer
    parameters = (first_stop, second_stop)
    travelTime = 0

    for i in route_map:
        if parameters == i:
            travelTime += route_map[i]['travel_time_mins']
            break

    return(travelTime)
eta(inputFirst, inputSecond, route_map)