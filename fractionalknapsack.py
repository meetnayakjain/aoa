class Item:
    def __init__(self,id,profit,weight):
        self.id = id
        self.profit = profit
        self.weight = weight

temp = []

def fractionalKnapsack(W,arr):

    arr.sort(key=lambda x:(x.profit/x.weight),reverse=True)

    profit = 0.0

    for item in arr:
        if item.weight <= W:
            W-= item.weight
            temp.append(item.id)
            profit += item.profit


        else:
            profit += item.profit/item.weight * W
            temp.append(item.id)
            break

    return profit

if __name__ == "__main__":
    W = 30
    arr=[Item(1,20,20),Item(2,10,10),Item(3,30,25)]

    print(f'The max profit is {fractionalKnapsack(W,arr)}')
    print('The processes included are',temp,end=" ")