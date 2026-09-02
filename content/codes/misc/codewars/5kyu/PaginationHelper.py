# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.ylist = []
    
    def item_count(self):
        return len(self.collection)

    def page_count(self):
        for i in range(0, len(self.collection), self.items_per_page):
            self.ylist.append(self.collection[i:i+self.items_per_page])
        return len(self.ylist)

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= len(self.ylist):
            return -1
        return len(self.ylist[page_index])

    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        return item_index // self.items_per_page


xlist = [chr(i) for i in range(65, 123)]
# print(xlist)
x = PaginationHelper(xlist, 5)


print(x.page_item_count(4))