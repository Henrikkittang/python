import time
import json

import benchmarker.grapher as grapher

import optimized
import unoptimized

class Benchmarker(object):
    def __init__(self):
        self.resultsOptimized = {}
        self.resultsUnoptimized = {}

    def saveResults(self):
        results = {
            'optmized': self.resultsOptimized,
            'unoptmized': self.resultsUnoptimized
        }

        with open('benchmarker/results.json', 'w') as f:
            json.dump(results, f)
            f.close()

    def graphResults(self):
        graph = grapher.Grapher()
        graph.graphResults()

    def runOptimzed(self, iterations):
        self.resultsOptimized = {
            'total': 0,
            'iterations': []
        }

        print('Running optimized...')
        totalStart = time.time()
        for _ in range(iterations):
            iterationStart = time.time()
            
            optimized.main()

            iterationEnd = time.time()
            self.resultsOptimized['iterations'].append(iterationEnd-iterationStart)
        totalEnd = time.time()
        print('Finnished running optimized')
        self.resultsOptimized['total'] = totalEnd-totalStart

    def runUnoptimzed(self, iterations):
        self.resultsUnoptimized = {
            'total': 0,
            'iterations': []
        }

        print('Running unoptimized')
        totalStart = time.time()
        for _ in range(iterations):
            iterationStart = time.time()
            
            unoptimized.main()

            iterationEnd = time.time()
            self.resultsUnoptimized['iterations'].append(iterationEnd-iterationStart)
        totalEnd = time.time()
        print('Finnished running unoptimized')
        self.resultsUnoptimized['total'] = totalEnd-totalStart
         
