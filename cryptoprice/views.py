import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse


@csrf_exempt
def price(request):

    df_error_output = {
        "messages": [
            {
                "speech": "I didn't get you",
                "type": 0
            }
        ]
    }

    if request.method == 'POST':
        df_request = json.loads(request.body)
        if df_request['result']['action'] == 'cryptoprice':
            ticker_df = df_request['result']['parameters']['any']
            ticker_df_list = ticker_df.split()
            print(len(ticker_df_list))
            print(ticker_df_list)
            if len(ticker_df_list) > 1:
                return JsonResponse(df_error_output)
            else:
                coinmk_res = requests.get('https://api.coinmarketcap.com/v1/ticker/' + ticker_df.lower())
                if coinmk_res.status_code == 200:
                    coinmk_res_list = json.loads(coinmk_res.text)  # unable to figure out why it is returning in list instead of dict
                    coin_info = "Coin :" + coinmk_res_list[0]['name'] + "\nCoin Rank:" + str(coinmk_res_list[0]['rank']) + "\nCoin price: $" + str(coinmk_res_list[0]['price_usd'])
                    df_success_output = {
                        "messages": [
                            {
                                "speech": coin_info,
                                "type": 0
                            }
                        ]
                    }
                    return JsonResponse(df_success_output)
                else:
                    return JsonResponse(df_error_output)

    else:
        return HttpResponse("just a GET response")
