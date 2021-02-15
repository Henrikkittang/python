import matplotlib.pyplot as plt
from statistics import median
import json

class Grapher(object):
    def __init__(self):
        self.resultsOptimized = {}
        self.resultsUnoptimized = {}

    def graphResults(self):
        self.readResults()
        self.computeResults()

        fig, (ax_av, ax_me) = plt.subplots(1, 2)
        fig.suptitle('Benchmark')

        #fill average
        ax_av.bar(0.8, self.resultsOptimized['average'], width=0.2, label='optimized file')
        ax_av.bar(1.2, self.resultsUnoptimized['average'], width=0.2, label='unoptimized file')
        ax_av.set_title('Average')

        #fill median
        ax_me.bar(0.8, self.resultsOptimized['median'], width=0.2, label='optimized file')
        ax_me.bar(1.2, self.resultsUnoptimized['median'], width=0.2, label='unoptimized file')
        ax_me.set_title('Median')

        ax_me.legend()
        ax_av.legend()
        plt.show()


    def readResults(self):
        with open('benchmarker/results.json') as f:
            results = json.load(f)
            self.resultsOptimized = results['optmized']
            self.resultsUnoptimized = results['unoptmized']
            f.close()

    def computeResults(self):
        self.resultsOptimized['average'] = sum(self.resultsOptimized['iterations']) / len(self.resultsOptimized['iterations'])
        self.resultsUnoptimized['average'] = sum(self.resultsUnoptimized['iterations']) / len(self.resultsUnoptimized['iterations'])

        self.resultsOptimized['median'] = median(self.resultsOptimized['iterations'])  
        self.resultsUnoptimized['median'] = median(self.resultsUnoptimized['iterations'])  

        
            

       




