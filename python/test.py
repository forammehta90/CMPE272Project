import request_json

request = request_json.request_json()

if __name__ == "__main__":
    st='OKLAHOMA'
    ct='ALFALFA'
    request.analyze(st, ct)

