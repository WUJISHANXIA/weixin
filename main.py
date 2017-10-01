# !/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from bottle import Bottle, run, request
import receive
import reply
app = Bottle()
@app.route('/wx',method='GET')
def test_token():
    try:
        data = request.query
        if len(data) == 0:
            return 'hello, this is wuji'
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "hello2017"
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception, Argument:
        return Argument

@app.route('/wx',method='POST')
def weixin():
    receive_msg = receive.parse_xml(request.body.read())
    if receive_msg.msg_type == 'text':
        reply_msg = reply.TextMsg(
            to_user_name=receive_msg.from_user_name,
            from_user_name=receive_msg.to_user_name,
            content=receive_msg.content
        )
        return reply_msg.send()
    elif receive_msg.msg_type == 'image':
        reply_msg = reply.ImageMsg(
            to_user_name=receive_msg.from_user_name,
            from_user_name=receive_msg.to_user_name,
            media_id=receive_msg.media_id
        )
        return reply_msg.send()
    else:
        reply_msg = reply.Msg()
        return reply_msg.send()
run(app=app, host='0.0.0.0', port=80)