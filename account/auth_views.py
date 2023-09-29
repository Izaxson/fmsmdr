import random
from urllib import request
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from twilio.rest import Client

from account.forms import LoginForm
from fms.models import OTPVerification

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Enter the pin Sent to your phone')
                    return render(request, 'fms/dashboard.html')
                
                
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.error(request, 'Error login to account, confirm your credentials')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.error(request,'Session Terminated, Login again')
    return redirect('/')



@method_decorator(login_required, name='dispatch')
class VerifyOTPView(View):
    template_name = 'account/send_otp.html'

    def post(self, request, *args, **kwargs):
        otp_input = request.POST.get('otp_input')
        otp_verification = OTPVerification.objects.filter(user=request.user, is_verified=False).first()

        if otp_verification and otp_input == otp_verification.otp_token:
            otp_verification.is_verified = True
            otp_verification.save()
            
            # Send the OTP via SMS to the user's phone number
            self.send_otp_to_user(request.user, otp_input)
            
            return redirect('dashboard')

        return render(request, self.template_name, {'error_message': 'Invalid OTP'})

    def send_otp_to_user(self, user, otp):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        # Retrieve the user's phone number from the user model (adjust as needed)
        user_phone_number = user.profile.phone_number  # Replace with the actual attribute name
        
        # Send the OTP via SMS
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=user_phone_number
        )
class OTPLoginView(View):
    template_name = 'account/login.html'
    redirect_authenticated_user = True  # Redirect logged-in users to the 'next' URL if provided

    def get_success_url(self):
        return reverse_lazy('dashboard')  # Customize the success URL as needed

    def form_valid(self, form):
        # Check if the user is verified with OTP
        if self.request.user.is_authenticated and self.request.user.otpverification.is_verified:
            return super().form_valid(form)
            
        else:
            return redirect('verify_otp')  # Redirect to the OTP verification view
        
@method_decorator(login_required, name='dispatch')
class SendOTPView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        otp_token = str(random.randint(100000, 999999))  # Generate a random OTP

        # Store the OTP and user's phone number in the database
        otp_verification = OTPVerification(user=user, otp_token=otp_token)
        otp_verification.save()

        # Send the OTP via SMS using Twilio (add Twilio integration here)

        return redirect('verify_otp')        