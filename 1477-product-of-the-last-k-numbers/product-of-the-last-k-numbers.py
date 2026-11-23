class ProductOfNumbers:
    def __init__(self):
        # Start with 1 as a base multiplier
        self.prefix =list([1])


    def add(self, num: int) -> None:
        if num == 0:
            # A zero wipes out all previous products, so reset the list
            self.prefix =list([1])

        else:
            # Store the running multiplied total
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches back to or past a 0, the product must be 0
        if k >= len(self.prefix):
            return 0
        # Instant division instead of a slow loop!
        return self.prefix[-1] // self.prefix[-1 - k]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)