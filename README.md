특정 사이트는 스크래핑을 막는 사이트가 있다.
그걸 회피하는 방법은
나의 브라우저가 해당 웹사이트에 Request를 보낼때 포함하는 Headers 값 중 User-Agent 값을 같이 보내주면 회피할 수 있다.

response = requests.get(
url,
headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
},
)
