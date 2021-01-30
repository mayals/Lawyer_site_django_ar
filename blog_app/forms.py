from .models import Comment,Post
from django import forms



# ----- add post form --------#
class PostForm(forms.ModelForm):
    post_title = forms.CharField(label='عنوان الموضوع', max_length=100,required=True, disabled=False)
    post_text = forms.CharField(label='نص الموضوع',
                                max_length=4000,
                                help_text='يجب أن لا يتجاوز طول النص 4000 ',
                                widget = forms.Textarea(attrs={'placeholder': ' إكتب موضوعك هنا .. '}))
    class Meta:
        model = Post
        fields = ('post_title', 'post_text')




# ----- add comment form --------#
class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label='نص التعليق',
                                max_length=4000,
                                help_text='يجب أن لا يتجاوز طول التعليق 4000',
                                widget=forms.Textarea(
                                    attrs={'placeholder': 'ضع تعليقك هنا'}))
    class Meta:
        model = Comment
        fields = ['comment_text']
