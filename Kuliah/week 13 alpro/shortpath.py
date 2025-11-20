print("Mini Map - Simple Route Finder")

# 1. Get Inputs
# We wrap the input in int() to make sure we can do math with it
ab = int(input("Distance A to B: "))
ac = int(input("Distance A to C: "))
ad = int(input("Distance A to D: "))
bc = int(input("Distance B to C: "))
bd = int(input("Distance B to D: "))
cd = int(input("Distance C to D: "))

print("-" * 30)
start_point = input("Start (A, B, C, D): ").upper()
end_point = input("End   (A, B, C, D): ").upper()

# 2. Create the Map
# A simple dictionary to hold the distances
graph = {
    'A': {'B': ab, 'C': ac, 'D': ad},
    'B': {'A': ab, 'C': bc, 'D': bd},
    'C': {'A': ac, 'B': bc, 'D': cd},
    'D': {'A': ad, 'B': bd, 'C': cd}
}

# 3. Basic Error Checking
if start_point == end_point:
    print("Error: You are already at the destination!")
elif start_point not in graph or end_point not in graph:
    print("Error: Invalid points entered.")
else:
    # 3.1 Find ALL Possible Routes First
    def find_all_routes(graph, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        all_routes = []
        for neighbor in graph[start]:
            if neighbor not in path:  # Avoid loops
                new_routes = find_all_routes(graph, neighbor, end, path)
                for route in new_routes:
                    all_routes.append(route)
        
        return all_routes
    
    # Calculate distance for a complete route
    def calculate_route_distance(graph, route):
        total = 0
        for i in range(len(route) - 1):
            total = total + graph[route[i]][route[i + 1]]
        return total
    
    # Get all possible routes
    all_possible_routes = find_all_routes(graph, start_point, end_point)
    
    # Calculate distances for all routes
    routes_with_distances = []
    for route in all_possible_routes:
        distance = calculate_route_distance(graph, route)
        routes_with_distances.append((route, distance))
    
    # Sort by distance (shortest first)
    routes_with_distances.sort(key=lambda x: x[1])
    
    # Display all possible routes
    print("\n" + "=" * 50)
    print("ALL POSSIBLE ROUTES:")
    print("=" * 50)
    for i, (route, dist) in enumerate(routes_with_distances, 1):
        route_str = " → ".join(route)
        print(f"\n{i}. {route_str}")
        print(f"   Distance: {dist}")
        if len(route) > 2:
            print("   Breakdown:")
            for j in range(len(route) - 1):
                segment_dist = graph[route[j]][route[j + 1]]
                print(f"     {route[j]} → {route[j + 1]}: {segment_dist}")
    
    # 4. The Loop (Greedy Logic)
    current_location = start_point
    path_taken = [current_location] # List to store our history
    total_distance = 0
    
    print("\n" + "=" * 50)
    print("GREEDY ALGORITHM ROUTE:")
    print("=" * 50)
    print("\nStarting Navigation...")
    
    # Keep moving until we are at the end point
    while current_location != end_point:
        # Get neighbors of where we are now
        neighbors = graph[current_location]
        
        # Logic:
        # 1. If we can go straight to the end, do it.
        # 2. If not, find the closest neighbor we haven't visited yet.
        
        if end_point in neighbors:
            # Go directly to destination
            distance_to_move = neighbors[end_point]
            total_distance = total_distance + distance_to_move
            current_location = end_point
            path_taken.append(end_point)
        else:
            # Find closest neighbor
            shortest_dist = 999999 # Set a high number to start
            next_move = ""
            
            for neighbor_name in neighbors:
                dist = neighbors[neighbor_name]
                
                # Check if this is the shortest AND if we haven't been there
                if dist < shortest_dist and neighbor_name not in path_taken:
                    shortest_dist = dist
                    next_move = neighbor_name
            
            # If we found a valid move, make it
            if next_move != "":
                total_distance = total_distance + shortest_dist
                current_location = next_move
                path_taken.append(next_move)
            else:
                print("Stuck! No path found.")
                break

    # 5. Print Results
    print("\nRoute Found:", " → ".join(path_taken))
    print("Total Distance:", total_distance)
    print("=" * 50)