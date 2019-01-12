import dns.resolver
from flask import Flask, request, render_template

debug = False

mx_dict = {
    "protection.outlook.com" : "Office 365",
    "aspmx.l.google.com" : "GSuite",
    "mailcontrol.com" : "Forcepoint",
    "messagelabs.com" : "Symantec",
    "mimecast" : "Mimecast",
    "pphosted.com" : "Proofpoint",
    "ppe-hosted.com" : "Proofpoint (Essentials)",
    "barracudanetworks.com" : "Barracuda",
    "icritical.com" : "iCritical / Fusemail",
    "trendmicro" : "Trend Micro"
}
def CheckDomains(domains):
    results = {}
    for domain in domains:
        try:
            for mx in dns.resolver.query(domain, 'MX'):
                results[domain] = 'Unknown SaaS solution'
                for key, val in mx_dict.items():
                    if key in mx.to_text().lower():
                        results[domain] = val
                        break
        except:
            if debug:
                print("Error:\t{} isn't a valid domain".format(domain))
    return results


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
