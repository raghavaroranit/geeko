def main():
    url = '<webhook URL>' ## Provide the webhook URL
    bot_message = {
        'text' : 'XYZ'} ## Provide the message

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
