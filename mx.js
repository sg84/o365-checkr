var dns = require('dns');
//let domain = "gmail.com"
let o365host = "protection.outlook.com";
let domains = ["gmail.com", "outlook.com"];
let curr_mx = "";

function gotResult2(err, mxlist) {
    for (mx in mxlist) {
        console.log(mxlist[mx]);
        if(mxlist[mx].exchange.includes(o365host)) {
            console.log
            console.log("Match: " + mxlist[mx].exchange)
        }
    }
}



for (x in domains) {
    dns.resolveMx(domains[x], gotResult2)
}


