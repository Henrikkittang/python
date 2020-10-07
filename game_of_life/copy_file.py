from random import randint

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def copy():
    
    file_name = "average/" + chars[randint(0, 25)] + chars[randint(0, 25)] + chars[randint(0, 25)] + chars[randint(0, 25)] + ".txt"

    print(file_name)

    with open("cells_data.txt", "r") as old_file:
        with open(file_name, "w") as new_file:
            for line in old_file:
                new_file.write(line)
                
            new_file.close()
        old_file.close()



    with open("average/files_name.txt", "a") as f:
        f.write(file_name + "\n")
        f.close()

