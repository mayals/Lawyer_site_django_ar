from django import forms


class ContactUsForm(forms.Form):
    subject = forms.CharField(
        label='الموضوع',
        max_length=100,
        required=True,
        disabled=False)


    from_email = forms.EmailField(
        max_length=200,
        label='البريد الألكتروني للمرسل',
        required=True)


    message = forms.CharField(
        label='الرسالة النصية',
        required=True,
        max_length=4000,
        help_text='لا تستخدم الرموز أو الأرقام أو الوجوه التعبيرية.',
        widget=forms.Textarea(attrs={'placeholder': 'إكتب رسالتك هنا'}))






    # this field not work
    # full_name = forms.CharField(
    #     max_length= 100,
    #     label=' sender Full Name',
    #     required=True)



    # this field not work
    # Mobile_num = forms.CharField(
    #     initial='00966*********',
    #     max_length=14,
    #     label='sender Mobile(WhatsApp) Number',
    #    required=True)


    
    
   
    
