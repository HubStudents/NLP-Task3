
import grpc
from transformers import pipeline

import QA_pb2_grpc
import QA_pb2

channel= grpc.insecure_channel('localhost:50051')
stub = QA_pb2_grpc.QAServiceStub(channel)
generator = pipeline('text-generation', model = 'gpt2')


def ask(textToCheck,qu):
    request = QA_pb2.QARequest(text=textToCheck, question=qu)
    reply = str (stub.Ask(request))
    return reply

def generateText(prompt,length,number):
    result = generator(prompt, max_length=length, num_return_sequences=number)
    return result

def printResult(list):
    for i in range (len(list)):
        print(list[i])


if __name__ == '__main__':

    textToCheck = """ World War I, also known as the Great War, began in 1914 after the assassination of Archduke Franz Ferdinand of Austria. 
    His murder catapulted into a war across Europe that lasted until 1918. During the conflict, Germany, Austria-Hungary, Bulgaria and the Ottoman Empire (the Central Powers) 
    fought against Great Britain, France, Russia, Italy, Romania, Canada, Japan and the United States (the Allied Powers). 
    Thanks to new military technologies and the horrors of trench warfare, World War I saw unprecedented levels of carnage and destruction. 
    By the time the war was over and the Allied Powers claimed victory, more than 16 million people—soldiers and civilians alike—were dead
                """
    qu = "Which event caused world war 1 ?"

    print(ask(textToCheck, qu))

    printResult(generateText(ask(textToCheck, qu),100,5))




