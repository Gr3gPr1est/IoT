
import urllib2

controlURL = "http://192.168.100.100/onvif/device_service"

postData ='''<?xml
        version='1.0'
        encoding='utf-8'
        ?>
     <soap-env:Envelope
        xmlns:soap-env="http://www.w3.org/2003/05/soap-envelope">
        <soap-env:Header>
            <wsse:Security
                xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
                <wsse:UsernameToken>
                    <wsse:Username>
                        admin
                        </wsse:Username>
                    <wsse:Password
                        Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">
                        /password here/
                        </wsse:Password>
                    <wsse:Nonce
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">
                        fdsafdafdafdas
                        </wsse:Nonce>
                    <wsu:Created
                        xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                        2024-01-17T14:03:35+00:00
                        </wsu:Created>
                    </wsse:UsernameToken>
                </wsse:Security>
            </soap-env:Header>
            <soap-env:Body>
            <ns0:GetCapabilities
                xmlns:ns0="http://www.onvif.org/ver10/device/wsdl"/>
            </soap-env:Body>
        </soap-env:Envelope>'''
header = {
    'Host': u'192.168.100.100',
    'Content-Type': 'application/soap+xml; charset=utf-8;',
    'Content-Length': len(postData),
}

request_object = urllib2.Request(controlURL, postData, header)
response = urllib2.urlopen(request_object)

print (response.read())
