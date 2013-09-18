#!/usr/bin/python2

class Stock :
	"""
	A simple class representing a stock on a stock exchange.
	Fields: name
		symbol
		price
		low
		high
		volume
	"""

	def __init__(self, name, symbol, price = 0.0 ,
			low = 0.0, high = 0.0, volume = 0.0) :
		self.name = name
		self.symbol = symbol
		self.price = price
		self.low = low
		self.high = high
		self.volume = volume
	
	## Special method that compares two stocks symbols
	def __eq__(self,other) :
		return self.symbol == other.symbol
	
	def __ne__(self,other) :
		return self.symbol != other.symbol
	
	def priceRange( this ) :
		return this.high - this.low
	
	def __repr__(self) :
		return "Stock(%s,%s,%f,%f,%f,%f)"% \
				(self.name, self.symbol,
				self.price, self.low,
				self.high, self.volume)
	
	def __hash__(self) :
		return hash(self.symbol)

