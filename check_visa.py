import requests
from bs4 import BeautifulSoup
import time

# Define the URL of the website you want to check
# url = "https://ais.usvisa-info.com/en-ca/niv/schedule/51711203/appointment?utf8=%E2%9C%93&applicants%5B%5D=60325749&applicants%5B%5D=60325816&confirmed_limit_message=1&commit=Continue"  # Replace with the actual URL
url = "https://ais.usvisa-info.com/en-ca/niv/schedule/51711203/appointment/days/94.json?appointments[expedite]=false"

# Define the criteria for an update (e.g., specific text on the page)
update_criteria = "Toronto, ON, Ontario, M5G 1S4"  # Replace with your criteria

cookies = {
    "_yatri_session": "empBYU5tR0I1OUdyMDg1Tjh6alVRNDVtNlNIWGxIN1l2VUlwaW9jQUJWNTNoMWZ0cHlvQktWSWFUbkJBZXFiVHBXWkgyWXJKU2czY0hadjhvNEtQeWZrMjZQMmRpUktLYys2QTZWV1U2V05qdXBJYVJSejBBTFBNK0xlQUhIN2ROamE2S0Q4YldMR29iWUZaZmRack9TNjhyaW9pUFhjTXU4OUZqb0NUSXFxeURLS2RwaFJEWEh4ZXArNGZYM0pkYmtvLy81RmxVdnJrSGZ1cHNJQ2xpV09TNEJzUFIxb2FzTzRjQ25PdS9xRnRXNXRvRWZjREhoQnMwMkx6cjZMQkplTGk1aGV1UGFEZGhIeVVoTlVhcFBWMkdkS3lwcFZQYmlnRXNwR1VORDk5V3dYNW95RGM5NGZVbzJabWhqVE9CYUVFQm1CVkNCbzF5OGRyTlhLZzhYZjczOEFaNndKQVpxTkQ2NGlNMTRjd2wvaWZEQVZud3JiKzgzb1AvemUra243YVhNUjR2RlpUM2FSMXdYMXRHZXFsdFZka1EvM3Rpa0xFa1ZsZk9jVE9MdEpWQjBpeE56VE1hVVR2WjlpYTFjTzYxV1htU2tDZUVUK3VqcXhFUk9sUUVNL1NEZzRGOENtaEorT1g0T0tDSWxnVTVhWStydi9UUzlSTHVQaWRJSWJlMVdseHdCVGNVMVpRRjFYSEZtRXZOa2RIRnlPNnJvTFI1MXFHclVZPS0tN2tTY0RKbHYwYmJBUzZWV3JOOWdnZz09--2b3eb86a6460b26b3530fcb1c5fc4dd37b022764",
}

headers = {
    "GET": "/en-ca/niv/schedule/51711203/appointment/days/94.json?appointments[expedite]=false HTTP/1.1",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,af;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "_yatri_session=TTFRTDFWNXpOSHQ5K2lhNG9HQThuVjhPNWRkME9tOFFEYXNLNGlWbnZLM3dOOGtnM1hEd2RERWpwSXo0YjQvWTZrZnFURzJ4Q3k2VUlzQldJeWdPblFXMHlOd0xPYWxkMDhXSXdDbHVDSWlzK2wrSFo5NEdNeWZhQXVQWmR6M2xSSW50K0RyQ0o4MkUrR2dDcHUvNVN1L2l2c3hwY2dnclBubzNkNmEzVEc2WmtWRGlYUXRRV3FnZzJaaXBmVFJYYzN5MHJodXRKMHg4TC9nWkZXd3pXd3U5NDZ5U0FmYWJTeHVaQ0dkN0pibFNTTmp6WFZNYVpKYUpuTU9TUmpub2ZJQXdZWG5PbEUwWjZnNTZWSnFGeG41SFE2Uko1eklMRm1KbFd2UkxsNFg1SmtNVjlKWTJDajNCdFBWMDZIcGVoMm4ycENnalJoVytBUCtwQytpcTVHRytqcU1wdmswMGp2RUtnWnJJSDA2RlJpT2ptcmpjU1JSbEd4ZDFUK0lJL0VESUROSDZVeElKQXAyRmJZSXhTL244RE1GSWlOMEp5RHdHNWVyeHluMVpvam9EZnFMeFhCSVMwQXROZncxdmRWQnZoSG82dDczV1BUMEFHVHRRcUJJc2paYkt1Uk4rTXduTjBEVXRZZHFjNG1WTHJHaytNeFl6Mjhic05sSS9IZ3pWRm5TZytvNWRMWWZtdnEyL3dSSFcwNjgveG01cG1nQlFuaTB0Q29FPS0teGx3dmZQQVc3Y3JHTDlHY0tIS0V5UT09--6419e31c141e5695cff2939b625115fc9069e22a; path=/; HttpOnly; Secure; SameSite=None",
    "Host": "ais.usvisa-info.com",
    "If-None-Match": 'W/"4f53cda18c2baa0c0354bb5f9a3ecbe5"',
    "Referer": "https://ais.usvisa-info.com/en-ca/niv/schedule/51711203/appointment?utf8=%E2%9C%93&applicants%5B%5D=60325749&applicants%5B%5D=60325816&confirmed_limit_message=1&commit=Continue",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-CSRF-Token": "SwUgCpZYhPFKmX5sjfOKLOm10l9CysFfeSld5m7ZmNTbcjvwDQQNdKL4W0R78MvpLuUmINrov0NWck3inq3tjQ==",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

def check_website_for_update():
    response = requests.get(url, headers=headers, cookies=cookies)
    json_data = response.json()
    print(json_data[0])

if __name__ == "__main__":
    while True:
        check_website_for_update()
        time.sleep(300)  # Wait for 5 minutes (300 seconds) before checking again