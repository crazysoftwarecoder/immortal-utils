#!/usr/bin/env python3

from twilio.rest import TwilioRestClient
import sys

class LateMessager:
        """This class uses the Twilio API to inform the wife if I am coming later than usual from work."""

        ACCOUNT_SID = '<YOUR-TWILIO-SID-HERE>'
        AUTH_TOKEN = '<YOUR-TWILIO-AUTH-TOKEN-HERE>'

        lateness_map = {'1': 'Have some work, will be slightly late, will eat at home. Miss you.'
                        ,'2': 'I will be seriously late, I will eat outside. Good night and Sweet dreams!!'}

        phone_number = '<YOUR_WIFES_PHONE_NUMBER'

        def shoot_message(self, how_late, custom_message=''):
                message_text = self.lateness_map[how_late]
                if len(custom_message) > 0:
                        message_text = custom_message
                client = TwilioRestClient(self.ACCOUNT_SID, self.AUTH_TOKEN)
                client.messages.create(
                to=self.phone_number,
                from_='+<YOUR_TWILIO_PHONE_NUMBER>',
                body=message_text,)

if len(sys.argv) < 2:
        sys.exit('Usage: inform_late.py [how_late] where how_late is 1 -> will eat at home and 2 -> will eat outside, or type your custom message.')

how_late = sys.argv[1]

messager = LateMessager()

try:
        late_severity = int(how_late)
        if (int(how_late) > 2) and int((how_late) < 1):
                sys.exit('how_late can only be between 1 and 2 (both inclusive)')
                messager.shoot_message(how_late)
except ValueError:
        messager.shoot_message('1', how_late)
