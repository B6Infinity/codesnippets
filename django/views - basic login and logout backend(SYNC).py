
def logoutuser(request):
    logout(request)
    return redirect('home')

def handlelogin(request):
    if request.method == 'POST':
        # RESPONSE = {"SUCCESS": True, "ERRORS": []}

        username = request.POST['login_username']
        password = request.POST['login_password']

        # Frisk Data
        if User.objects.filter(username=username).first() == None:
            # RESPONSE['SUCCESS'] = False
            # RESPONSE['ERROR'].append("Username does not exist!")
            messages.error(request, "Username does not exist!")
            
            return redirect('loginorsignup')
        
        login_user = authenticate(username=username, password=password)

        if login_user is None:
            messages.error(request, "Invalid Passsword!")
            return redirect('loginorsignup')
        
        # Correct Creds - Login Now... HAYAKU!

        messages.success(request, f"Logged in as {login_user}!")

        login(request, login_user)

        return redirect('home')
