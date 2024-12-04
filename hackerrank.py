if __name__ == '__main__':
    n = int(input()) 
    arr = map(int, input().split())  
    scores = list(arr) 
    unique_scores = list(set(scores)) 
    unique_scores.sort(reverse=True) 
    
    if len(unique_scores) > 1:
        print(unique_scores[1]) 
    else:
        print("No runner-up score available.") 
