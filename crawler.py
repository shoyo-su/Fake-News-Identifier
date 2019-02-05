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

print(str(content_l[:300]))



def word_finder(content_l):
    word=input("Search word:")
    word=str(word)
    #content=" ".join(content_l)
    pos_l=[]
    content_l=content_l[0]
    content_len=len(content_l)
    nl=[]
    ide=0
    while ide<content_len:
        wr=content_l[ide]
        nl.append(wr.decode('Latin-1'))
        ide=ide+1
    content_l="".join(nl)    
    word_len=len(word)
    content_len=len(content_l)
    iter_index=0
    while iter_index<content_len:
    
        check_word=content_l[iter_index:iter_index+word_len:word_len]
        print(word_len,iter_index)
        print(check_word)
        #check_word=check_word.decode('Latin-1')
        
        print(check_word,word)
        if check_word==word:
            print("went in")
            pos_l.append(iter_index)
        iter_index=iter_index+word_len
    return pos_l


print(word_finder(content_l))
             
        
        
    
