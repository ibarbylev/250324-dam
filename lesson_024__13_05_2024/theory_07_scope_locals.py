count = 0


def outer():
    count_outer = 1
    print("inside the outer function", locals().keys())

    def inner():
        count_inner = 2
        print("inside the inner function", locals().keys())

    inner()


outer()
print("module", locals().keys())
