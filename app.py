import dns.resolver
from flask import Flask, request, render_template

debug = False
testdomains = ['outlook.com','hotmail.com', '7e837e8378e328.com', 'ba.com', 'checkpoint.com', 'google.com', 'aaa.com']

def CheckDomains(domains):
    results = {}
    for domain in domains:
        try:
            for mx in dns.resolver.query(domain, 'MX'):
                if "protection.outlook.com" in mx.to_text():
                    results[domain] = "O365"
                elif "aspmx.l.google.com" in mx.to_text():
                    results[domain] = "GSuite"
                else:
                    results[domain] = "Something else"
        except:
            if debug:
                print("Error:\t{} isn't a valid domain".format(domain))
    return results

def Results(r):
    print(r)

#res = CheckDomains(testdomains)
#Results(res)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/post', methods=['POST'])
def json_example():
    form_domains = request.form['domains'].split("\r\n")
    out = CheckDomains(form_domains)
    return render_template('result.html', result = out)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, use_reloader=True)
