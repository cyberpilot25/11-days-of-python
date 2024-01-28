#learning decorators
def invoice_decorator(func):
    def wrap(num):
        print("***")
        print(f"INVOICE #{num}")
        print("***")
        print("END OF PAGE")
    return wrap

@invoice_decorator
def invoice(num):
    print("INVOICE #" + num)

invoice(input())
