class Searcher:


    def simple_search(self, searched, elements):
        for i in range(len(elements)):
            if elements[i] == searched:
                return i
        return -1

    def binary_search(self, searched, elements):
        start_position = 0
        end_position = len(elements)-1
        while end_position >= start_position:
            search_position = (start_position+end_position)//2 
            if elements[search_position] == searched:
                return search_position
            else:
                if elements[search_position] > searched:
                    end_position = search_position - 1
                else:
                    start_position = search_position + 1
        return -1
        
