# -*- coding: utf-8 -*-
# Copyright (c) 2021, Tridz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import random

class Customer(Document):
	def codeGenerator(self):
		
		code_doc=frappe.db.get_all('Customer',['customer'])
		for a in code_doc:
			if a['customer']==self.customer:
				code_name=self.customer[0:3]
				
		upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
		numbers = "1234567890"
		total = upper+numbers
		length = 8
		self.referral = "".join(random.sample(total,length))
		self.referral_code=self.referral+code_name
		return self.referral_code

		

	def after_insert(self):
		
		self.referral_id = self.codeGenerator()		
	def validate(self):
		customer_doc = frappe.db.get_all('Customer',fields=['customer','referral_id','referred_by'])
	
		for i in customer_doc:
			if i['referral_id'] == self.enter_referral_code:
				self.referred_by = i['customer']

				
	
				#referred_by_obj = frappe.db.get_value('Customer',{ "customer": i['customer']})		
				#referred_by_obj =frappe.get_value('Customer', i['customer'])
				#frappe.throw(i['customer'])
				# referred_doc=frappe.get_doc('Customer',self.referred_by)
				# frappe.throw(self.referred_by)
				# refto = referred_doc.referred_to
				# for d in refto:
				# 	d.customer_name = self.customer
				# 	d.mobile_number = self.phone_number
				#referred_by_customer_doc = frappe.db.set_value('Referred To',self.customer,'customer_name')	

				#testing

				

				
				

		



	

		

		

	
	
		


	
