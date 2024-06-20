from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["apple"] = 5
ordered_dict["banana"] = 2
ordered_dict["orange"] = 8

print(ordered_dict)  # OrderedDict({'apple': 5, 'banana': 2, 'orange': 8})

ordered_dict.pop("banana")
print(ordered_dict)  # OrderedDict({'apple': 5, 'orange': 8})

ordered_dict["banana"] = 2
print(ordered_dict)  # OrderedDict({'apple': 5, 'orange': 8, 'banana': 2})


print(""" ============ Сравнение с обычным словарём ============ """)

usual_dict = {}
usual_dict["apple"] = 5
usual_dict["banana"] = 2
usual_dict["orange"] = 8

print(usual_dict)  # {'apple': 5, 'banana': 2, 'orange': 8}

usual_dict.pop("banana")
print(usual_dict)  # {'apple': 5, 'orange': 8}

usual_dict["banana"] = 2
print(usual_dict)  # {'apple': 5, 'orange': 8, 'banana': 2}

