import dns.resolver
from flask import Flask, request, render_template

debug = False

def CheckDomains(domains):
    results = {}
    for domain in domains:
        try:
            for mx in dns.resolver.query(domain, 'MX'):
                if "protection.outlook.com" in mx.to_text().lower():
                    results[domain] = "O365"
                elif "aspmx.l.google.com" in mx.to_text().lower():
                    results[domain] = "GSuite"
                elif "googlemail.com" in mx.to_text().lower():
                    results[domain] = "GSuite (Maybe)"
                elif "mailcontrol.com" in mx.to_text().lower():
                    results[domain] = "Forcepoint"
                elif "messagelabs.com" in mx.to_text().lower():
                    results[domain] = "Symmantec"
                elif "mimecast" in mx.to_text().lower():
                    results[domain] = "Mimecast" 
                elif "pphosted.com" in mx.to_text().lower():
                    results[domain] = "Proofpoint"
                elif "ppe-hosted.com" in mx.to_text().lower():
                    results[domain] = "Proofpoint (Essentials)"
                elif "barracudanetworks.com" in mx.to_text().lower():
                    results[domain] = "Baracuda"
                elif "icritical.com" in mx.to_text().lower():
                    results[domain] = "iCritical/Fusemail"
                elif "trendmicro" in mx.to_text().lower():
                    results[domain] = "Trend Micro"
                else:
                    results[domain] = "Something else: {}".format(mx.to_text)
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
