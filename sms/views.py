from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import requests
import json

import text


# Create your views here.

def testing(request):
	return HttpResponse("Testing successful...")


class CommonUrl(generic.View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello")


class ChatBot(generic.View):

	def get(self, request, *args, **kwargs):
		print self.request.GET
		if self.request.GET.get('hub.verify_token') == '': #Enter your verify token here
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		message = json.loads(self.request.body.encode('utf-8'))

		for entry in message['entry']:
			for msg in entry.get('messaging'):
				print msg.get('message')

				if "text" in msg.get('message').keys():
					reply_to_message(msg.get('sender')['id'], msg.get('message')['text'])
				else:
					print "Some Error!!!"

		return HttpResponse("None")


def reply_to_message(user_id, message):
	access_token = '' #Enter your access_token here
	url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + access_token
	resp = generate_response(message)
	send_resp = {"recipient":{"id":user_id}, "message":{"text": resp}}
	response_msg = json.dumps(send_resp)
	status = requests.post(url, headers={"Content-Type": "application/json"},data=response_msg)
	print status.json()

def generate_response(msg):
	if 'send' in msg:
		number1 = msg.split(' ')[1]
		message1 = ' '.join([ix for ix in msg.split(' ')[2:]])
		text.send_message(number1, message1)
		return "message sent"
	else:
		return "Please try again with the following input:\nsend <number> <message>"
