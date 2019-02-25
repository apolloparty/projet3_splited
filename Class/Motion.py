class Motion:
    """limit position possible, check if the next position is valid, update maps variable"""
    def check_direction(self, move, mcy, mcx, maps, collect):
        """limit position possible, check if the next position is valid, update maps variable"""
        if move == "z":
            if mcy == 0:
                pass
            elif (
                    maps[mcy - 1][mcx] == "X" or
                    maps[mcy - 1][mcx] == "Y" or
                    maps[mcy - 1][mcx] == "Z"
                ):
                maps[mcy][mcx] = " "
                maps[mcy - 1][mcx] = "M"
            elif maps[mcy - 1][mcx] == " ":
                maps[mcy][mcx] = " "
                maps[mcy - 1][mcx] = "M"
        if move == "s":
            if mcy == 14:
                pass
            elif (
                    maps[mcy + 1][mcx] == "X" or
                    maps[mcy + 1][mcx] == "Y" or
                    maps[mcy + 1][mcx] == "Z"
                ):
                maps[mcy][mcx] = " "
                maps[mcy + 1][mcx] = "M"
            elif maps[mcy + 1][mcx] == " ":
                maps[mcy][mcx] = " "
                maps[mcy + 1][mcx] = "M"
        if move == "q":
            if mcx == 0:
                pass
            elif (
                    maps[mcy][mcx - 1] == "X" or
                    maps[mcy][mcx - 1] == "Y" or
                    maps[mcy][mcx - 1] == "Z"
                ):
                maps[mcy][mcx] = " "
                maps[mcy][mcx - 1] = "M"
            elif maps[mcy][mcx - 1] == "T":
                if collect == [1, 1, 1]:
                    maps[mcy][mcx] = " "
                    maps[mcy][mcx - 1] = "M"
            elif maps[mcy][mcx - 1] == " " and maps[mcy][mcx - 1] != "T":
                maps[mcy][mcx] = " "
                maps[mcy][mcx - 1] = "M"
        if move == "d":
            if mcx == 14:
                pass
            elif (
                    maps[mcy][mcx + 1] == "X" or
                    maps[mcy][mcx + 1] == "Y" or
                    maps[mcy][mcx + 1] == "Z"
                ):
                maps[mcy][mcx] = " "
                maps[mcy][mcx + 1] = "M"
            elif maps[mcy][mcx + 1] == " ":
                maps[mcy][mcx] = " "
                maps[mcy][mcx + 1] = "M"
        for line in maps:
            print(line)
