from django.http import JsonResponse
from rest_framework.decorators import api_view
from pymarket.models import Food, TransactionDetail
from pymarket.serializers import FoodSerializer, TransactionDetailSerializer, TransactionSerializer
import midtransclient

@api_view(['POST'])
def createTransaction(request):
    snap = midtransclient.Snap(
        is_production=False,
    )

    param = {
        "transaction_details": {
            "order_id": request.data['order_id'],
            "gross_amount": str(request.data['total'])
        }
    }

    transaction_snap = snap.create_transaction(param)
    transaction_redirect_url = transaction_snap['redirect_url']

    transactionData = {
        "order_id" : request.data['order_id'],
        "total" : request.data['total'],
        "payment_url" : transaction_redirect_url
    }

    transaction = TransactionSerializer(data=transactionData)
    if transaction.is_valid():
        transaction.save()

    transaction_id = transaction.data['id']
    transaction_details = []

    for food in request.data['foods']:
        transactionDetailData = {
            "food" : food['food_id'],
            "transaction" : transaction_id,
            "quantity" : food['quantity'],
            "size" : food['size']
        }
        
        transactionDetailCreate = TransactionDetailSerializer(data=transactionDetailData)
        if transactionDetailCreate.is_valid():
            transactionDetailCreate.save()
        
        transaction_details.append(transactionDetailCreate.data)
    

    return JsonResponse({
        "message" : "success",
        "data" : {
            "transaction" : transaction.data,
            "transaction_details" : transaction_details
        }
    })

@api_view(['GET'])
def getAllTransactions(request):
    transaction_detail = TransactionDetail.objects.all()
    serializer = TransactionDetailSerializer(transaction_detail, many=True)

    for s in serializer.data:
        food = Food.objects.get(id=s['food'])
        fserializer = FoodSerializer(food)

        s['food'] = fserializer.data

    return JsonResponse({
        "message" : "success get transactions",
        "data" : serializer.data
    })
