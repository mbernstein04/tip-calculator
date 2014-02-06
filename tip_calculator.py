from optparse import OptionParser 

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="What the base price of your meal is")

parser.add_option("-t", "--tax", dest="tax", help="What the tax on the meal is")

parser.add_option("-x", "--tip", dest="tip", help="What percent tip that should be left on the meal",
	default=".2")

(options, args) = parser.parse_args()

if not (options.meal and options.tax):
	parser.error("You need to supply an argument for foth -m and -t")

meal = format(options.meal)
tax = format(options.tax)
tip = format(options.tip)

meal_converted = float(meal)
tax_converted = float(tax)
tip_converted = float(tip)

tax_value = meal_converted * tax_converted
meal_with_tax = tax_value + meal_converted
tip_value = meal_converted * tip_converted
total = meal_with_tax + tip_value


print "The base cost of the meal is %r" % ("{:.2f}".format(meal_converted))
print "The dollar value of tax on the meal is %r" % ("{:.2f}".format(tax_value))
print "The dollar value of the tip you'll need to pay is %r" % ("{:.2f}".format(tip_value))
print "The grand total for the meal is %r" % ("{:.2f}".format(total))