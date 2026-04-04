def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    
    mp = [
        " _     _  _     _  _  _  _  _ ",
        "| |  | _| _||_||_ |_   ||_||_|",
        "|_|  ||_  _|  | _||_|  ||_| _|",
        "                              "]
    
    ans = ""
    
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[0]), 3):
            num = -1
            for mapnum in range(0, 10):
                flag = True
                for ii in range(4):
                    for jj in range(3):
                        if (input_grid[i + ii][j + jj] != mp[ii][mapnum * 3 + jj]):
                            flag = False
                if (flag):
                    num = mapnum
                    break
            if num == -1:
                ans += '?'
            else:
                ans += str(num)

        if i != len(input_grid) - 4:
            ans += ','
    return ans