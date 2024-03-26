# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Time-O(n+l) Space-O(n) Recursive Flattened List
"""
class NestedIterator:
    def flattenList(self, myList: [NestedInteger]) -> None:
        for element in myList:
            if element.isInteger():
                self.pureList.append(element.getInteger())
            else:
                self.flattenList(element.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.pureList = []
        self.flattenList(nestedList)
        self.length = len(self.pureList)
        self.index = 0
    
    def next(self) -> int:
        value = self.pureList[self.index]
        self.index += 1
        return value
    
    def hasNext(self) -> bool:
        return self.index < self.length
"""


# Time-O(n+l) Space-O(n) Stack Iterator
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):  # type: ignore
        self.stack = [[nestedList, 0]]
        self.integer = None

    def next(self) -> int:
        return self.integer

    def hasNext(self) -> bool:
        while self.stack:  # Keep on iteratng till you find an integer
            nestedList, index = self.stack[-1]
            if index == len(nestedList):
                self.stack.pop()  # Pop when index gets out of bounds in the current nestedList
            else:
                nestedInteger = nestedList[index]
                self.stack[-1][
                    1
                ] += (
                    1  # Update (NOT pop) index to explore futher in the same nestedList
                )

                if nestedInteger.isInteger():
                    self.integer = nestedInteger.getInteger()
                    return True  # Set Integer and return True for next() to fetch
                else:
                    self.stack.append(
                        [nestedInteger.getList(), 0]
                    )  # Push new list to traverse

        return False  # Return if no integer exist


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
