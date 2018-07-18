from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from index.models import UserTicket


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):

        ticket = request.COOKIES.get('ticket')

        if not ticket:
            pass

        userticket = UserTicket.objects.filter(ticket=ticket)

        if userticket:
            if userticket[0].out_time.replace(tzinfo=None) > datetime.utcnow():
                request.user = userticket[0].user
            else:
                userticket.delete()
        else:
            return None