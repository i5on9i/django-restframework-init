# coding=utf-8

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, CSRFCheck

__author__ = 'namh'



class CsrfAuthentication(BaseAuthentication):
    """
    Check only Csrf token
    """

    def authenticate(self, request):
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """

        self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return ({}, None)

    def enforce_csrf(self, request):
        """
        Enforce CSRF validation for session based authentication.
        """
        reason = CSRFCheck().process_view(request, None, (), {})
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)
