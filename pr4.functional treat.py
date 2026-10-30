
data_summary = {"last_step": "Started"}


def get_statistic(data):
    total_ele = len(data)
    min_val = min(data)
    max_val = max(data)
    sum_val = sum(data)
    avg_val = sum_val / total_ele
    return total_ele, min_val, max_val,sum_val, avg_val

def display_summary(data):
    global data_summary
    tot, mn, mx, sm, avg = get_statistic(data)
    print(f"\nTotal: {tot} | Min: {mn} | Max: {mx} | Sum: {sm} | Avg: {avg:.2f}")
    data_summary["last_step"] = "Summary Displayed"


#(*args, **kwargs):
    #print("Args:", args)
    #("Kwargs:", kwargs)ef pri


def cal_factorial(n):
    if n <= 1:
        return 1
    return n * cal_factorial(n - 1)


def filter_data(data, threshold):
    return list(filter(lambda a: a >= threshold, data))


def sort_data(data, choice):
   
    if choice == 1:
        data.sort()
        print("Ascending:",data )
    else:
        print("Descending:", sorted(data, reverse=True))


def main():
    user_data = []
    
    while True:
        print("\n--- MENU ---")
        print("1. Input Data")
        print("2. Display Summary")
        print("3. Factorial ")
        print("4. Filter ")
        print("5. Sort Data")
        print("6. Display Dataset Statistics")
        print("7. Exit")
        
        ch = input("Enter choice: ")
        
        if ch == '1':
            user_data = [int(a) for a in input("Enter numbers : ").split()]
            print("Data saved!")
            
        elif ch == '2':
            if user_data: 
                display_summary(user_data)
                print_info(user_data, type="1D List")
            else: 
                print("Enter data first!")
                
        elif ch == '3':
            n = int(input("Enter number for factorial: "))
            print("Factorial:", cal_factorial(n))
            
        elif ch == '4':
            if user_data:
                t = int(input("Enter threshold: "))
                print("Filtered:", filter_data(user_data, t))
            else: 
                print("Enter data first!")
                
        elif ch == '5':
            if user_data:
                sc = int(input("1. Ascending 2. Descending: "))
                sort_data(user_data, sc)
            else: 
                print("Enter data first!")
                
        elif ch == '6':
            if user_data:
                print("Dataset Statistics:")
                print(f"Min: {min(user_data)}")
                print(f"Max: {max(user_data)}")
                print(f"Sum : {sum(user_data)}")
                avg = sum(user_data) / len(user_data)
                print(f"Ave: {avg:.2f}")
            else:
                print("Enter data first!")

        elif ch == '7':
              print("Thank you. Goodbye!")
              break
            
           

if __name__ == "__main__":
    main()