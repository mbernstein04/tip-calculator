import sys

meal_converted = float(sys.argv[1])
tax_converted = float(sys.argv[2])
tip_converted = float(sys.argv[3])

tax_value = meal_converted * tax_converted
meal_with_tax = tax_value + meal_converted
tip_value = meal_converted * tip_converted
total = meal_with_tax + tip_value


print "The base cost of the meal is %r" % ("{:.2f}".format(meal_converted))
print "The dollar value of tax on the meal is %r" % ("{:.2f}".format(tax_value))
print "The dollar value of the tip you'll need to pay is %r" % ("{:.2f}".format(tip_value))
print "The grand total for the meal is %r" % ("{:.2f}".format(total))