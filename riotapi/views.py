from django.shortcuts import render


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.restapi import Resp
from common.auth import CsrfAuthentication
from riotapi.serializer import RiotApiRuneParamSerializer

# Create your models here.

class RiotApiView(APIView):
    authentication_classes = (CsrfAuthentication,)
    permission_classes = (AllowAny,)

# https://global.api.pvp.net/api/lol/static-data/kr/v1.2/rune?runeListData=all&api_key=mykey
class LStatRuneView(RiotApiView):
    def get(self, request):
        """
        :param request:
        :return:
        """
        serializer = RiotApiRuneParamSerializer(data=request.data)
        if not serializer.is_valid():
            
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=Resp.err({
                                'message':  serializer.errors
                            }))
        
        
        vdata = serializer.validated_data
        # result = riotapi.staticdata.rune(vdata)
        result = ''
        return Response(data=Resp.success(
            self._format(request.data, result)
        ))
        
    def _format(self, reqParam, queryResult):
            
        return {
                "interval": reqParam['interval'],
                "value": queryResult
            }
        