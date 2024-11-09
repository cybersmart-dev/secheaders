import requests
import pathlib
from colorama import Fore,init
from .utils import *

sec_headers = open("main/sec_headers.txt", "r").read().split("\n")
init()

class SecHeaders:
    def __init__(self):
        
        self.args = args
        self.parser = parser
        self.banner()
        
    def run(self):
        
        if not self.args.url:
            # check for urls list if single url not found
            if self.args.list: 
                self.extract_file(self.args.list)
                
            else:
                self.parser.print_help()
        else:
            # if url is valid make attack
            if self.is_valid_url(self.args.url):
                self.attack_url(self.args.url)
                
            else:
                self.print_error("invalid url. url most be contain https or http")
            
    def is_valid_url(self, url):
            if "https://" in url or "http://" in url:
                return True
            else:
                return False
                
    def attack_url(self, url):
        info = self.get_url_info(url)
        if info.get("status") == 301 or info.get("status") == 302:
              location = info.get("headers").get("location")
              if not self.is_valid_url(location):
                  location = f"https://{get_domain(url)}{location}"
              location_info = self.get_url_info(location, True)
              print(f"{Fore.YELLOW} [{url}] {Fore.WHITE}: {self.status_code(info.get('status'))} =>{Fore.LIGHTBLACK_EX} { location}{Fore.WHITE}\n")
              self.check_headers_sec(url, location_info)
        else:
            print(f"{Fore.YELLOW} [{url}] {Fore.WHITE} => {self.status_code(info.get('status'))}\n")
            self.check_headers_sec(url, info)
        self.print_success("Done!")
        
    def attack_list_urls(self, list):
        for url in list:
            info = self.get_url_info(url)
            if info.get('status') != None:
                if info.get("status") == 301 or info.get("status") == 302:
                    location = info.get("headers").get("location")
                    if not self.is_valid_url(location):
                        location = f'https://{get_domain(url)}{location}'
                    location_info = self.get_url_info(location, True)
                    print(f"{Fore.YELLOW} [{url}] {Fore.WHITE}: {self.status_code(info.get('status'))} =>{Fore.LIGHTBLACK_EX} { location}{Fore.WHITE}\n")
                    self.check_headers_sec(url, location_info)
                else:
                    print(f"{Fore.YELLOW} [{url}] {Fore.WHITE}: {self.status_code(info.get('status'))}\n")
                    self.check_headers_sec(url, info)
        self.print_success('Done!')
        
    def check_headers_sec(self, url, info):
     
        for sec_header in sec_headers:
            if sec_header in info.get("headers"):
                print(f"{Fore.GREEN} √ {sec_header}{Fore.WHITE}")
            else:
                print(f"{Fore.RED} × {sec_header}{Fore.WHITE}")
                
    def status_code(self, code):
        code = int(code)
        if code >= 200 and code <= 299:
            return f"{Fore.GREEN}{code}{Fore.WHITE}"
            
        elif code >= 400 and code <= 499:
            return f"{Fore.RED}{code}{Fore.WHITE}"
            
        elif code >= 300 and code <= 399:
            return f"{Fore.YELLOW}{code}{Fore.WHITE}"
            
        else:
            return f"{Fore.CYAN}{code}{Fore.WHITE}"
            
    def extract_file(self, file):
        urls = []
        if self.is_valid_path(file):
            urls_list = open(file, 'r').read().split("\n")
            for url in urls_list:
                if self.is_valid_url(url):
                    urls.append(url)
                else:
                    if '.' in url:
                        url = f"https://{url}"
                        urls.append(url)
                    else:
                        ...
        else:
            self.print_error("file not found {file}")
             
        self.attack_list_urls(urls)
        
    def print_error(self, msg):
        print(f"\n{Fore.RED}[×]{Fore.CYAN} {msg} {Fore.RESET}")
        
    def print_success(self, msg):
        print(f"\n{Fore.GREEN}[√] {Fore.CYAN} {msg} {Fore.RESET}")
        
    def get_url_info(self, url, redirect=False):
        
        try:
            res = requests.get(url, allow_redirects=redirect,stream=True)
            return {'status':res.status_code,'headers':res.headers,'body':res.text}
        except requests.exceptions.ConnectionError as e:
            #print(f"{Fore.RED}{e}{Fore.WHITE}")
            return {'er':1}
            
    def is_valid_path(self, path):
        return pathlib.Path(path).resolve().exists()
        
    def banner(self):
        b = f""" {Fore.YELLOW}
 ____  ____  ___      _  _  ____   __   ____  ____  ____  ____ 
/ ___)(  __)/ __)___ / )( \(  __) / _\ (    \(  __)(  _ \/ ___)
\___ \ ) _)( (__(___)) __ ( ) _) /    \ ) D ( ) _)  )   /\___ \
(____/(____)\___)    \_)(_/(____)\_/\_/(____/(____)(__\_)(____/
      {Fore.GREEN}  
        Developer: Cyber Smart
        Version: 0.1-shark 🐋
        Url: github.com/cybersmart-dev/secHeaders.git {Fore.WHITE}
        
        {Fore.WHITE}"""
        print(b)