import os

class Input:
    def __init__(self):
        self.List1 = []
        self.List2 = []

    def add_values(self, val1: int, val2: int):
        self.List1.append(val1)
        self.List2.append(val2)

class Day1:

    def parse_file(self, file_path: str):
        """
        Parses the input file to fetch the two lists in the problem
        File will have two values separated by a space for each line
        """
        result = Input()
        try:
            with open(file_path, "r") as fs:
                while ln := fs.readline():
                    ln = ln.strip()
                    vals = ln.split(" ")
                    vals[:] = [val for val in vals if val != ""]
                    if len(vals) != 2:
                        print(f"Unable to parse the given file, expected two values but found: {len(vals)}")
                        print(f"Values: {vals}")
                        return result
                    result.add_values(int(vals[0]), int(vals[1]))
        except Exception as e:
            print(e)
        
        return result

    def part1(self, result: Input):

        sorted_1 = sorted(result.List1)
        sorted_2 = sorted(result.List2)
        runningTotal = 0

        # Assuming both lists would be of same length, as the negative scenario is not described
        for i in range(len(sorted_1)):
            diff = sorted_1[i] - sorted_2[i]
            runningTotal = runningTotal + (diff * (1 if diff >= 0 else  -1))
        
        return runningTotal
    

    def part2(self, result: Input):
        key_count = {}

        for i in range(len(result.List2)):
            key_count[result.List2[i]] = key_count.get(result.List2[i], 0) + 1
        
        
        runningTotal = 0

        # Assuming both lists would be of same length, as the negative scenario is not described
        for i in range(len(result.List1)):
            val = result.List1[i]
            repeat = key_count.get(val, 0)
            runningTotal = runningTotal + (val * repeat)
        
        return runningTotal
                

