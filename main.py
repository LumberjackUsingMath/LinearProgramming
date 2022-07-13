import pulp as pl
import yaml

if __name__ == "__main__":
    yaml_inputs = yaml.load(open("inputs.yaml", 'r'), Loader=yaml.FullLoader)
    parameters = yaml_inputs["parameters"]
    products   = yaml_inputs["products"]


    for product  in products:
        product["LpVariable"] = pl.LpVariable(name=product["name"], lowBound=product["lb"], upBound=product["ub"], cat=product["cat"], e=None)

    # Define model
    model = pl.LpProblem(name = parameters["model_name"], sense= pl.LpMaximize)
    # Define objective
    model += sum([product["price"] * product["LpVariable"] for product in products ])
    # Define constraints
    model += sum([product["packer_days"] * product["LpVariable"] for product in products ]) <= parameters["packer_days_total"]
    model += sum([product["baker_days"] * product["LpVariable"] for product in products ]) <= parameters["baker_days_total"]


    model.solve()

    for product in products:
        print(f"Produce {(product['LpVariable']).varValue} pieces of {product['name']}")