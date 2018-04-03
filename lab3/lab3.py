# http://www.aup.ru/books/m157/4_3_3.htm

from math import sqrt

items_amount = 24000
monthly_storing_price = 0.1
batch_prod_price = 350
planned_days = 365

daily_supply_amount = items_amount / planned_days
daily_storing_price = monthly_storing_price * 12 / 365


def get_initial_batch_size():
    return sqrt(2 * daily_supply_amount * batch_prod_price / daily_storing_price)


def get_batch_size(n):
    return daily_supply_amount * items_amount / n


def get_mean_cost(batch_size):
    return (daily_supply_amount * batch_prod_price / batch_size) + (daily_storing_price * batch_size / 2)


def main():
    initial_batch_size = get_initial_batch_size()
    batch_size_upper = 0
    batch_size_lower = 0
    n = 1
    while not (batch_size_upper < initial_batch_size <= batch_size_lower):
        batch_size_lower = batch_size_upper
        batch_size_upper = get_batch_size(n)
        n += 1
    mean_cost_upper = get_mean_cost(batch_size_upper)
    mean_cost_lower = get_mean_cost(batch_size_lower)

    optimal_batch_size = batch_size_lower if mean_cost_lower < mean_cost_upper else batch_size_upper
    optimal_interval = planned_days / (items_amount / optimal_batch_size)

    print('Optimal batch size: {0}'.format(optimal_batch_size))
    print('Optimal interval: {0}'.format(optimal_interval))


if __name__ == '__main__':
    main()
