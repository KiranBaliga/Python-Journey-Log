#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to join given strings
def combo_string(a, b):
    # Determine the shorter and longer strings
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    
    # Return the concatenated string in the format shorter+longer+shorter
    return shorter + longer + shorter

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    # 
    testcases = int(input())
    
    while(testcases > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        
        testcases -= 1
        
        print (combo_string(string1, string2))

if __name__ == '__main__':
    main()
# } Driver Code Ends