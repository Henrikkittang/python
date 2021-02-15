import converter

maze = [ [0] * 1000 for _ in range(1000)]
def main():
    converter.findPath(maze, [0, 0], [998, 998])

main()