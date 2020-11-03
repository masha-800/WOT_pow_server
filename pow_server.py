from flask import Flask, request #import main Flask class and request object
from Crypto.Hash import keccak
#from datetime import datetime

app = Flask(__name__)
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

def pow(version,complexity,timestamp,resourse,extension,random_string):
    #startTime = datetime.now()
    var7='{0}:{1}:{2}:{3}:{4}:{5}:'.format(str(version),str(complexity),timestamp,resourse,extension,random_string)
    zero_quantity='0'*complexity
    for i in range(1,1000000):
      var10=f'{var7}{str(i)}'
      getbytes=var10.encode() 
      keccak_hash = keccak.new(digest_bits=512)
      keccak_hash.update(getbytes)
      var12=keccak_hash.hexdigest()
      check=var12.startswith(zero_quantity)
      if check:
        #fintime= datetime.now()-startTime
        #print(f'{fintime}')
        return i

def server():
    app = Flask(__name__)
    
    @app.route('/json-example', methods=['POST'])
    def json_example():
        req_data = request.get_json()
        version=req_data['pow']['algorithm']['version']
        complexity=req_data['pow']['complexity']
        timestamp=req_data['pow']['timestamp']
        resourse=req_data['pow']['algorithm']['resourse']
        extension=req_data['pow']['algorithm']['extension']
        random_string=req_data['pow']['random_string']
        work=pow(version,complexity,timestamp,resourse,extension,random_string)
        try:
            version=req_data['pow']['algorithm']['version']
            complexity=req_data['pow']['complexity']
            timestamp=req_data['pow']['timestamp']
            resourse=req_data['pow']['algorithm']['resourse']
            extension=req_data['pow']['algorithm']['extension']
            random_string=req_data['pow']['random_string']
            work=pow(version,complexity,timestamp,resourse,extension,random_string)
            return str(work)
        except:
            return 'captcha',403

    app.run(debug=False, port=5000)
    #app.run(ssl_context='adhoc',debug=True, port=5000)
if __name__ == "__main__":
    server()
    
