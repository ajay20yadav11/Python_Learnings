def count_uniform_numbers(start,end):
    
    curr_len = len( str(start) )
    curr_min,curr_max = get_min(start),10
    if curr_len == len(str(end)):
        curr_max = get_max(end)
    ans = 0
    
    while curr_len <= len(str(end)):
        
        ans += (curr_max-curr_min-1)
        
        curr_len += 1
        curr_min,curr_max = 0,10
        if curr_len == len(str(end)):
            curr_max = get_max(end)
    
    return ans

def get_min(num):
    
    str_num = str(num)
    start = int(str_num[0])
    for s in str_num[1:]:
        if int(s) > start:
            return start
    
    return start-1

def get_max(num):
    
    str_num = str(num)
    start = int(str_num[0])
    for s in str_num[1:]:
        if int(s) < start:
            return start
    
    return start+1

count_uniform_numbers(75,300)