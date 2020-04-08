# This is the long way on how to connect a import from a different folder
# we are prefixing it with the name of the package
# ------------------------------
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
# -------------------------------

# Here is another way
from ecommerce import shipping

shipping.calc_shipping()