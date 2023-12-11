#!/usr/bin/env python3

from brain_module import ChatGPT

if  __name__ == "__main__":
    bot = ChatGPT()
    response = bot.request_openai(input("Hi this is ChatGPT, how can assist you today? "))
    print(response)
