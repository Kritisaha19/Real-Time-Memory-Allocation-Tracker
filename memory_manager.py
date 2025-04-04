class MemoryManager:
    def __init__(self, total_pages=256, page_size=4):
        self.total_pages = total_pages
        self.page_size = page_size
        self.pages = [0] * total_pages  # 0 = free, 1 = allocated
        self.page_table = {}  # Maps process ID to allocated pages
        self.segment_table = {}  # Maps process ID to (base, limit) segments

    def allocate_paging(self, process_id, num_pages):
        """Allocates pages for a process"""
        allocated_pages = []
        for i in range(len(self.pages) - num_pages + 1):
            if all(p == 0 for p in self.pages[i:i+num_pages]):
                for j in range(num_pages):
                    self.pages[i+j] = 1
                self.page_table[process_id] = list(range(i, i+num_pages))
                return i  # Return start index
        return -1  # No space available

    def allocate_segmentation(self, process_id, size):
        """Allocates memory for a process using segmentation"""
        for i in range(len(self.pages) - size + 1):
            if all(p == 0 for p in self.pages[i:i+size]):
                self.segment_table[process_id] = (i, size)
                for j in range(size):
                    self.pages[i+j] = 1
                return i  # Return base address
        return -1  # No space available

    def deallocate(self, process_id):
        """Frees memory allocated to a process"""
        if process_id in self.page_table:
            for page in self.page_table.pop(process_id):
                self.pages[page] = 0
        elif process_id in self.segment_table:
            base, size = self.segment_table.pop(process_id)
            for i in range(size):
                self.pages[base + i] = 0
