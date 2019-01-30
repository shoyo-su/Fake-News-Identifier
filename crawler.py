import requests

def url_input():
    no_of_inputs=int(input("Mention  the no of inputs:"))
    index=0
    url_list=[]
    while index<no_of_inputs:
        x=input("Mention the url:")
        url_list.append(x)
        index=index+1
        return url_list

def html_extractor(url_list):
    content_l=[]
    for i in url_list:
        sess={'Sessionid':'1...'}
        req_info=requests.get(i,cookies=sess)
        content_l.append(req_info.content)

    return content_l


url_list=url_input()

content_l=html_extractor(url_list)

print(str(content_l))


'''
def word_finder(content_l):
    word=input("Search word:")
    content=" ".join(content_l)
    return content.find(word)
print(word_finder(content_l))
'''             
        
        
    
