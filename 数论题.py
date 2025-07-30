count = 0
for x in range(0,676):
    for y in range(0,506):
        for z in range(0,2020):
            if 3*x + 4*y + 12*z == 2020:
                count+=1
                print(x, y, z)
            elif 3*x + 4*y + 12*z >= 2020:
                break

print(count)