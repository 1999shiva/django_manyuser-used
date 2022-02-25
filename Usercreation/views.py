import json
from sqlite3 import IntegrityError

from rest_framework.response import Response
from django.forms import ValidationError
from Usercreation.serializer import RegistrationSerializer,CampaignsSerializer, OrganizationSerializer
from rest_framework.authtoken.models import Token
from .models import Campaigns, Users
from rest_framework.views import APIView
from .serializer import  RegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics,status
from rest_framework import viewsets


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def Register_Users(request):
#     try:
#         data = {}
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             account = serializer.save()
#             account.is_active = True
#             account.save()
#             token = Token.objects.get_or_create(user=account)[0].key
#             data["message"] = "user registered successfully"
#             data["email"] = account.Email_Address
#             data["username"] = account.name
#             data["token"] = token

#         else:
#             data = serializer.errors


#         return Response(data)
#     except IntegrityError as e:
#         account=Users.objects.get(username='')
#         account.delete()
#         raise ValidationError({"400": f'{str(e)}'})

#     except KeyError as e:
#         print(e)
#         raise ValidationError({"400": f'Field {str(e)} missing'})
@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["email"] = account.Email_Address
            data["username"] = account.name
            data["token"] = token

        else:
            data = serializer.errors


        return Response(data)
    except IntegrityError as e:
        account=Users.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})



@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        reqBody = json.loads(request.body)
        email1 = reqBody['Email_Address']
        password = reqBody['password']
        try:

            Account = Users.objects.get(Email_Address=email1)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=Account)[0].key
        

        if Account:
            if Account.is_active:
                # login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.Email_Address

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})





class OrganizationView(APIView):
    serializer_class = OrganizationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)





@api_view(['GET', 'POST'])
def CampignsView(request, Email_Address=None,**validated_data):
    try:
        
        user = Users.objects.filter(Email_Address = Email_Address).first()

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        contents = Campaigns.objects.filter(user= user.pk)
        serializer = CampaignsSerializer(contents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data["user"] = user.id
        serializer = CampaignsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


