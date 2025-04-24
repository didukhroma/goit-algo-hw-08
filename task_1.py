import heapq

def cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        total_cost += cable1 + cable2
        heapq.heappush(cables, cable1 + cable2)
    return total_cost

cables = [1,3,5,4,6]
print(cost_to_connect_cables(cables))