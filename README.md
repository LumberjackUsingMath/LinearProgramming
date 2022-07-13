# Resource Scheduling of Bakery Zurich 


### Set-up

Given an amount of baker and packer days, the bakery Zurich wants to know how much to produce of product ``x_1,...,x_n`` to optimize the profit.

### How the inputs work: 
The file [inputs](inputs.yaml) expects a dictionary "parameters" with the keys:
* ``model_name``
* ``packer_days_total``
* ``baker_days_total``


and another dictionary products which is a list of dictionaries with the keys:

* ``name`` 
* ``lb``  lower bound of the number of units to produce
* ``ub`` upper bound of the number of units to produce
* ``cat``  category of units (whether Integer or continuous)
* ``price``  price per unit
* ``baker_days``  days a baker is needed to produce 1 unit
* ``packer_days``  days a packer is needed to produce 1 unit



### How to run the program
In the end, execute the [main file](main.py). The result will be printed to the console 
