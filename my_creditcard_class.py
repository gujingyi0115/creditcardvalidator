class CreditCard:

	def __init__(self,cardnumber):
		self.cardnumber=cardnumber
		self.cardlength=self.long()
		self.cardtype=False
		self.valid=False

	def long(self):
		if len(self.cardnumber) == 15:
			self.cardlength = 15
		if len(self.cardnumber) == 16:     
			self.cardlength = 16
		return self.cardlength

	def card_type(self):
	
		if self.cardnumber[0] == '4':
			if self.cardlength == 16:
				self.cardtype = 'Visa'
		elif self.cardnumber[0:2] in ['51', '52','53','54','55'] and self.cardlength == 16:

			self.cardtype = 'Mastercard'
		elif self.cardnumber[0:2]=='34' or '37':
			if self.cardlength == 15:
				self.cardtype = 'AMEX'
		elif self.cardnumber[0:4] == '6011':
			if self.cardlength == 16:
				self.cardtype = 'Discover'
		
		return self.cardtype

	def validate(self):
		digits_doubled=[str(int(self.cardnumber[n])*2) if n%2 == 0 else str(int(self.cardnumber[n])) for n in range(len(self.cardnumber)) ]
		digits_splited=[int(x[0])+int(x[1]) if len(x) ==2 else int(x) for x in digits_doubled]
		a=0
		for i in digits_splited:
			a += i
		if a%10 == 0:
			self.valid = True
		return self.valid

cc_input=input("Give me a card number: ")
cc=CreditCard(cc_input)
print(cc.cardnumber)
print("Card type? " + str(cc.card_type()))
print("Valid length? " + str(cc.long()))
print("Pass algorithm? " + str(cc.validate()))