def convert_customer_list(customers):
    _results = []
    for customer in customers:
        _results.append(customer.to_dict())

    return _results
