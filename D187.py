class Rectangle:
    def __init__(self, top_left, dimensions) -> None:
        self.top_left = top_left
        self.dimensions = dimensions
        self.bottom_right = (top_left[0]+dimensions[0], top_left[1]-dimensions[1])
        self.bottom_left = (top_left[0], self.bottom_right[1])
        self.top_right = (self.bottom_right[0], top_left[1])

    def is_overlapping(self, rect_2):
        if self.bottom_left <= rect_2.bottom_left and rect_2.bottom_left < self.top_right:
            return True
        if self.bottom_left < rect_2.top_right and rect_2.top_right <= self.top_right:
            return True
        return False

rect_list = [Rectangle((1, 4), (3, 3)),  Rectangle((-1, 3), (2, 1)),  Rectangle((0, 5), (4, 3))]

for rect in rect_list:  
    for rect2 in rect_list:
        print(rect.is_overlapping(rect2) or rect2.is_overlapping(rect))