from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        msg.body("Hey there! 👋 How can I help you today?")
    else:
        msg.body("I’m not sure how to respond to that yet. Add more features to make me smarter!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)