   
def handlesignup(request):
    if request.method == 'POST':
        # RESPONSE = {"SUCCESS": True, "ERRORS": []}

        signup_username = request.POST['signup_username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        github_username = request.POST['github_username']
        signup_password = request.POST['signup_password']
        cf_signup_password = request.POST['cf_signup_password']
        agreed2TNC = request.POST['agreed2TNC']


        # Frisk Data

        ERROR_COUNT = 0

        if User.objects.filter(username=signup_username).first() != None:
            ERROR_COUNT += 1
            messages.error(request, "Username already exists!")
        
        if signup_password != cf_signup_password:
            ERROR_COUNT += 1
            messages.error(request, "Passwords don't match!")

        if agreed2TNC != 'on':
            ERROR_COUNT += 1
            messages.error(request, "You must agree to the <a href='#'>Terms and Conditions</a>")

        if ERROR_COUNT != 0:
            return redirect('signuporlogin')

        # CREATE USER NOW

        newuser = User.objects.create(username=signup_username, password=signup_password, first_name=first_name, email=email)
        UserProfile.objects.create(user=newuser,github_username=github_username)

        messages.success(request, f"Logged in as {newuser}")
        login(request, newuser)

        return redirect('home')
