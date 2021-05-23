def largest_product_in_grid(thread, num, limit, row):
    thread_str = str(thread)
    my_dict = {}
    count = 0
    count2 = num
    greatest = 0
    length = len(thread_str)
    line = int(length / num)
    print(line)

    for i in range(0, line):
        digits = thread_str[count:count2]
        my_dict[i + 1] = digits
        count += num
        count2 += num

    for i in my_dict:
        if i < line - limit + 1:
            multiple = int(my_dict[i]) * int(my_dict[i + 1]) * int(my_dict[i + 3]) * int(my_dict[i + 4])
            if multiple > greatest:
                greatest = multiple

        if i < line - (limit - 1) * (row + 1) + 1:
            multiple = int(my_dict[i]) * int(my_dict[i + 21]) * int(my_dict[i + 42]) * int(my_dict[i + 63])
            if multiple > greatest:
                greatest = multiple

        if i < line - (limit - 1) * row + 1:
            multiple = int(my_dict[i]) * int(my_dict[i + 20]) * int(my_dict[i + 40]) * int(my_dict[i + 60])
            if multiple > greatest:
                greatest = multiple

        if limit - 1 < i < line - (limit - 1) * (row - 1) + 1:
            multiple = int(my_dict[i]) * int(my_dict[i + 19]) * int(my_dict[i + 38]) * int(my_dict[i + 57])
            if multiple > greatest:
                greatest = multiple

    return greatest


print(largest_product_in_grid("08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748", 2, 4, 20))
