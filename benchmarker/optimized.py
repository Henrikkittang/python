import a_star


maze = [ [0] * 1000 for _ in range(1000)]
def main():
    a_star.find_path(maze, (0, 0), (998, 998), False)

main()