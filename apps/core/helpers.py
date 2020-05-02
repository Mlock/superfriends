from django.shortcuts import redirect


def redirect_back(request):
    '''
    A simple trick to redirect back to the previous page
    '''
    return redirect(request.META.get('HTTP_REFERER', '/'))

