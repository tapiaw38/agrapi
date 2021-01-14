""" User Serializers. """

# Django
from django.conf import settings
from django.contrib.auth import (
    authenticate,
    password_validation
)
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Django Rest Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Utilities  
from datetime import timedelta
import jwt 

# Profile Serializer
from user.serializers.profile import ProfileModelSerializer

# Models
from user.models import User, Profile

class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer """

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """ Meta class """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_admin',
            'profile',
        )
        
class UserSignUpSerializer(serializers.Serializer):
    """ User sign up serializer """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Phone validator
    phone_regex = RegexValidator(
        regex=r'\d{10,10}$',
        message= "Debes ingresar un número con el siguiente formato: 3837430000. Hasta 10 digitos."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8,max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2,max_length=30)
    last_name = serializers.CharField(min_length=2,max_length=30)

    def validate(self, data):
        """ Validacion de contraseña """

        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraselas no cohinciden.")

        password_validation.validate_password(passwd)

        return data
    
    def create(self, data):
        """ Creacionnde usuario y perfil. """

        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False, is_pollster=False, is_admin=False)
        profile = Profile.objects.create(user=user)
        #self.send_confirmation_email(user)
        return user

    '''
    def send_confirmation_email(self, user):
        """ Funcion de envio de token para verificar cuenta. """

        verification_token = self.gen_verification_token(user)
        subject = "Bienvenido @{} a la confirmación de mail para usar Tinogasta Productiva".format(user.username)
        from_email = 'Tinogasta Productiva'
        content =  render_to_string(
            'emails/user/account_verification.html',
            {'token': verification_token, 'user':user}
            )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
    '''
    def gen_verification_token(self, user):
        """ Crea un Json Web Token para ser usado 
        en la verificacion de la cuenta. """

        exp_date = timezone.now() + timedelta(seconds=360)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='SH256')

        return token.decode()


class UserLoginSerializer(serializers.Serializer):
    """ User login serializer. """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self, data):
        """ Chequeo de credenciales. """

        user = authenticate(username=data['email'],password=data['password'])
        if not user:
            raise  serializers.ValidationError('Credenciales invalidas')
        if not user.is_pollster:
            raise serializers.ValidationError('La cuenta no esta verificada')
        
        self.context['user'] = user
        return data

    def create(self, data):
        """ Genaracion o recuperación de nuevo token. """
        token, created = Token.objects.get_or_create(user=self.context['user'])

        return self.context['user'], token.key

class UserDataSerializer(serializers.ModelSerializer):
    """ User data serializer """

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """ Meta class """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_admin',
            'is_pollster',
            'profile',
        )
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.is_pollster = validated_data.get('is_pollster', instance.is_pollster)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        
        
        instance.save()

        profile.picture = profile_data.get(
            'picture',
            profile.picture
        )
        profile.polls = profile_data.get(
            'polls',
            profile.polls
         )
        profile.save()

        return instance