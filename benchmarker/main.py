from benchmarker.benchmarker import Benchmarker

bencher = Benchmarker()

if __name__ == '__main__':
    bencher.runOptimzed(5)
    bencher.runUnoptimzed(5)

    bencher.saveResults()
    bencher.graphResults()
