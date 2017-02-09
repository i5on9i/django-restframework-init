
# coding=utf-8

__author__ = 'namh'



class Resp(object):
    @staticmethod
    def success(param):
        """

        :param param: python-dict
        :return:
        """
        return {'success' : param}

    @staticmethod
    def err(param):
        """

        :param param: python-dict
        :return:
        """
        return {'error' : param}


def dictfetchall(cursor):
    """
    :ref : https://docs.djangoproject.com/es/1.9/topics/db/sql/
    :param cursor:
    :return:
    """
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dtformat(date):
    if date is None:
        return ''
    return date.strftime("%Y-%m-%d")

def quarterStartDateformat(date):
    if date is None:
        return ''
    return date.strftime("%Y-%m-01")
