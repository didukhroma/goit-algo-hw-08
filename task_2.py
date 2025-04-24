import heapq
def merge_k_lists(lists):
    merged_list = []
    for list in lists:
        for value in list:
            heapq.heappush(merged_list, value)
            
    return [heapq.heappop(merged_list) for _ in range(len(merged_list))]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)