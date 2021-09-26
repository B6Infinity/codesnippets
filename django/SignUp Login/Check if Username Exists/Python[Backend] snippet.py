
def usernameexists(request):
    if request.method == 'POST':
        RESPONSE = {"SUCCESS": True, "ERRORS": []}

        username_to_check_availability = request.POST['username_to_check_availability']

        if User.objects.filter(username=username_to_check_availability).first()!= None:
            RESPONSE['SUCCESS'] = False
            RESPONSE['ERRORS'].append("Username Already Exists")

        return JsonResponse(RESPONSE)
