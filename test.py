import json


def dummy():
    data = {"name": "Alice", "age": 25, "city": "New York"}

    with open("videos.json", "r") as file:
        data = json.load(file)
        print(data)

def lambda_comprehension():
    print("hi")
    num_list = list(range(1, 11))
    print(num_list)
    even_odd_list = map(lambda x: "True" if x % 2 == 0 else "False", num_list)
    print(list(even_odd_list))

def aray_mod():
    named_list = [{"name":"Raksh"}, {"name":"Aashrith"}, {"name":"Naalla"}]
    copied_list = named_list[:]
    copied_list[0]["name"] = "Aashrith"
    copied_list[1]["name"] = "Rakseh"

    print(f"""
    named_list: {named_list}
    copied_list: {copied_list}
    """)

# lambda_comprehension()
if __name__ == "__main__":
    # dummy()
    # lambda_comprehension()
    aray_mod()