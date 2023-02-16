from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
from easyleasy2.models import *


class ProductAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            products = Product.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        product = self.get_object(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PromoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            promos = Promo.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PromoSerializer(promos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PromoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromoDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Promo.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        promo = self.get_object(pk=pk)
        if promo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PromoSerializer(promo)
        return Response(serializer.data)

    def put(self, request, pk):
        promo = self.get_object(pk=pk)
        if promo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PromoSerializer(promo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        promo = self.get_object(pk=pk)
        if promo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        promo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SupportRequestAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            support_request = Support_Request.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SupportRequestSerializer(support_request, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupportRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupportRequestDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Support_Request.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        support_request = self.get_object(pk=pk)
        if support_request is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SupportRequestSerializer(support_request)
        return Response(serializer.data)

    def put(self, request, pk):
        support_request = self.get_object(pk=pk)
        if support_request is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SupportRequestSerializer(support_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        support_request = self.get_object(pk=pk)
        if support_request is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        support_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InterestRateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            interest_rate = Interest_Rate.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InterestRateSerializer(interest_rate, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InterestRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterestRateDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Interest_Rate.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        interest_rate = self.get_object(pk=pk)
        if interest_rate is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InterestRateSerializer(interest_rate)
        return Response(serializer.data)

    def put(self, request, pk):
        interest_rate = self.get_object(pk=pk)
        if interest_rate is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InterestRateSerializer(interest_rate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        interest_rate = self.get_object(pk=pk)
        if interest_rate is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        interest_rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientProfileAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            client_profile = ClientProfile.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientProfileSerializer(client_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientProfileDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ClientProfile.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        client_profile = self.get_object(pk=pk)
        if client_profile is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClientProfileSerializer(client_profile)
        return Response(serializer.data)

    def put(self, request, pk):
        client_profile = self.get_object(pk=pk)
        if client_profile is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClientProfileSerializer(client_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client_profile = self.get_object(pk=pk)
        if client_profile is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        client_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            application = Application.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ApplicationSerializer(application, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        application = self.get_object(pk=pk)
        if application is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk):
        application = self.get_object(pk=pk)
        if application is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        application = self.get_object(pk=pk)
        if application is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DealAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            deal = Deal.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DealSerializer(deal, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Deal.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        deal = self.get_object(pk=pk)
        if deal is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DealSerializer(deal)
        return Response(serializer.data)

    def put(self, request, pk):
        deal = self.get_object(pk=pk)
        if deal is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DealSerializer(deal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        deal = self.get_object(pk=pk)
        if deal is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            document = Document.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentSerializer(document, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentToClientAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, client_id):
        try:
            documents = Document.objects.filter(client_profile=ClientProfile.objects.get(pk=client_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)


class DocumentDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        document = self.get_object(pk=pk)
        if document is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk):
        document = self.get_object(pk=pk)
        if document is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        document = self.get_object(pk=pk)
        if document is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

