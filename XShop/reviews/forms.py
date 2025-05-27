from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'rating', 
            'comment',
        )
    
    comment = forms.CharField()
    rating = forms.IntegerField()
        