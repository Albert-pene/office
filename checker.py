import time 
import requests
import os
os.system("clear")
time.sleep(2)
print("\n\n\n\n")
print("        \33[92mwelcome on url_checker By Nour Lyahyaoui !\33[m")
time.sleep(0.8)
print("\33[92musage: at first, copy the url that you want to check (https://www.exemple.com) and go download a wordlist to try like https://www.exemple.com\33[m\33[91m/word_to_try\33[m")
def check_url_exists(current_url,url):
    if not url.startswith("http"):
        url = f"{current_url}/{url}"
    try:
        response = requests.head(url, timeout=5)
        status_code = response.status_code
        if status_code == 100:
            return f"\33[95m[*]\33[m\33[95mThe URL {url} continues with additional information.\33[m"
        elif status_code == 101:
            return f"\33[95m[*]\33[m\33[95mThe URL {url} is switching protocols.\33[m"
        elif status_code == 102:
            return f"\33[95m[*]\33[m\33[95mThe URL {url} processing has been accepted.\33[m"
        elif status_code == 200:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} exists and is accessible.\33[m"
        elif status_code == 201:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has been created.\33[m"
        elif status_code == 202:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has been accepted for processing.\33[m"
        elif status_code == 203:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} is a non-authoritative information.\33[m"
        elif status_code == 204:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has no content.\33[m"
        elif status_code == 205:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has been reset.\33[m"
        elif status_code == 206:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has partial content.\33[m"
        elif status_code == 207:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has multi-status.\33[m"
        elif status_code == 208:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has already reported.\33[m"
        elif status_code == 226:
            return f"\33[92m[*]\33[m\33[92mThe URL {url} has IM used.\33[m"
        elif status_code == 300:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} has multiple choices.\33[m"
        elif status_code == 301:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} has been permanently moved to {response.headers['Location']}.\33[m"
        elif status_code == 302:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} has been temporarily moved to {response.headers['Location']}.\33[m"
        elif status_code == 303:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} can be found at {response.headers['Location']}.\33[m"
        elif status_code == 304:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} has not been modified.\33[m"
        elif status_code == 305:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} must be accessed through a proxy.\33[m"
        elif status_code == 306:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} must be accessed through a different proxy.\33[m"
        elif status_code == 307:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} has been temporarily redirected to {response.headers['Location']}.\33[m"
        elif status_code == 308:
            return f"\33[94m[*]\33[m\33[94mThe URL {url} has been permanently redirected to {response.headers['Location']}.\33[m"
        elif status_code == 400:
            return f"\33[91m[*]The URL {url} has a bad request.\33[m"
        elif status_code == 401:
            return f"\33[91m[*]The URL {url} requires authentication.\33[m"
        elif status_code == 402:
            return f"\33[91m[*]The URL {url} requires payment.\33[m"
        elif status_code == 403:
            return f"Access to the URL {url} is forbidden."
        elif status_code == 404:
            return f"\33[91m[*]The URL {url} was not found.\33[m"
        elif status_code == 405:
            return f"The request method is not allowed for the URL {url}."
        elif status_code == 406:
            return f"\33[91m[*]The URL {url} is not acceptable.\33[m"
        elif status_code == 407:
            return f"Proxy authentication is required for the URL {url}."
        elif status_code == 408:
            return f"The request to the URL {url} timed out."
        elif status_code == 409:
            return f"The request to the URL {url} conflicts with an existing resource."
        elif status_code == 410:
            return f"\33[91m[*]The URL {url} is gone.\33[m"
        elif status_code == 411:
            return f"\33[91m[*]The URL {url} requires a length.\33[m"
        elif status_code == 412:
            return f"The precondition for the URL {url} failed."
        elif status_code == 413:
            return f"The request to the URL {url} is too large."
        elif status_code == 414:
            return f"\33[91m[*]The URL {url} is too long.\33[m"
        elif status_code == 415:
            return f"The media type for the URL {url} is not supported."
        elif status_code == 416:
            return f"The range for the URL {url} is not satisfiable."
        elif status_code == 417:
            return f"The expectation for the URL {url} failed."
        elif status_code == 418:
            return f"\33[91m[*]The URL {url} is a teapot.\33[m"
        elif status_code == 421:
            return f"The request to the URL {url} was misdirected."
        elif status_code == 422:
            return f"\33[91m[*]The URL {url} is unprocessable.\33[m"
        elif status_code == 423:
            return f"\33[91m[*]The URL {url} is locked.\33[m"
        elif status_code == 424:
            return f"\33[91m[*]The URL {url} failed dependency.\33[m"
        elif status_code == 425:
            return f"\33[91m[*]The URL {url} is too early.\33[m"
        elif status_code == 426:
            return f"\33[91m[*]The URL {url} needs to be upgraded.\33[m"
        elif status_code == 428:
            return f"\33[91m[*]The URL {url} requires preconditions.\33[m"
        elif status_code == 429:
            return f"\33[91m[*]The URL {url} has too many requests.\33[m"
        elif status_code == 431:
            return f"The request headers for the URL {url} are too large."
        elif status_code == 451:
            return f"\33[91m[*]The URL {url} is unavailable for legal reasons.\33[m"
        elif status_code == 500:
            return f"The URL {url} has an internal server error."
        elif status_code == 501:
            return f"The URL {url} is not implemented."
        elif status_code == 502:
            return f"The URL {url} has a bad gateway."
        elif status_code == 503:
            return f"The URL {url} is unavailable due to maintenance."
        elif status_code == 504:
            return f"The URL {url} has a gateway timeout."
        elif status_code == 505:
            return f"The HTTP version for the URL {url} is not supported."
        elif status_code == 506:
            return f"The URL {url} has a variant also negotiates."
        elif status_code == 507:
            return f"The server lacks sufficient storage to process the request for the URL {url}."
        elif status_code == 508:
            return f"The request detected a loop for the URL {url}."
        elif status_code == 510:
            return f"The request is not extended for the URL {url}."
        else:
            return f"The URL {url} returned an unexpected status code of {status_code}."
    except requests.exceptions.RequestException as e:
        return f"\33[91m[-]An error occurred while checking the URL {url}: {str(e)}.\33[m"




time.sleep(1)
print("")
current_url=input("\33[96m[***]Enter the first url to discover [https://www.exemple.com]:\33[m")
time.sleep(0.8)
print("")
print(f"\33[96m[++]Target ==> {current_url} .\33[m")
print("")
time.sleep(0.8)
url_list_path=input(f"\33[96m[***]Enter the full path list of words you want to try with {current_url}\33[m :")
time.sleep(0.8)
print("")
print(f"\33[96m[++]Wordlist path ==> {url_list_path} .\33[m")
print("")
time.sleep(0.8)
print("\n--------------------------------------------------------------------------------------\n")
time.sleep(0.5)
print("----------------------------------------------------------output here :")
print("\n")
with open(url_list_path, 'r') as f:
        urls = [line.strip() for line in f]
        for url in urls:
            print(check_url_exists(current_url,url))
print("")
print("-------------thanks for using, I hope that you will have a good bug bounty day !!! ")

        