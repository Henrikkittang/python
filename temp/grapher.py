import matplotlib.pyplot as plt


def grapher():
    x1 = []
    y1 = []

    with open('temp/time_data.txt', 'r') as file:
        y1 = file.read().split('\n')
        x1 = list(range(1, len(y1)+1))
        file.close()

    plt.plot(x1, y1, label='Time graph')
    plt.xlabel('Idx')
    plt.ylabel('Time')

    plt.title('Tacobaugett')
    plt.legend()
    plt.show()


grapher()
