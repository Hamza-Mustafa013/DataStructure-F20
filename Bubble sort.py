def bubblesort(list):

    listed=len(list)
    isSorted=False
    while not isSorted:
        isSorted=True
        for eachvalue in range(0,listed-1):
            print(range(0,listed-1))
            # print(eachvalue)
            if list[eachvalue]>list[eachvalue+1]:
                isSorted=False
                temp=list[eachvalue]
                list[eachvalue]=list[eachvalue+1]
                list[eachvalue+1]=temp
    print(list)
listed=[6,2,5,4,3]
bubblesort(listed)

