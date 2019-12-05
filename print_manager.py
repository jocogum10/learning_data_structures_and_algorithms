from collections import deque
class PrintManager:
    def __init__(self):
        self.queue = deque([])
        
    def queue_print_job(self, document):
        self.queue.append(document)
        
    def run(self):
        while self.queue != deque([]):
            print(self.queue.popleft())
            
if __name__ == '__main__':
    print_manager = PrintManager()
    print_manager.queue_print_job("First Document")
    print_manager.queue_print_job("Second Document")
    print_manager.queue_print_job("Third Document")
    print_manager.run()