# write dec_to_bin and implement user-selected mode via input

def get_number():
    number_string = input("Input a binary number: ").strip()
    return number_string

def convert():
    binary_temp = get_number()
    temp_bin = []
    
    for i in range(0,len(binary_temp)):
        temp_bin.append(binary_temp[i])

    temp_dec = []
    
    n = len(temp_bin) - 1
    
    for m in range(0, len(temp_bin)):
        if n >= 0:
            temp_dec.append(int(temp_bin[m])*(2 ** n))
        else:
            return
        n = n-1
        
    result = 0

    for num in temp_dec:
        result = result + num

    return result

def main():
    result = convert()
    print(f"The number converted to decimal is {result}\n")

if __name__ == "__main__":
    main()