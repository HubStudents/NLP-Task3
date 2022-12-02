
import grpc
from transformers import pipeline

import QA_pb2_grpc
import QA_pb2

channel= grpc.insecure_channel('localhost:50051')
stub = QA_pb2_grpc.QAServiceStub(channel)
generator = pipeline('text-generation', model = 'gpt2')


def ask(textToCheck,qu):
    request = QA_pb2.QARequest(text=textToCheck, question=qu)
    reply = str (stub.Ask(request)).replace("answer:","")
    return reply

def generateText(prompt,length,number):
    result = generator(prompt, max_length=length, num_return_sequences=number)
    for i in range (len(result)):
        result[i]= result[i]['generated_text']
    return result

def printResult(list):
    for i in range (len(list)):
        print(list[i])
        print("##########")


if __name__ == '__main__':

    textToCheck = """ 
    An economic system is a means by which societies or governments organize and distribute available resources, services, and goods across a geographic region or country. 
    Economic systems regulate the factors of production, including land, capital, labor, and physical resources. 
    An economic system encompasses many institutions, agencies, entities, decision-making processes, and patterns of consumption that comprise the economic structure of a given community.
    Capitalism generally features the private ownership of the means of production (capital) and a market economy for coordination. 
    Corporate capitalism refers to a capitalist marketplace characterized by the dominance of hierarchical, bureaucratic corporations.
    Mercantilism was the dominant model in Western Europe from the 16th to 18th century. 
    This encouraged imperialism and colonialism until economic and political changes resulted in global decolonization. 
    Modern capitalism has favored free trade to take advantage of increased efficiency due to national comparative advantage and economies of scale in a larger, more universal market. 
                """
    qu = "What are capitalism  characteristics ?"

    print( ask(textToCheck, qu))

    printResult ( generateText(ask(textToCheck, qu),150,10)  )




