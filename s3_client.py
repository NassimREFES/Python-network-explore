import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

access_id = 'AKIAJ5ZOEN2FICRHVCAA'
access_key = 'lIuOAi4wQ6liwm5kSBoxz/s21hsrfy7QgOs4bM7B'
region = 'us-west-2'
endpoint = 's3-{}.amazonaws.com'.format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(xml_string):
    print (minidom.parseString(xml_string)).toprettyxml()
    
def create_bucket(bucket):
    #print('Bucket name: {}'.format(bucket))
    XML = ET.Element('CreateBucketConfiguration')
    XML.attrib['xmlns'] = ns
    location = ET.SubElement(XML, 'LocationConstraint')
    location.text = auth.region
    data = ET.tostring(XML, encoding='utf-8')
    #xml_pprint(data)
    url = 'http://{}.{}'.format(bucket, endpoint)
    r = requests.put(url, data=data, auth=auth)
    if r.ok:
        print('Created bucket{} OK'.format(bucket))
    else:
        xml_pprint(r.text)
    
if __name__ == '__main__':
    cmd, args = sys.argv[1:]
    globals()[cmd](args)