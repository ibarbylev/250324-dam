count = 0


def outer():
    count_outer = 1

    def inner():
        count_inner = 2
        print("inside the inner function", locals().keys())

    inner()
    print("inside the outer function", locals().keys())


outer()
print("module", locals().keys())
