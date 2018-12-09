import os
path = os.path.join("../data/task1.csv")

def make_list(file):

    titles = file.readline().replace("\n","").split(", ")

    file = file.read().splitlines()
    result = []

    for line in file:
        result.append(dict(zip(titles, line.split(","))))
    return result

def Add_person(person,dataset):
    if person['client'] in dataset:
        if person['date'] in dataset[person['client']]:
            dataset[person['client']][person['date']].update({person['product']:[person['quantity'],person['price']]})
        else:
            dataset[person['client']].update({
                person['date']:{
                    person['product']:[person['quantity'],person['price']]
                }
            })
    else:
        dataset.update({
            person['client']:{
                person['date']:{
                    person['product']:[person['quantity'],person['price']]
                }
            }
        })
'''
products = {
    product1:{
        price={data1:price1,data2:price2},
        buys=int,
        buyers=int
        }
}
'''
'''
    dataset = {
        client:{
            data:{
                product:[quantiti,price]
            }
        }
    }
'''
def Add_product(product,dataset):
    # TODO
    pass

def Make_products_set(dataset):
    products_set = {}
    dataset = set(dataset)
    for person in dataset.values():
        for date in dataset[person].values():
            Add_person(dataset[person][date],products_set)




def Find_popular_meal(dataset):
    # TODO
    pass


if __name__ == '__main__':
    with open(path, "r") as file:
        dataset = {}
        data = make_list(file)
        for person in data:
            Add_person(person,dataset)





