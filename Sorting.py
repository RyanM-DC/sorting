def fillList(f_inp):
    while True:
        # loop that keeps program running until user chooses to exit
        value = input("Input a number into the unsorted list (type exit to stop)")
        if value.lower() == 'exit':
            #if user types exit the program stops asking for inputs
            break
        try:
            #checks if the value entered is a number
            f_inp.append(int(value))
        except:
            print("Invalid input")


def bubbleSort(b_inp):
    bubble_list = b_inp
    sorted_check = 0
    sort_counter = 0
    temp_val = 0
    while not sorted_check:
        sorted_check = 1
        sort_counter = 0
        while sort_counter < len(b_inp)-1:
            if bubble_list[sort_counter] > bubble_list[sort_counter + 1]:
                sorted_check = 0
                temp_val = bubble_list[sort_counter]
                bubble_list[sort_counter] = bubble_list[sort_counter + 1]
                bubble_list[sort_counter + 1] = temp_val
            sort_counter+=1

    return(bubble_list)


def mergeSort(m_inp):
    sorted = []
    #new list to hold values when sorted
    if len(inp) < 2:
        return(m_inp)
        #the recursion stopping case
    else:
        lowermid = mergeSort(inp[:int(len(m_inp) / 2)])
        uppermid = mergeSort(inp[int(len(m_inp) / 2):])
        #recursively splits the values into halves
        while (len(lowermid) > 0) or (len(uppermid) > 0):
            if len(lowermid) > 0 and len(uppermid) > 0:
                # if both sections are greater than 0 in length
                if lowermid[0] > uppermid[0]:
                    sorted.append(uppermid[0])
                    uppermid.pop(0)
                else:
                    sorted.append(lowermid[0])
                    lowermid.pop(0)
                # sorts all the values within the split sections
            elif len(uppermid) > 0:
                # if both the lower section only is greater than 0 in length
                for upval in uppermid:
                    sorted.append(upval)
                    uppermid.pop(0)
            else:
                # if both the upper section only is greater than 0 in length
                for lowval in lowermid:
                    sorted.append(lowval)
                    lowermid.pop(0)
        return(sorted)
        #returns the sorted list


def selectionSort(s_inp):
    sort_counter = 0
    selectionList = s_inp
    while sort_counter < len(selectionList):
        minimum = min(selectionList[sort_counter:])
        minimumIndex = selectionList[sort_counter:].index(minimum)
        selectionList[sort_counter + minimumIndex] = selectionList[sort_counter]
        selectionList[sort_counter] = minimum
        sort_counter += 1
    return(selectionList)


while True:
    unsorted = []
    fillList(unsorted)
    sort_choice = str(input("Choose a sorting method:\nBubble\nMerge\nSelection\nExit\nChoice: "))
    if sort_choice.lower() == "bubble":
        print(bubbleSort(unsorted))
    elif sort_choice.lower() == "merge":
        print(mergeSort(unsorted))
    elif sort_choice.lower() == "selection":
        print(selectionSort(unsorted))
    elif sort_choice.lower() == "exit":
        break
    else:
        print("Invalid Input")
