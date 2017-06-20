from apns3 import APNs, Payload, Frame
from database import Database

import os.path
import time


class SendCron(object):

    def __init__(self):
        self.db = Database()
        self.tokens = self.db.token_select_all()

    def send_notification(self):
        payload = Payload(content_available=True)
        frame = Frame()

        identifier = 1
        expiry = int(time.time() + 3600)
        priority = 10

        for token in self.tokens:
            frame.add_item(token.token, payload, identifier, expiry, priority)

        apns = APNs(use_sandbox=True,
                    cert_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           'apns_localbattery_develop.pem'),
                    enhanced=True)

        apns.gateway_server.send_notification_multiple(frame)


if __name__ == '__main__':
    cron = SendCron()
    cron.send_notification()
